# 📬 Cold Mail Generator – AI-Powered Outreach Assistant

**Cold Mail Generator** is a Streamlit-based application that uses **LLMs** to generate personalized cold emails for various professional use cases, such as job outreach, networking, product pitches, or B2B sales — with minimal user input.

Powered by **LangChain**, **LLMs (via Ollama)**, and custom templates, the app transforms basic details into polished, context-aware email drafts ready to send.

---

## 💼 Use Cases

- 🔍 **Job Hunting** — Generate tailored outreach emails to recruiters
- 💬 **Networking** — Connect with professionals on LinkedIn/email
- 📈 **Startup/SaaS Pitch** — Contact potential customers or investors
- 🛠️ **Freelancer/Consultant Outreach** — Propose services to prospects

---

## ⚙️ Tech Stack

| Tech              | Purpose                                      |
|-------------------|----------------------------------------------|
| **Streamlit**     | Interactive frontend for user input/output   |
| **LangChain**     | Prompt templating, agent routing             |
| **Ollama + LLM**  | Local LLM (e.g., Mistral) for text generation|
| **Python-dotenv** | Secure environment variable handling         |
| **Rich**          | Colored logging for better error handling    |

---

## 🧠 How It Works

1. **User Input**:
   - Name, target role, company, type of outreach
2. **Prompt Template**:
   - Dynamically inserts user details into a cold-email prompt
3. **LLM Generation**:
   - Generates a well-structured, natural-language email
4. **Output**:
   - Displays the final result in Streamlit and allows copy/export

---

## 📷 Demo

![Cold Mail Generator Demo](https://raw.githubusercontent.com/AniEE107/Cold-Mail-Generator/main/cold-mail.png)

> The interface is minimal, fast, and user-friendly — ideal for generating outreach emails in under 10 seconds.

---

## 📁 Project Structure

Cold-Mail-Generator/
├── app/
│ └── cold_mail_generator.ipynb # Main Streamlit UI
├── templates/
│ └── prompts.txt # Email prompt templates
├── .env # API keys/config (not committed)
├── requirements.txt
└── README.md
