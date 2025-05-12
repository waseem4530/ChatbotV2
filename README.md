# 🤖 ChatbotV2 – AI Chat Widget Using Groq API & Flask

This project is a beautiful, responsive chat widget powered by the **Groq LLM API**. It's built using **Flask (Python)** for the backend and **HTML, CSS, Bootstrap, and JavaScript** for the frontend. The chatbot communicates with the `llama-3.3-70b-versatile` model via Groq and streams helpful responses to the user.

---

## 🚀 Features

- 🧠 Uses Groq’s blazing-fast LLM (`llama-3.3-70b-versatile`)
- 💬 Chat interface with user & AI messages styled cleanly
- 🌐 Built with Flask, Bootstrap, HTML, CSS, and JavaScript
- 🔐 API Key authentication with Groq
- 📦 Easy to run locally


---

## 📁 Project Structure

```
ChatbotV2/
├── app.py
├── templates/
│   └── index.html
├── static/               # (Optional)
├── requirements.txt      # Optional
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/waseem4530/ChatbotV2.git
cd ChatbotV2
```

### 2. Install Dependencies

```bash
pip install flask groq
```

### 3. Add Your Groq API Key

Replace `"your_api_key_here"` in `app.py` with your actual API key:

```python
client = Groq(api_key="your_api_key_here")
```

### 4. Run the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

---

## 🛠 How It Works

- The user enters a message in the chat prompt.
- The message is sent to Flask backend.
- Flask calls `generate_responses()` using Groq API.
- LLM’s response is returned and shown in the UI.

---

## 🌐 Groq API Docs

👉 [https://console.groq.com/docs](https://console.groq.com/docs)

---

## 📌 Future Enhancements

- [ ] Chat history
- [ ] User login
- [ ] Typing animation
- [ ] Deploy online

---

## 📄 License

MIT License

---

## 🙌 Author

**Waseem4530**  
[GitHub](https://github.com/waseem4530)
