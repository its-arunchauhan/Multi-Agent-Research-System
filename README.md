# Multi-Agent Research System

A multi-agent research system built with LangChain that autonomously researches topics, gathers information from the web, generates structured reports, and evaluates report quality using specialized AI agents.

<p align="center">
  <strong>🔬 Research Automation • 🤖 Multi-Agent Orchestration • 📝 Intelligent Report Generation</strong>
</p>

---

## 🎯 Motivation

Research workflows often involve multiple repetitive steps: searching for information, reading articles, synthesizing findings, and evaluating report quality.

This project explores how a coordinated multi-agent architecture can automate these tasks using LLM-powered agents, enabling faster and more structured research generation.

---

## 🌟 Features

* **Multi-Agent Architecture** – Dedicated Search, Reader, Writer, and Critic agents
* **Automated Web Research** – Retrieves relevant information using Tavily Search
* **Smart Content Extraction** – Extracts and cleans content from web pages using multiple parsing strategies
* **AI-Powered Report Generation** – Produces structured research reports automatically
* **Quality Evaluation** – Critic agent scores reports and suggests improvements
* **Interactive UI** – Streamlit-based web interface
* **Pipeline Orchestration** – Coordinates the complete research workflow end-to-end
* **Modular Design** – Easily extensible agent and tool architecture

---

## 🏗️ System Architecture

```text
┌─────────────────────────────────────────────────────┐
│           Streamlit UI (app.py)                     │
│      Multi-Agent Research Assistant Interface       │
└──────────────────┬──────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────┐
│      Research Pipeline (pipeline.py)                │
│        Orchestrates multi-agent workflow            │
└──────────────────┬──────────────────────────────────┘
                   │
    ┌──────────────┼──────────────┐
    │              │              │
┌───▼───┐    ┌────▼─────┐   ┌───▼────┐
│Search │    │  Reader   │   │ Writer │
│Agent  │    │   Agent   │   │ Chain  │
└───┬───┘    └────┬─────┘   └───┬────┘
    │             │             │
    │  ┌──────────▼─────────┐   │
    └─▶│    Tools Layer     │◀──┘
       │                    │
       │ • web_search       │
       │ • scrape_url       │
       │                    │
       └────────┬───────────┘
                │
            ┌───▼────────┐
            │ Critic     │
            │ Chain      │
            └────────────┘
```

An editable version of the architecture diagram is available in:

```text
demo.excalidraw
```

---

## ⚙️ Internal Design

The system follows a sequential research workflow:

1. **Search Agent** discovers relevant sources using Tavily.
2. **Reader Agent** extracts and cleans content from retrieved URLs.
3. **Writer Chain** synthesizes findings into a structured report.
4. **Critic Chain** evaluates report quality and provides feedback.
5. Final results are displayed through the Streamlit UI or CLI.

### Agent Responsibilities

| Agent        | Responsibility                                 |
| ------------ | ---------------------------------------------- |
| Search Agent | Finds relevant sources and URLs                |
| Reader Agent | Extracts readable content from web pages       |
| Writer Chain | Generates structured research reports          |
| Critic Chain | Evaluates report quality and provides feedback |

---

## 🛠️ Technologies Used

| Technology       | Purpose                                  |
| ---------------- | ---------------------------------------- |
| LangChain        | Agent orchestration and chain management |
| Groq API         | Primary LLM provider for fast inference  |
| OpenAI API       | Optional LLM backend and experimentation |
| Streamlit        | Interactive web interface                |
| Tavily API       | Web search and information retrieval     |
| BeautifulSoup4   | HTML parsing                             |
| Trafilatura      | Web content extraction                   |
| Readability-lxml | Article extraction                       |
| Python-dotenv    | Environment configuration                |
| Rich             | Terminal output formatting               |

---

## 📋 Prerequisites

* Python 3.11+
* Tavily API Key
* Groq API Key

Optional:

* OpenAI API Key

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Multi-Agent-Research-System.git
cd Multi-Agent-Research-System
```

### 2. Create a Virtual Environment

Using Conda:

```bash
conda create -n langagent python=3.11 -y
conda activate langagent
```

Using venv:

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
OPENAI_API_KEY=your_openai_api_key
```

API Providers:

* OpenAI: https://platform.openai.com/api-keys
* Groq: https://console.groq.com/keys
* Tavily: https://tavily.com

---

## ⚙️ Configuration

Common configuration values can be adjusted inside the source code:

* Model selection (Groq/OpenAI)
* Temperature settings
* Number of search results
* Scraping behavior
* Agent prompts

---

## 💡 Usage

### Run the Streamlit Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

### Run from the Command Line

```bash
python main.py
```

Modify the topic variable in `main.py` to research different subjects.

---

## 🔄 Workflow

1. User enters a research topic.
2. Search Agent gathers relevant sources.
3. Reader Agent extracts article content.
4. Writer Chain creates a structured report.
5. Critic Chain evaluates the report.
6. Results are displayed to the user.

---

## 📌 Example

### Input

```text
Impact of Large Language Models on Software Engineering
```

### Output

```text
Research Report
├── Introduction
├── Background
├── Key Findings
├── Analysis
├── Conclusion
└── References

Critic Evaluation
├── Score: 8.7/10
├── Strengths
└── Improvement Suggestions
```

---

## 📁 Project Structure

```text
.
├── app.py                      # Streamlit web interface
├── main.py                     # CLI entry point
├── requirements.txt            # Project dependencies
├── README.md
├── LICENSE
├── demo.excalidraw             # Editable architecture diagram
├── tests/
│   ├── test_critic.py
│   ├── test_groq.py
│   ├── test_groq_sdk.py
│   ├── test_langchain_groq.py
│   ├── test_pipeline.py
│   ├── test_project_llm.py
│   ├── test_reader_agent.py
│   ├── test_search_agent.py
│   ├── test_tools.py
│   └── test_writer.py
│
└── src/
    ├── agents/
    │   └── agents.py
    ├── tools/
    │   └── tools.py
    └── pipelines/
        └── pipeline.py
```

---

## 🧪 Running Tests

Run all tests:

```bash
pytest tests/
```

Run a specific test:

```bash
pytest tests/test_pipeline.py
```

---

## ⚠️ Limitations

* Quality depends on the availability and quality of web sources.
* Some websites may block scraping or restrict access.
* LLM-generated reports may contain inaccuracies or hallucinations.
* API rate limits can affect performance.
* Research quality depends on retrieved source coverage.

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📚 References

* LangChain: https://python.langchain.com
* Streamlit: https://streamlit.io
* Tavily: https://tavily.com
* Groq: https://groq.com

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 🙏 Acknowledgments

* LangChain
* Tavily
* Streamlit
* Groq

---

## 📧 Support

If you encounter an issue, please open a GitHub issue in this repository.

**Happy Researching! 🚀**
