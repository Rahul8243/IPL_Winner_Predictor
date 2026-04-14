# 🏏 IPL Winner Predictor

<p align="center">
<img src="https://img.shields.io/badge/Machine%20Learning-Model-blue?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Streamlit-App-green?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge"/>
</p>

---

## 📌 Project Overview

The **IPL Winner Predictor** is a machine learning–powered system that estimates the **real-time winning probability** of an IPL match during the second innings.

It dynamically adapts to match conditions using inputs such as:

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

> Built to simulate real-time cricket analytics similar to platforms like Cricbuzz.

---

## 🧠 Key Highlights

### ⚡ Real-Time Prediction Engine
Predicts match outcomes dynamically at any stage of the chase.

### 📊 Advanced Feature Engineering
Derived powerful cricket features:

- Runs Left  
- Balls Left  
- Required Run Rate (RRR)  
- Current Run Rate (CRR)  
- Wickets Remaining  
- Match Target  

### 🤖 Machine Learning Pipeline
- Logistic Regression (interpretable & fast)  
- OneHotEncoding (teams & city)  
- Robust preprocessing pipeline  
- Generalizes across multiple IPL seasons  

### 🌐 Streamlit Web Application
- Interactive UI  
- Real-time input-based prediction  
- Match progression visualization  
- Clean dashboard experience  

---

## 🏗️ Project Architecture
📦 IPL_Winner_Predictor
┣ 📁 data
┣ 📁 notebooks
┃ ┗ 📄 ipl_winner_predictor.ipynb
┃ ┗ 📄 pipe.pkl
┣ 📄 app.py
┣ 📄 requirements.txt
┣ 📄 README.md


---

## ⚙️ How It Works

### 🔹 Data Preprocessing
- Standardized team names  
- Removed D/L affected matches  
- Filtered second innings for chase modeling  
- Handled missing & inconsistent data  

---

### 🔹 Feature Engineering

```python
runs_left = target - current_score
balls_left = 120 - balls_bowled
crr = current_score / overs_completed
rrr = (runs_left * 6) / balls_left
wickets_left = 10 - wickets_fallen

# Clone the repo
git clone https://github.com/Rahul8243/IPL_Winner_Predictor.git

cd IPL_Winner_Predictor

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py


## 🌐 Live Demo

🚀 Try the live application:

<p align="center">
  <a href="https://ipl-winner-predictor-the-rahul.streamlit.app/">
    <img src="https://img.shields.io/badge/Streamlit-Live_App-success?style=for-the-badge&logo=streamlit">
  </a>
</p>

🔗 Direct Link:  
https://ipl-winner-predictor-the-rahul.streamlit.app/
