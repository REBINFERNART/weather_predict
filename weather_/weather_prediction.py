









import streamlit as st
import requests
import pickle
import pandas as pd
import numpy as np


API_KEY = "1659cf5477bd0a121c844691d4bd9e81"

def load_trained_model(model_path=r"C:\Users\krebi\Downloads\weathercard.pkl"):
    """Load pre-trained model from pickle file"""
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def fetch_weather_data(city):
    """Fetch weather data from OpenWeatherMap API"""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        
        if response.status_code == 404 or 'main' not in data:
            st.error("City not found. Please check the spelling of the city name.")
            return None

        return {
            'temp': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'pressure': data['main']['pressure'],
            'cloud_cover': data['clouds']['all'],
            'description': data['weather'][0]['description']
        }
    except Exception as e:
        st.error(f"Error fetching weather data: {e}")
        return None

def display_creative_output(city, model_output):
    """Display a creative output based on model prediction"""
    st.markdown("""<style>body {background-color: #DFF6FF; color: #000080;}</style>""", unsafe_allow_html=True)

    st.write("### Rain Prediction Result")
    
    if model_output == 1:
        
        st.markdown(f"### 🌧️ Heavy Rain  in {city}!")
        
        
        st.markdown("""
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="300" height="200">
            <rect width="300" height="200" fill="#87CEEB" />
            <path d="M50 100 Q100 50, 150 100 T250 100" fill="none" stroke="#4682B4" stroke-width="10" />
            <circle cx="100" cy="150" r="10" fill="#1E90FF">
                <animate attributeName="cy" values="150;180;150" dur="1.5s" repeatCount="indefinite" />
            </circle>
            <circle cx="150" cy="170" r="8" fill="#4169E1">
                <animate attributeName="cy" values="170;200;170" dur="1.7s" repeatCount="indefinite" />
            </circle>
            <circle cx="200" cy="160" r="12" fill="#00BFFF">
                <animate attributeName="cy" values="160;190;160" dur="1.6s" repeatCount="indefinite" />
            </circle>
        </svg>
        """, unsafe_allow_html=True)
        
        
        st.write("### 🌂 Rain Advisory")
        st.markdown("""
        ⚠️ **Prepare for Heavy Rain:**
        - Carry an umbrella or raincoat
        - Avoid waterlogged areas
        - Check local weather alerts
        - Keep electronic devices protected
        - Plan for potential travel delays
        """)
        
        
        st.markdown("""
        <div style="background-color: #FF6347; color: white; padding: 10px; text-align: center; 
                    animation: pulse 1.5s infinite; border-radius: 10px;">
            <strong>⚡ HEAVY RAIN WARNING ⚡</strong>
        </div>
        <style>
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        
        st.markdown(f"### ☀️ No Rain  in {city}.")
        
       
        st.markdown("""
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="300" height="200">
            <rect width="300" height="200" fill="#87CEEB" />
            <circle cx="150" cy="100" r="50" fill="#FFD700" />
            <line x1="150" y1="30" x2="150" y2="50" stroke="#FFD700" stroke-width="4" />
            <line x1="150" y1="150" x2="150" y2="170" stroke="#FFD700" stroke-width="4" />
            <line x1="80" y1="100" x2="100" y2="100" stroke="#FFD700" stroke-width="4" />
            <line x1="200" y1="100" x2="220" y2="100" stroke="#FFD700" stroke-width="4" />
            <line x1="105" y1="60" x2="120" y2="75" stroke="#FFD700" stroke-width="4" />
            <line x1="180" y1="125" x2="195" y2="140" stroke="#FFD700" stroke-width="4" />
            <line x1="105" y1="140" x2="120" y2="125" stroke="#FFD700" stroke-width="4" />
            <line x1="180" y1="75" x2="195" y2="60" stroke="#FFD700" stroke-width="4" />
        </svg>
        """, unsafe_allow_html=True)

def main():
    
    st.set_page_config(page_title="Rain Prediction App", page_icon="🌧️")
    st.title("🌦️  Rain Predictor 🌦️")
    
    
    model = load_trained_model()
    
    if model is None:
        st.error("Failed to load the model. Please check the model file path.")
        return
    
    
    city = st.text_input("Enter City Name", "chennai")
    
    if st.button("Predict Rain"):
        
        weather_data = fetch_weather_data(city)
        
        if weather_data:
            
            input_data = pd.DataFrame([
                [weather_data['temp'], weather_data['humidity'], 
                 weather_data['wind_speed'], weather_data['cloud_cover'], 
                 weather_data['pressure']]
            ], columns=['Temperature', 'Humidity', 'Wind_Speed', 'Cloud_Cover', 'Pressure'])
            
            
            model_output = model.predict(input_data)[0]
            
            
            display_creative_output(city, model_output)

if __name__ == "__main__":
    main()

