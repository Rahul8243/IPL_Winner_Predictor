import streamlit as st
import pickle
import pandas as pd
import numpy as np
import base64
import os
from datetime import datetime

# ADD BACKGROUND IMAGE
def add_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(
                rgba(0,0,0,0.55),
                rgba(0,0,0,0.55)
            ),
            url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
        }}

        .title-text {{
            font-size: 42px;
            font-weight: 900;
            text-align: center;
            background: linear-gradient(90deg, #0a4abf, #ff9933);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-top: 40px;
        }}

        .credits {{
            position: fixed;
            bottom: 15px;
            left: 20px;
            color: #E8D28D;
            font-size: 15px;
            font-weight: 600;
            opacity: 0.85;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg("background_images/background.jpg")

# TEAMS & CITIES
teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals'
]

cities = [
    'Hyderabad','Bangalore','Mumbai','Indore','Kolkata','Delhi',
    'Chandigarh','Jaipur','Chennai','Cape Town','Port Elizabeth',
    'Durban','Centurion','East London','Johannesburg','Kimberley',
    'Bloemfontein','Ahmedabad','Cuttack','Nagpur','Dharamsala',
    'Visakhapatnam','Pune','Raipur','Ranchi','Abu Dhabi',
    'Sharjah','Mohali','Bengaluru'
]

# LOAD MODEL
pipe = pickle.load(open(
    r'C:\Users\The Rahul\OneDrive\Desktop\IPL_winner_prediction\notebooks\pipe.pkl',
    'rb'
))

# TITLE
st.markdown("<h1 class='title-text'>🏆 IPL WINNER PREDICTOR 🏏</h1>", unsafe_allow_html=True)
st.write("")

# INPUT UI
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select Batting Team", teams)

with col2:
    bowling_team = st.selectbox("Select Bowling Team", [t for t in teams if t != batting_team])

city = st.selectbox("Select Host City", sorted(cities))
target = st.number_input("Target", min_value=0)

col3, col4, col5 = st.columns(3)
with col3: current_score = st.number_input("Current Score", min_value=0)
with col4: overs = st.number_input("Overs Completed", min_value=0.0, max_value=20.0)
with col5: wickets_fallen = st.number_input("Wickets Fallen", min_value=0, max_value=10)

# PREDICTION
if st.button("Predict Probability"):

    runs_left = target - current_score
    balls_left = 120 - int(overs * 6)
    wickets = 10 - wickets_fallen

    crr = current_score / overs if overs > 0 else 0
    rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [city],
        'target': [target],
        'runs_left': [runs_left],
        'current_score': [current_score],
        'balls_left': [balls_left],
        'wickets': [wickets],
        'crr': [crr],
        'rrr': [rrr]
    })

    result = pipe.predict_proba(input_df)
    loss = result[0][0] * 100
    win = result[0][1] * 100

    # Add professional probability cards
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(90deg, rgba(0,255,0,0.08), rgba(0,255,0,0.15));
            border-left: 6px solid #00FF7F;
            padding: 20px;
            border-radius: 14px;
            margin-top: 25px;
            text-align: center;
            backdrop-filter: blur(6px);
            box-shadow: 0 2px 12px rgba(0,0,0,0.4);
        ">
            <span style="font-size:28px; font-weight:800; color:#00FF7F;">
                🟢 WIN Probability: {win:.2f}%
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(90deg, rgba(255,0,0,0.08), rgba(255,0,0,0.15));
            border-left: 6px solid #FF4B4B;
            padding: 20px;
            border-radius: 14px;
            margin-top: 18px;
            text-align: center;
            backdrop-filter: blur(6px);
            box-shadow: 0 2px 12px rgba(0,0,0,0.4);
        ">
            <span style="font-size:28px; font-weight:800; color:#FF4B4B;">
                🔴 LOSE Probability: {loss:.2f}%
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Add columns
    input_df["wins_prob"] = round(win, 2)
    input_df["lose_prob"] = round(loss, 2)

    # Table Header
    st.markdown(
        """
        <h2 style='color:white; font-weight:800; margin-top:30px;'>
            📊 Match Situation Details
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.dataframe(input_df)

    # SAVE HISTORY TO CSV
    history_folder = "history"
    os.makedirs(history_folder, exist_ok=True)

    history_file = os.path.join(history_folder, "prediction_history.csv")

    history_row = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "batting_team": batting_team,
        "bowling_team": bowling_team,
        "city": city,
        "target": target,
        "runs_left": runs_left,
        "current_score": current_score,
        "balls_left": balls_left,
        "wickets": wickets,
        "crr": round(crr, 2),
        "rrr": round(rrr, 2),
        "win_probability": round(win, 2),
        "lose_probability": round(loss, 2)
    }

    df_row = pd.DataFrame([history_row])

    if os.path.exists(history_file):
        df_row.to_csv(history_file, mode='a', header=False, index=False)
    else:
        df_row.to_csv(history_file, index=False)

# CREDITS SECTION

st.markdown("""
<div class='credits'>
<b>Developed By:</b><br>
Rahul Kumar<br>
</div>
""", unsafe_allow_html=True)
