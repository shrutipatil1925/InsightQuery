from llm_service import generate_sql


schema = """
Table: dataset

Columns:
sepal_length REAL
sepal_width REAL
petal_length REAL
petal_width REAL
species TEXT
"""

question = "Show the average petal length for each species."

sql = generate_sql(question, schema)

print("Generated SQL:")
print(sql)