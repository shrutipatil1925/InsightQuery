import requests


FASTAPI_URL = "http://127.0.0.1:8001"


def analyze_data(database_name, question):

    url = f"{FASTAPI_URL}/api/chat"

    payload = {
        "database_name": database_name,
        "question": question
    }

    response = requests.post(
        url,
        json=payload
    )

    response.raise_for_status()

    return response.json()

def upload_csv(file):
    url = f"{FASTAPI_URL}/api/database/upload-csv"

    files = {
        "file": (
            file.name,
            file.read(),
            "text/csv"
        )
    }

    response = requests.post(
        url,
        files=files
    )

    response.raise_for_status()

    return response.json()