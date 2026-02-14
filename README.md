🌱 EcoSphere AI
Environmental Intelligence Dashboard

EcoSphere AI is a Python-based environmental intelligence system that simulates environmental sensor data, analyzes risks, predicts future trends using AI, and provides actionable recommendations through an interactive Streamlit dashboard.

This project is designed as a hackathon-ready prototype focused on sustainability, smart cities, and intelligent decision-making.

🚀 Features

 Real-time environmental dashboard (Streamlit)

 Simulated sensor data (AQI, soil, water, temperature)

Automated risk detection

AI-based future risk prediction

Smart recommendation engine

 Sustainability impact estimation

🗂 Project Structure
EcoSphere-AI/
│── app.py            # Streamlit dashboard
│── simulator.py      # Environmental data simulation
│── analyzer.py       # Risk analysis logic
│── predictor.py      # AI-based prediction module
│── recommender.py    # Actionable recommendations
│── requirements.txt
│── README.md

🧠 How It Works
1. Data Simulation

Generates synthetic environmental data for multiple zones:

Soil moisture

Water level

Air Quality Index (AQI)

Temperature

2. Risk Analysis

Identifies environmental issues such as:

Dry soil

High air pollution

Low water levels

3. AI Prediction

Uses Linear Regression to forecast future risk trends based on historical values.

4. Recommendation Engine

Transforms detected risks into human-readable corrective actions.

5. Dashboard UI

Displays metrics, alerts, insights, and sustainability impact using Streamlit.

▶ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/EcoSphere-AI.git
cd EcoSphere-AI

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
streamlit run app.py

📦 Requirements

Python 3.8+

streamlit

pandas

numpy

scikit-learn

🌍 Use Cases

Smart city monitoring

Precision agriculture

Campus sustainability systems

Environmental risk analysis

Hackathons & AI demos

🏆 Hackathon Value

AI-driven insights (not just visualization)

Modular and scalable architecture

Real-world sustainability relevance

Easy to extend with IoT or live data

🔮 Future Enhancements

IoT sensor integration

Advanced ML models (LSTM, anomaly detection)

Cloud deployment (AWS / GCP)

Alert notifications (Email / SMS)

Enhanced visual analytics

👨‍💻 Author

Rishav Sinha
Computer Science Undergraduate
Interests: AI, Sustainability, Software Engineering
