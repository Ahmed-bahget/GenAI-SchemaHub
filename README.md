# GenAI-SchemaHub

A powerful FastAPI-based backend that dynamically generates structured text using predefined schemas and integrates AI-based text regeneration and Google Custom Image Search.

---

## 🚀 Features

- 🔧 Select from multiple pre-defined schemas for structured content generation.
- ✍️ Regenerate text using AI (powered by Gradio Gemini API).
- 🔍 Search for related images using Google Custom Search API.
- 🌐 CORS enabled for frontend integration.
- 📄 Swagger docs for easy API testing and exploration.

---

## 📥 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/ai-schema-generator.git
cd ai-schema-generator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
Open docs in your browser: http://localhost:8000/docs
