from app.services.chart_service import (
    select_chart,
    create_chart
)


result = [
    {
        "species": "setosa",
        "average": 5.006
    },
    {
        "species": "versicolor",
        "average": 5.936
    },
    {
        "species": "virginica",
        "average": 6.588
    }
]


chart_type = select_chart(result)

print("Selected chart:", chart_type)


fig = create_chart(result, chart_type)

print("Chart created:", fig is not None)