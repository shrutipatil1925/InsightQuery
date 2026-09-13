from app.agents.graph import graph


state = {
    "database_name": "iris",
    "user_question": "Show the average sepal length for each species",
    "retry_count": 0
}

result = graph.invoke(state)

print("\nGenerated SQL:")
print(result["sql_query"])

print("\nValidation:")
print(result["is_valid"])

print("\nQuery Result:")
print(result["query_result"])

print("\nChart Type:")
print(result["chart_type"])

print("\nChart Created:")
print(result["chart"] is not None)

print("\nAI Insight:")
print(result["insight"])