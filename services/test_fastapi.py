from services.fastapi_service import analyze_data


result = analyze_data(
    "iris",
    "Which species has the highest average sepal length?"
)

print("\nFastAPI Response:")
print(result)