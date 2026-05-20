# LinkedIn AI Writing Assistant

An AI-powered LinkedIn content generation system built using LLMs, few-shot prompting, and retrieval-based generation.

The application generates context-aware LinkedIn posts by dynamically selecting relevant examples based on:

* topic
* tone
* language
* post length

instead of relying only on static prompting.

---

## Screenshots

### Home Interface

<img width="100%" alt="Home Interface" src="screenshots\img1.png">

---

### Generated LinkedIn Post

<img width="100%" alt="Generated Post" src="screenshots\img2.png">

---

## Features

* AI-powered LinkedIn post generation
* Few-shot prompting using real LinkedIn posts
* Tone-based content generation
* Dynamic retrieval using SQLite
* Metadata extraction and filtering
* Interactive Streamlit UI
* Copy-ready generated posts

---

## Tech Stack

* Python
* Streamlit
* LangChain
* SQLite
* Pandas
* Groq API

---

## Core Concepts Used

* Prompt Engineering
* Few-Shot Learning
* Retrieval-Augmented Generation (RAG)
* LLM Application Development
* Metadata-Based Retrieval
* AI-Assisted Content Generation

---

## System Flow

User Input
→ Example Retrieval
→ Prompt Construction
→ LLM Generation
→ LinkedIn Post Output

---

## Run Locally

Clone the repository:

```bash
git clone https://github.com/your-username/linkedin-ai-writing-assistant.git
cd linkedin-ai-writing-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
GROQ_API_KEY=your_api_key
```

Run the application:

```bash
streamlit run main.py
```

---

## Future Improvements

* Semantic search using embeddings
* Multi-creator writing styles
* Engagement prediction
* AI hook optimization
* Vector database integration


