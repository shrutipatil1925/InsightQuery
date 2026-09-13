from app.services.insight_service import generate_insight


result = [
    {"species": "setosa", "average": 5.006},
    {"species": "versicolor", "average": 5.936},
    {"species": "virginica", "average": 6.588}
]

insight = generate_insight(
    "Show the average sepal length for each species",
    result
)

print("\nAI Insight:")
print(insight)