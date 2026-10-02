# InsightQuery 📊💬

> An AI-powered conversational data analysis platform that allows users to upload datasets, ask questions in natural language, generate SQL queries, and visualize data insights.

**InsightQuery** is a conversational data-analysis application designed to make data exploration easier without requiring users to manually write SQL queries.

Users can upload a CSV dataset and ask questions such as:

```text
"What is the average age of passengers?"
```

The application processes the question, generates an appropriate SQL query, executes it against the dataset, and presents the result in a user-friendly format.

---

## 🚀 Features

### 📁 CSV Dataset Upload

Users can upload CSV datasets through the application.

The uploaded dataset is converted into a SQLite database for querying.

```text
CSV File
   ↓
SQLite Database
   ↓
Dataset Table
```

### 💬 Natural Language Data Queries

Users can ask questions about their datasets using natural language instead of manually writing SQL.

Examples:

```text
How many passengers survived?

What is the average age?

Which passenger class has the highest number of passengers?

Show the distribution of passengers by gender.
```

### 🤖 Natural Language → SQL

InsightQuery converts natural-language questions into SQL queries.

```text
User Question
      ↓
   AI Model
      ↓
Generated SQL
      ↓
SQLite Database
      ↓
Query Result
```

Example:

```sql
SELECT COUNT(*)
FROM dataset
WHERE Survived = 1;
```

### 📊 Data Visualization

Query results can be represented using **Plotly** visualizations.

Depending on the query and result structure, the application can generate visualizations such as:

- Bar charts
- Line charts
- Pie charts
- Scatter plots

This allows users to understand data through both results and visual representations.

### 🗂️ Conversational Chat History

InsightQuery maintains conversations so users can continue asking questions about their dataset.

Example:

```text
User:
What is the average age?

AI:
The average age is approximately 29.7 years.

User:
What about the survived passengers?

AI:
The average age of survived passengers is ...
```

### 📝 Automatic Chat Naming

Chats can be given meaningful names based on the conversation, making it easier to identify previous analyses.

### 🗄️ Dataset Management

Uploaded datasets are stored and associated with their corresponding SQLite databases.

The application can work with multiple datasets instead of requiring users to manually create database tables.

---

## 🏗️ System Architecture

InsightQuery uses a **Django + FastAPI** architecture.

```text
                         ┌──────────────┐
                         │     User     │
                         └──────┬───────┘
                                │
                                ▼
                     ┌────────────────────┐
                     │   Django Frontend  │
                     │  Authentication &  │
                     │   Chat Interface   │
                     └─────────┬──────────┘
                               │
                               ▼
                     ┌────────────────────┐
                     │   Django Backend   │
                     │                    │
                     │ • Users            │
                     │ • Chats            │
                     │ • Dataset Upload   │
                     └─────────┬──────────┘
                               │
                               │ API Request
                               ▼
                     ┌────────────────────┐
                     │   FastAPI Service  │
                     │                    │
                     │ • Question         │
                     │   Processing       │
                     │ • SQL Generation   │
                     │ • Query Execution  │
                     └─────────┬──────────┘
                               │
                               ▼
                     ┌────────────────────┐
                     │  SQLite Database   │
                     │                    │
                     │     dataset        │
                     └─────────┬──────────┘
                               │
                               ▼
                     ┌────────────────────┐
                     │   Query Result     │
                     └─────────┬──────────┘
                               │
                               ▼
                     ┌────────────────────┐
                     │ Plotly / Response  │
                     │   Visualization    │
                     └────────────────────┘
```

---

## 🔄 How InsightQuery Works

### 1. Upload Dataset

The user uploads a CSV file.

```text
dataset.csv
     ↓
Django
     ↓
SQLite Database
```

The uploaded CSV is converted into a SQLite database containing a `dataset` table.

### 2. Ask a Question

The user asks a question in natural language.

```text
"What is the average fare by passenger class?"
```

### 3. Send Question to FastAPI

Django communicates with the FastAPI service to process the data-analysis request.

```text
Django
   ↓
FastAPI
```

### 4. Generate SQL

The AI system converts the natural-language question into SQL.

```text
Natural Language
       ↓
      AI
       ↓
      SQL
```

Example:

```sql
SELECT Pclass, AVG(Fare)
FROM dataset
GROUP BY Pclass;
```

### 5. Execute SQL

The generated SQL query is executed against the corresponding SQLite database.

```text
Generated SQL
      ↓
SQLite
      ↓
Query Result
```

### 6. Generate Visualization

The result is analyzed to determine an appropriate visualization.

```text
Query Result
     ↓
Visualization Logic
     ↓
Plotly Chart
```

### 7. Display Result

The user receives the result through the conversational interface.

```text
Question
   ↓
SQL
   ↓
Result
   ↓
Chart + Explanation
```

---

## 📊 Example Workflow

Suppose the user uploads the Titanic dataset.

```text
Titanic.csv
    ↓
SQLite
    ↓
dataset table
```

The user asks:

```text
How many passengers survived?
```

InsightQuery processes the question:

```text
Natural Language Question
          ↓
      SQL Generation
          ↓
SELECT COUNT(*)
FROM dataset
WHERE Survived = 1
          ↓
     Query Execution
          ↓
       Result: 152
```

The result can then be displayed through the conversational interface.

---

## 🧠 Natural Language to SQL

One of the core components of InsightQuery is converting human language into executable SQL.

### Traditional Data Analysis

```text
User
 ↓
Learn SQL
 ↓
Write Query
 ↓
Execute Query
 ↓
Analyze Result
```

### InsightQuery

```text
User
 ↓
Ask Question
 ↓
AI generates SQL
 ↓
Execute Query
 ↓
Analyze Result
```

This makes structured-data exploration more accessible to users who are not familiar with SQL syntax.

---

## 📈 Visualization Pipeline

```text
User Question
      ↓
Generated SQL
      ↓
Database Query
      ↓
Query Result
      ↓
Data Analysis
      ↓
Plotly
      ↓
Interactive Visualization
```

Example:

```text
Question:
Show the number of passengers in each class.

        ↓

SQL:
SELECT Pclass, COUNT(*)
FROM dataset
GROUP BY Pclass;

        ↓

Result:
Pclass | Count
-------|------
1      | ...
2      | ...
3      | ...

        ↓

Plotly Bar Chart
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| Django | Web application, authentication, and chat management |
| FastAPI | Data-analysis API service |
| SQLite | Dataset storage and SQL execution |
| Pandas | CSV and data processing |
| Plotly | Interactive data visualization |
| SQL | Data querying |
| HTML/CSS | Frontend interface |
| JavaScript | Frontend interactions |
| AI/LLM | Natural-language-to-SQL generation |

---

## 📁 Project Structure

```text
InsightQuery/
│
├── backend/
│   │
│   ├── django_app/
│   │   │
│   │   ├── accounts/
│   │   ├── chats/
│   │   ├── insightquery/
│   │   ├── templates/
│   │   └── manage.py
│   │
│   └── fastapi_app/
│       ├── ...
│       └── ...
│
├── data/
│   └── databases/
│       └── dataset.db
│
├── static/
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> Update the folder names above if your current repository structure differs.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shrutipatil1925/InsightQuery.git
```

Move into the project:

```bash
cd InsightQuery
```

### 2. Create a Virtual Environment

#### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

#### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file and add the required API credentials.

For example:

```env
GOOGLE_API_KEY=your_api_key
```

If the current implementation uses additional API keys, configure them according to the project configuration.

**Never commit API keys to GitHub.**

Add the following to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

---

## ▶️ Running the Project

InsightQuery contains two backend services:

```text
Django
   +
FastAPI
```

Both services need to be running.

### Start Django

From the Django application directory:

```bash
python manage.py runserver
```

### Start FastAPI

From the FastAPI application directory:

```bash
uvicorn main:app --reload --port 8001
```

> Use the port configured in your current project if it differs.

---

## 💻 Example Use Cases

### Dataset Exploration

```text
What is the average age?
```

### Group Analysis

```text
What is the average fare for each passenger class?
```

### Filtering

```text
How many passengers were above 50 years old?
```

### Aggregation

```text
Which gender has more survivors?
```

### Visualization

```text
Show the number of passengers in each class.
```

---

## 📚 Sample Datasets

InsightQuery can be tested with datasets such as:

- Titanic dataset
- Iris dataset
- Other structured CSV datasets

Example workflow:

```text
Titanic.csv
     ↓
CSV Upload
     ↓
SQLite
     ↓
Natural Language Question
     ↓
SQL
     ↓
Result
     ↓
Visualization
```

---

## 🔑 Core Concepts Demonstrated

### Django

Used for:

- User authentication
- Web application logic
- Chat management
- Dataset upload
- Database interaction

### FastAPI

Used as a separate API service for data-analysis operations.

### SQL

Used for:

- Filtering
- Aggregation
- Grouping
- Sorting
- Data analysis

### Natural Language to SQL

Allows users to interact with structured data using natural language.

### SQLite

Provides a lightweight database for uploaded datasets.

### Plotly

Provides interactive visualizations for query results.

### API Communication

Django communicates with the FastAPI service to process data-analysis requests.

---

## 🎯 Why InsightQuery?

Traditional data analysis often requires users to know:

```text
Python
SQL
Pandas
Data Visualization
```

InsightQuery provides a conversational layer:

```text
              User
                │
                ▼
       Natural Language
                │
                ▼
         InsightQuery
                │
        ┌───────┴───────┐
        ▼               ▼
       SQL           Visualization
        │               │
        └───────┬───────┘
                ▼
             Insight
```

The goal is to make structured-data exploration more accessible through natural-language interaction.

---

## ⚠️ Current Limitations

- SQL generation depends on the quality of the AI model.
- Complex natural-language questions may produce incorrect SQL.
- Uploaded CSV files must contain structured/tabular data.
- Very large datasets may require more scalable database infrastructure.
- Visualization selection can be improved for more complex analytical questions.
- Generated SQL should be validated before execution in a production environment.

---

## 🔮 Future Improvements

### 🔒 SQL Safety

Add SQL validation and query restrictions before executing AI-generated queries.

### 🧠 Better Text-to-SQL

Improve SQL generation using:

- Schema-aware prompting
- Few-shot examples
- Query validation
- SQL correction
- Query retry mechanisms

### 📊 Advanced Analytics

Add support for:

- Correlation analysis
- Trend detection
- Statistical summaries
- Outlier detection
- Predictive analysis

### 📈 More Visualizations

Automatically select from:

- Bar charts
- Line charts
- Scatter plots
- Histograms
- Heatmaps
- Box plots

### 🗃️ Multiple Database Support

Extend beyond SQLite to:

- PostgreSQL
- MySQL
- DuckDB

### 🤖 Agentic Data Analysis

Future versions could use multiple specialized agents:

```text
                    Data Analyst Agent
                           │
            ┌──────────────┼──────────────┐
            ▼              ▼              ▼
       SQL Agent      Visualization    Insight
                         Agent           Agent
            │              │              │
            └──────────────┼──────────────┘
                           ▼
                     Final Response
```

---

## 📈 Learning Outcomes

Through InsightQuery, the project demonstrates practical experience with:

- Python
- Django
- FastAPI
- REST APIs
- SQL
- SQLite
- Pandas
- Plotly
- Natural Language Processing
- Natural Language to SQL
- AI-powered data analysis
- Dataset processing
- Conversational applications
- Frontend-backend communication

---

## 👩‍💻 Author

**Shruti Patil**

**Aspiring AI/ML Engineer**

GitHub:  
https://github.com/shrutipatil1925

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is intended for educational and portfolio purposes.