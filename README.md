# 🧮 Advanced Calculator App (Flask + Docker)

A powerful web-based calculator built with Python and Flask. Supports basic math, powers, trigonometry, square roots, logarithms, and more!

## 🔧 Features
- ✅ Addition, subtraction, multiplication, division
- ✅ Square root: `sqrt(x)`
- ✅ Powers: `2^3`
- ✅ Trigonometry: `sin(x)`, `cos(x)`, `tan(x)`
- ✅ Logs: `log(x)` (base 10), `ln(x)`
- ✅ Constants: `pi`, `e`
- ✅ Error handling and clean UI

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/calculator-app.git
cd calculator-app
2. Build the Docker image
bash
Copy
Edit
docker build -t calculator-app .
3. Run the container
bash
Copy
Edit
docker run -d -p 5000:5000 calculator-app
4. Open in browser
Visit: http://localhost:5000

🛠 Local Development (Optional)
bash
Copy
Edit
pip install flask
python app.py
📁 Project Structure
cpp
Copy
Edit
calculator-app/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
├── Dockerfile
└── README.md

