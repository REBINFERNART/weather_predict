# Weather Prediction System

A sophisticated weather prediction system that combines real-time weather API data with machine learning to forecast rainfall probability based on multiple meteorological parameters.

## Features

- Real-time weather data retrieval using Weather API
- Machine learning model for rainfall prediction based on:
  - Temperature
  - Humidity
  - Wind Speed
  - Atmospheric Pressure
  - Cloud Cover
- Interactive display of weather predictions and forecasts
- Combined analysis of API data and ML predictions

## Installation

1. Clone the repository:
```bash
git clone https://github.com/REBINFERNART/weather_predict/upload
cd weather-prediction-system
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your API key:
- Create an account at [Weather API Provider]
- Copy your API key
- Create a `.env` file in the project root
- Add your API key: `WEATHER_API_KEY=your_api_key_here`

## Usage

1. Start the application:
```bash
python main.py
```

2. The system will:
   - Fetch current weather data from the API
   - Process meteorological parameters
   - Generate rainfall predictions using the ML model
   - Display combined results

## Project Structure

```
weather-prediction-system/
├── data/
│   ├── training_data.csv
│   └── model_artifacts/
├── models/
│   ├── train_model.py
│   └── predict.py
├── api/
│   └── weather_api.py
├── utils/
│   └── data_processing.py
├── main.py
├── requirements.txt
└── README.md
```

## Model Information

The machine learning model is trained on historical weather data with the following features:
- Temperature (°C)
- Humidity (%)
- Wind Speed (km/h)
- Atmospheric Pressure (hPa)
- Cloud Cover (%)

Target Variable:
- Rainfall Probability (%)

## Requirements

- Python 3.8+
- pandas
- numpy
- scikit-learn
- requests
- python-dotenv
- [Other dependencies]

## API Integration

The system uses [Weather API Provider] to fetch real-time weather data. The API provides:
- Current weather conditions
- Hourly forecasts
- Historical weather data

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Weather data provided by [Weather API Provider]
- Thanks to contributors and data providers
- Inspiration from various weather forecasting systems

## Contact

- Your Name
- krebinfernart@gmail.com
- Project Link: https://github.com/REBINFERNART/weather_predict/upload

## Future Improvements

- Add more weather parameters for prediction
- Implement advanced ML models (e.g., LSTM, XGBoost)
- Develop a web interface
- Add historical data analysis
- Improve prediction accuracy through ensemble methods
