
# 🤖 Agentia Assistant

![image](https://raw.githubusercontent.com/ambideXtrous9/Agentia-Agentic-Chatbot-Assistant/refs/heads/main/agentia.jpg)

**Your intelligent AI-powered chat assistant** ✨

---

## 🌟 Features

- 🗨️ **Natural Conversations**: Human-like chat experience powered by Qwen2.5-0.5B-Instruct  
- 📚 **Multiple Chat Sessions**: Organize conversations by topics or projects  
- 🔍 **Smart Search**: DuckDuckGo integration for real-time information  
- 💾 **Persistent Memory**: Chat history saved across sessions  
- 🎨 **Beautiful UI**: Clean, modern interface with dark/light mode support  

---

## 🚀 Quick Start

### 1. Install requirements
```bash
pip install -r requirements.txt
```

### 2. Run the application
```bash
streamlit run app.py
```

### 3. Start chatting! Ask Agentia anything:
```
"Explain quantum computing"  
"Write Python code for a REST API"  
"Latest news about AI advancements"
```

---

## 🛠️ Technical Stack

| Component     | Technology              |
|---------------|--------------------------|
| **AI Model**  | Qwen2.5-0.5B-Instruct     |
| **Framework** | Streamlit                |
| **Search**    | DuckDuckGo Search API    |
| **Vector DB** | FAISS                    |
| **Embeddings**| BAAI/bge-small-en        |

---
```
## 🖼️ Screenshots

<div align="center">
  <img src="screenshots/chat-example.png" width="45%" alt="Chat Example">
  <img src="screenshots/sidebar.png" width="45%" alt="Sidebar View">
</div>
```
---

## 🧩 Project Structure

```
agentia/
├── app.py                 # Main application
├── models/                # AI model handling
├── services/              # Business logic
├── tools/                 # External integrations
├── utils/                 # Helper functions
└── assets/                # Images and resources
```

---

## 💡 Usage Examples

```python
# Ask coding questions
response = agentia.ask("Write a Python function to reverse a string")

# Get news summaries
news = agentia.search("Latest breakthroughs in renewable energy")
```

---

## 🌈 Customization

- Replace `agentia.png` with your own logo (400x400 recommended)  
- Modify `config/prompts.py` to change AI behavior  
- Adjust `utils/display.py` for UI and theme customization  

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository  
2. Create your feature branch  
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes  
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. Push to the branch  
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 📬 Contact

**Project Maintainer** – *Your Name*

---

<p align="center">✨ Happy chatting with Agentia! ✨</p>
<div align="center">
  <img src="agentia.png" width="100" alt="Agentia Logo">
</div>
