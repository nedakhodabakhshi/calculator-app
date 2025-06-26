# 🧮 Advanced Calculator Web App (Flask + Docker)

A professional web-based **Advanced Calculator** built using **Python (Flask)** and **Docker**, supporting basic and scientific operations. Clean UI, mobile-friendly, and easy to deploy.

---

## 🚀 Features

✅ Basic arithmetic: `+`, `-`, `*`, `/`, `^`  
✅ Power and root: `2^3`, `sqrt(25)`  
✅ Trigonometry: `sin(x)`, `cos(x)`, `tan(x)`  
✅ Logarithms: `log(x)` (base 10), `ln(x)` (natural log)  
✅ Constants: `pi`, `e`  
✅ User-friendly math expressions  
✅ Input validation and error handling  
✅ Styled interface with HTML/CSS  
✅ Dockerized for easy deployment

---

## 📁 Project Structure

calculator-app/
├── app.py
├── templates/
│ └── index.html
├── static/
│ └── style.css
├── requirements.txt
├── Dockerfile
└── README.md

---

🐳 Docker Deployment
1. Build the Docker image

docker build -t calculator-app .

2. Run the Docker container
docker run -d -p 5000:5000 calculator-app

Visit: http://localhost:5000

