from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
import pandas as pd
import io
import sqlite3
import os
from pathlib import Path

router = APIRouter()

class SQLRequest(BaseModel):
    query:str

#Database folder
BASE_DIR = Path(__file__).resolve().parents[4]
DATABASE_DIR =  BASE_DIR/"data"/"databases"
os.makedirs(DATABASE_DIR, exist_ok=True)

@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):

    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are allowed"
        )

    contents = await file.read()

    try:
        df = pd.read_csv(io.BytesIO(contents))
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Unable to read CSV file"
        )
        
    database_name = Path(file.filename).stem
    database_path = DATABASE_DIR / f"{database_name}.db"
    
    table_name = "dataset"
    conn = sqlite3.connect(database_path)
    
    try:
        df.to_sql(table_name, conn, if_exists="replace", index=False)
    finally:
        conn.close()
        
    return {
        "message" : "CSV uploaded and database created successfully",
        "filename": file.filename,
        "database": database_path,
        "table": table_name,
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": df.columns.tolist()
    }
    
@router.get("/schema/{database_name}")
def get_schema(database_name: str):

    database_path = DATABASE_DIR / f"{database_name}.db"

    if not database_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Database not found"
        )

    conn = sqlite3.connect(database_path)

    try:
        cursor = conn.cursor()

        # Get tables
        cursor.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table'
        """)

        tables = cursor.fetchall()

        if not tables:
            raise HTTPException(
                status_code=404,
                detail="No tables found in database"
            )

        table_name = tables[0][0]

        # Get column information
        cursor.execute(f"PRAGMA table_info('{table_name}')")

        columns = cursor.fetchall()

    finally:
        conn.close()

    schema = []

    for column in columns:
        schema.append({
            "column_name": column[1],
            "data_type": column[2]
        })

    return {
        "database": database_name,
        "table": table_name,
        "columns": schema
    }
    
@router.post("/execute-sql/{database_name}")
def validate_sql(query: str):

    query = query.strip().lower()

    if not query:
        return False, "SQL query cannot be empty"

    if not query.startswith("select"):
        return False, "Only SELECT queries are allowed"

    forbidden_keywords = [
        "insert",
        "update",
        "delete",
        "drop",
        "alter",
        "create",
        "replace",
        "attach",
        "detach",
        "pragma"
    ]

    for keyword in forbidden_keywords:
        if keyword in query:
            return False, f"Forbidden SQL keyword: {keyword}"

    return True, "SQL query is valid"

def execute_sql(database_name: str, request: SQLRequest):

    database_path = DATABASE_DIR / f"{database_name}.db"

    if not database_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Database not found"
        )

    query = request.query.strip()

    is_valid, message = validate_sql(query)

    if not is_valid:
        raise HTTPException(
            status_code=400,
            detail=message
    )

    conn = sqlite3.connect(database_path)

    try:
        cursor = conn.cursor()

        cursor.execute(query)

        rows = cursor.fetchall()

        columns = [
            description[0]
            for description in cursor.description
        ]

    except sqlite3.Error as e:
        raise HTTPException(
            status_code=400,
            detail=f"SQL Error: {str(e)}"
        )

    finally:
        conn.close()

    result = []

    for row in rows:
        result.append(dict(zip(columns, row)))

    return {
        "database": database_name,
        "query": query,
        "columns": columns,
        "rows": result,
        "row_count": len(result)
    }
    
