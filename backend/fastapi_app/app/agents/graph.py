from app.agents.state import InsightQueryState
from app.api.database import DATABASE_DIR
from app.services.llm_service import generate_sql
from app.api.database import validate_sql
from langgraph.graph import StateGraph, START, END
from app.services.chart_service import select_chart, create_chart
from app.services.insight_service import generate_insight
import sqlite3


def get_schema(state: InsightQueryState):

    database_name = state["database_name"]

    database_path = DATABASE_DIR / f"{database_name}.db"

    conn = sqlite3.connect(database_path)

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table'
        """)

        tables = cursor.fetchall()

        table_name = tables[0][0]

        cursor.execute(f"PRAGMA table_info('{table_name}')")

        columns = cursor.fetchall()

    finally:
        conn.close()

    schema = []

    for column in columns:
        column_name = column[1]
        data_type = column[2]

        schema.append(
            f"{column_name} ({data_type})"
        )

    schema_text = f"Table: {table_name}\n"
    schema_text += "Columns:\n"
    schema_text += "\n".join(schema)

    state["schema"] = schema_text

    return state

def generate_sql_node(state: InsightQueryState):

    question = state["user_question"]
    schema = state["schema"]

    sql_query = generate_sql(
        question,
        schema
    )

    state["sql_query"] = sql_query

    state["retry_count"] = state.get("retry_count", 0) + 1

    return state

def validate_sql_node(state: InsightQueryState):

    sql_query = state["sql_query"]

    is_valid, message = validate_sql(sql_query)

    state["is_valid"] = is_valid
    state["validation_message"] = message

    return state

def execute_sql_node(state: InsightQueryState):

    database_name = state["database_name"]
    sql_query = state["sql_query"]

    database_path = DATABASE_DIR / f"{database_name}.db"

    conn = sqlite3.connect(database_path)

    try:
        cursor = conn.cursor()

        cursor.execute(sql_query)

        rows = cursor.fetchall()

        columns = [
            description[0]
            for description in cursor.description
        ]

    finally:
        conn.close()

    result = [
        dict(zip(columns, row))
        for row in rows
    ]

    state["query_result"] = result

    return state

def check_sql(state: InsightQueryState):
    if state["is_valid"]:
        return "execute_sql"
    if state["retry_count"] >= 3:
        return "end"
    return "generate_sql"

def chart_node(state: InsightQueryState):

    result = state["query_result"]

    chart_type = select_chart(result)

    chart = create_chart(
        result,
        chart_type
    )

    state["chart_type"] = chart_type
    state["chart"] = chart

    return state

def insight_node(state: InsightQueryState):
    question = state["user_question"]
    result = state["query_result"]

    insight = generate_insight(
        question,
        result
    )

    state["insight"] = insight

    return state

builder = StateGraph(InsightQueryState)

builder.add_node("get_schema", get_schema)
builder.add_node("generate_sql", generate_sql_node)
builder.add_node("validate_sql", validate_sql_node)
builder.add_node("execute_sql", execute_sql_node)
builder.add_node("chart", chart_node)
builder.add_node("insight", insight_node)

builder.add_edge(START, "get_schema")
builder.add_edge("get_schema", "generate_sql")
builder.add_edge("generate_sql", "validate_sql")
builder.add_conditional_edges(
    "validate_sql",
    check_sql,
    {
        "execute_sql": "execute_sql",
        "generate_sql": "generate_sql",
        "end": END
    }
)
builder.add_edge("execute_sql", "chart")
builder.add_edge("chart", "insight")
builder.add_edge("insight", END)

graph = builder.compile()