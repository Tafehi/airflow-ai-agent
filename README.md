# 🤖 AI Agent for Communicating with Apache Airflow DAGs

This project demonstrates how to build an AI agent that can interact with your Apache Airflow DAGs using natural language. The agent leverages **Langchain AI**, **Gemini 2.0 Flash**, and the **Airflow REST API** to provide a conversational interface for querying and managing DAGs. The airflow platform is made via [astro](https://www.astronomer.io/docs/astro/)


## 🚀 Features

- 🔍 Query DAG status, schedule, and metadata using natural language
- 🛠️ Build custom tools to interact with the Airflow API
- 🧠 Use Langchain AI to structure and validate agent responses
- ⚡ Integrate Gemini 2.0 Flash for fast and efficient LLM responses
- 🧪 Test and validate agent interactions with real DAGs

---

## 🧰 Tech Stack
- **Python 3.10+**
- **Apache Airflow 2.7+**
- **Langchain AI**
- **Gemini 2.0 Flash**
- **FastAPI** (optional for serving the agent)
- **LangChain** (optional for tool orchestration)

---

## ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/ai-airflow-agent.git
cd ai-airflow-agent
```
---
2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure environment variables
Create a .env file with the following:

```bash
AIRFLOW_API_URL=http://localhost:8080/api/v1
AIRFLOW_API_KEY=your_api_key_here
```

5. Run the agent
```bash
python agent/agent.py
```

---

🧪 Example Queries
* "What is the status of the daily_sales_report DAG?"
* "When is the next run of etl_pipeline?"
* "List all failed DAGs in the last 24 hours."
* "Trigger the data_cleanup DAG now."
---

📌 Notes
* Ensure your Airflow instance has the REST API enabled and accessible.
* You may need to configure CORS or authentication depending on your setup.
* Gemini 2.0 Flash requires API access—check Gemini documentation for setup.

---

🙌 Credits
* Data with Marc for the original tutorial
* Langchain AI for structured agent design
* Gemini 2.0 Flash for LLM integration