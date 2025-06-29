# 🎓 EduHaiku Agent 🤖🌿

A command-line AI agent that detects the topic of any educational question and responds in **haiku format** using Gemini API (OpenAI-compatible interface).

---

## ✨ Features

- 🧠 Topic detection using Gemini
- 📜 Poetic answers in 5-7-5 haiku style
- 💻 Minimal CLI interface
- 🚀 Fast Gemini-2.0 Flash model
- 🧪 Tested across 20+ educational topics

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/muhammadwaheedairi/eduhaiku-agent.git
cd eduhaiku-agent
````

### 2. Create a virtual environment using `uv`

```bash
uv venv
```

### 3. Activate the virtual environment

#### 🪟 Windows:

```bash
.venv\Scripts\activate
```

#### 🐧 Mac/Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
uv pip install -r requirements.txt
```

---

## 🔐 Setup API Key

1. Create a `.env` file in the root folder
2. Paste your Gemini API key:

```env
GEMINI_API_KEY=your-real-gemini-api-key-here
```

> See `.env.example` for reference

---

## 🚀 Run the Agent

```bash
python main.py
```

💬 You'll be prompted to ask an educational question.

---

## 🧪 Sample Output

```
Ask your educational question: What is gravity?

📚 Detected Topic: Physics

🎓 Haiku Response:

A force unseen pulls,  
Objects drawn to center mass,  
Earth's gentle embrace.
```

---

## 📂 Project Structure

```
eduhaiku-agent/
├── main.py
├── .env
├── .env.example
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🤝 Credits

Built with ❤️ by **Muhammad Waheed**
Follow the journey: [@muhammadwaheedairi](https://github.com/muhammadwaheedairi)

---
