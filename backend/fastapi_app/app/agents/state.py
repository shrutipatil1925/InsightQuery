from typing import TypedDict, Any


class InsightQueryState(TypedDict, total=False):
    database_name: str
    user_question: str
    schema: str
    sql_query: str
    is_valid: bool
    validation_message: str
    query_result: Any
    retry_count: int
    chart_type: str
    chart: Any
    insight: str