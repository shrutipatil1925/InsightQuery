from django.shortcuts import render
from services.fastapi_service import analyze_data, upload_csv
from django.contrib.auth.decorators import login_required
import json

@login_required
def chat(request):
    context = {}

    if request.method == "POST":

        # CSV upload
        uploaded_file = request.FILES.get("file")

        if uploaded_file:
            try:
                result = upload_csv(uploaded_file)

                context["upload_success"] = True
                context["filename"] = result.get("filename")
                context["database_name"] = uploaded_file.name.rsplit(".", 1)[0]
                context["rows"] = result.get("rows")
                context["columns"] = result.get("columns")
                context["column_names"] = result.get("column_names")

            except Exception as e:
                context["error"] = str(e)

        # Question
        question = request.POST.get("question", "").strip()

        if question:
            database_name = request.POST.get(
                "database_name",
                "iris"
            )

            try:
                result = analyze_data(
                    database_name,
                    question
                )

                context["question"] = question
                context["sql_query"] = result.get("sql_query")
                context["query_result"] = result.get("query_result")
                context["chart_type"] = result.get("chart_type")
                if result.get("chart"):
                    context["chart"] = json.loads(result["chart"])
                else:
                    context["chart"] = None
                context["insight"] = result.get("insight")

            except Exception as e:
                context["error"] = str(e)

    return render(
        request,
        "chats/chat.html",
        context
    )
    
def datasets(request):
    return render(request, "chats/datasets.html")


def history(request):
    return render(request, "chats/history.html")