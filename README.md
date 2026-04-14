<h1 align="center">🏏IPL Winner Predictor </h1>

<p align="center">
  <img src="https://img.shields.io/badge/Machine%20Learning-Model-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge"/>
</p>

<p align="center">
  ⚡ Real-time IPL match prediction powered by Machine Learning
</p>

---

<h2 align="center">📌 Project Overview</h2>

The **IPL Winner Predictor** is a machine learning–powered system that estimates the **real-time winning probability** of an IPL match during the second innings.

It dynamically adapts to match conditions using:

- Batting Team  
- Bowling Team  
- City (Venue)  
- Target Score  
- Current Score  
- Overs Completed  
- Wickets Fallen  

### 🎯 Output

✔ Win Probability (%)  
✔ Lose Probability (%)  
✔ Over-wise Match Progression Curve  

> Designed to simulate real-time cricket analytics similar to Cricbuzz.

---

<h2 align="center">🧠 Key Highlights</h2>

### ⚡ Real-Time Prediction Engine
Predicts match outcomes dynamically at any stage of the chase.

### 📊 Advanced Feature Engineering
Includes powerful cricket features:

- Runs Left  
- Balls Left  
- Required Run Rate (RRR)  
- Current Run Rate (CRR)  
- Wickets Remaining  
- Match Target  

### 🤖 Machine Learning Pipeline
- Logistic Regression (fast & interpretable)  
- OneHotEncoding (teams & city)  
- Robust preprocessing pipeline  
- Generalizes across IPL seasons  

### 🌐 Streamlit Web Application
- Interactive UI  
- Real-time input-based prediction  
- Match progression visualization  
- Clean and intuitive dashboard  

---
<h2 align="center">🏗️ Project Architecture</h2>

```
📦 IPL_Winner_Predictor
 ┣ 📁 data
 ┣ 📁 notebooks
 ┃ ┣ 📄 ipl_winner_predictor.ipynb
 ┃ ┗ 📄 pipe.pkl
 ┣ 📄 app.py
 ┣ 📄 requirements.txt
 ┗ 📄 README.md
```
---

<h2 align="center">⚙️ How It Works</h2>

### 🔹 Data Preprocessing
- Standardized team names  
- Removed D/L affected matches  
- Filtered second innings for prediction  
- Handled missing and inconsistent data  

---

### 🔹 Feature Engineering

```python
runs_left = target - current_score
balls_left = 120 - balls_bowled
crr = current_score / overs_completed
rrr = (runs_left * 6) / balls_left
wickets_left = 10 - wickets_fallen


### 🔹 Model Training
- Train/Test Split (80/20)  
- Logistic Regression Pipeline  
- OneHotEncoding for categorical variables  
- Evaluated using accuracy & probability outputs  

### 🔹 Deployment
- Built using Streamlit  
- Real-time prediction interface  
- Interactive probability visualization  


## 🚀 Run Locally

# Clone the repo
git clone https://github.com/Rahul8243/IPL_Winner_Predictor.git

cd IPL_Winner_Predictor

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

<h2 align="center">🌐 Live Demo</h2>

> ⚡ Experience real-time IPL match prediction powered by Machine Learning

<p align="center">
  <a href="https://ipl-winner-predictor-the-rahul.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/🚀 Launch Live App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  </a>
</p>


## 📊 Results
<p>
  ✔ Accurate win probability prediction  
✔ Real-time match progression tracking  
✔ Works across IPL seasons & teams  
✔ Lightweight and fast model
</p>

## 🔮Future Enhancements

- XGBoost / Deep Learning models  
- Player-level features (batsman vs bowler)  
- Live API integration (Cricbuzz / ESPN)  
- First innings score prediction  
- Model explainability (SHAP)  


## 🧠 Key Learnings

- Feature engineering in sports analytics  
- Handling real-world noisy datasets  
- Building interpretable ML pipelines  
- Deploying ML models with Streamlit  

<h2 align="center">👨‍💻 Author</h2>

<div align="center">
**Rahul Kumar**

</div>


<h2 align="center">⭐ Support</h2>

If you found this project helpful, consider giving it a ⭐

<h2 align="center">🏁 Conclusion</h2>

This project demonstrates how **machine learning + cricket analytics** can be combined to build a **real-time predictive system**.

It serves as a strong foundation for advanced sports analytics, live prediction systems, and AI-powered dashboards.
