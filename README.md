📌 Project Overview

The IPL Winner Predictor is a machine-learning–powered system that predicts the real-time winning probability of an IPL match based on the current match situation.

It takes dynamic inputs such as:

Batting team

Bowling team

Host city

Target score

Current score

Overs completed

Wickets fallen

Using these features, it computes:
✔ Win Probability
✔ Lose Probability
✔ Match Progression Curve (Over-wise prediction swing)

The final model is deployed using Streamlit, offering an intuitive and interactive UI.

🧠 Key Features
🔹 Real-Time Win Prediction

Predicts match outcomes dynamically during any point of the chase.

🔹 Accurate Feature Engineering

Includes essential cricket features such as:

Runs Left

Balls Left

Required Run Rate (RRR)

Current Run Rate (CRR)

Wickets Left

Match Target (1st innings total + 1)

🔹 Clean Machine Learning Pipeline

Model used:

Logistic Regression with OneHotEncoder

Fully scalable & interpretable model

Generalizes well across seasons

🔹 Professional Streamlit Web App

Modern UI/UX

Match history tracking

Slide-based match progression

Visual probability indicators

📂 Project Structure
📦 IPL_Winner_Predictor
 ┣ 📁 data
 ┣ 📁 notebooks
 ┃ ┗ 📄 ipl_winner_predictor.ipynb
 ┃ ┗ 📄 pipe.pkl
 ┣ 📄 app.py
 ┣ 📄 requirements.txt
 ┣ 📄 README.md   ← (This file)

🛠 Technologies Used
Category	Tools
Programming Language	Python
ML Libraries	pandas, numpy, scikit-learn
Visualization	matplotlib, seaborn
Deployment	Streamlit
Development	VS Code / Google Colab
🔧 How it Works
✔ Step 1: Data Cleaning

Fix team name inconsistencies (Delhi Daredevils → Delhi Capitals)

Remove D/L method matches

Keep only second-innings deliveries

✔ Step 2: Feature Engineering

Generated features:

runs_left = target - current_score
balls_left = 120 - balls_bowled
crr = current_score / overs_completed
rrr = (runs_left * 6) / balls_left
wickets_left = 10 - wickets_fallen

✔ Step 3: Model Training

OneHotEncoder for team + city

Logistic Regression pipeline

Train/test split → 80/20

✔ Step 4: Deployment

Built with Streamlit

Probability shown with dynamic colored cards

Match history saved automatically

🚀 How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/Rahul8243/IPL_Winner_Predictor.git
cd IPL_Winner_Predictor

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py

📸 Screenshots

(Add the images you shared in this section
– Streamlit UI, Match Situation Table, Probability Display)

📊 Results

✔ Predicts accurate win probabilities
✔ Shows over-wise match progression
✔ Works for all IPL teams and seasons
✔ Stable and interpretable ML model

🔮 Future Scope

Integrate XGBoost / Neural Networks

Add bowler quality, batsman form, pitch type

Live integration using API from Cricbuzz / ESPN

First-innings score prediction model

Add Model Explainability (SHAP)

## 🚀 Live Demo

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live-brightgreen)](https://ipl-winner-predictor-the-rahul.streamlit.app/)


🏁 Conclusion

This project successfully demonstrates how cricket analytics and machine learning can be combined to build a realistic, real-time IPL match prediction system.
The model, UI, and feature engineering make it a complete end-to-end solution suitable for deployment and research.
