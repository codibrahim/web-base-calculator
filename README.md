# 🧮 Web Base Calculator

A modern web-based calculator built with **Flask** and **Python**. Features a sleek glassmorphism UI and supports keyboard input.

---

## ✨ Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- ⚠️ Division by zero protection
- ⌨️ Full keyboard support
- 🎨 Modern glassmorphism design
- 🐳 Docker ready

---

## 🚀 How to Run

### Option 1 — Run Locally with Python

**Requirements:** Python 3.x

```bash
# 1. Clone the repository
git clone git@github.com:codibrahim/web-base-calculator.git
cd web-base-calculator

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the app
python app.py
```

Open your browser at **http://localhost:5000**

---

### Option 2 — Run with Docker 🐳

**Requirements:** [Docker](https://www.docker.com/get-started) installed

```bash
# 1. Clone the repository
git clone git@github.com:codibrahim/web-base-calculator.git
cd web-base-calculator

# 2. Build the Docker image
docker build -t web-base-calculator .

# 3. Run the container
docker run -p 5000:5000 web-base-calculator
```

Open your browser at **http://localhost:5000**

---

## ☁️ Deploy

### Deploy to Render (Free)

1. Go to [render.com](https://render.com) and sign up
2. Click **"New Web Service"** → connect your GitHub repo
3. Set the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
4. Click **"Create Web Service"**

---

## 📁 Project Structure

```
web-base-calculator/
├── app.py              # Flask backend & API routes
├── templates/
│   └── index.html      # Calculator UI (HTML + CSS + JS)
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── .dockerignore       # Files to exclude from Docker build
├── .gitignore          # Files to exclude from Git
└── README.md           # Project documentation
```

---

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `0-9` | Input numbers |
| `+ - * /` | Operators |
| `Enter` or `=` | Calculate |
| `Backspace` | Delete last character |
| `Escape` | Clear all |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
