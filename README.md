# Weather Application

A simple weather application built with a React frontend and Django backend. The frontend allows users to search for cities and view current weather and forecast data using data from the OpenWeatherMap API. The backend uses Django to provide two API endpoints: one for geolocation using the GeoDB Cities API and one for weather data using the OpenWeatherMap API.

Features
City Search: Search for cities with a population greater than 1 million.
Current Weather: View current weather details for the selected city.
Forecast: Get a 5-day weather forecast for the selected city.
Technologies Used
Frontend: React.js
Backend: Django, Django REST Framework
APIs: OpenWeatherMap API, GeoDB Cities API
Installation
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/react-weather-app.git
cd react-weather-app
2. Setting up the Backend (Django)
bash
Copy code
cd weather_backend

# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the backend server
python manage.py runserver
3. Setting up the Frontend (React)
bash
Copy code
cd ../src

# Install dependencies
npm install

# Start the frontend server
npm start
4. Access the Application
The React frontend will be available at http://localhost:3000.
The Django backend will be available at http://127.0.0.1:8000.
API Endpoints
1. Geolocation API
Endpoint: /api/geo/
Method: GET
Query Parameters:
namePrefix - The city name prefix to search for.
2. Weather Data API
Endpoint: /api/weather/
Method: GET
Query Parameters:
lat - Latitude of the city.
lon - Longitude of the city.
Deployment
Backend (Django) on Heroku
Follow the instructions in the Heroku Deployment section to deploy your Django backend to Heroku.
Ensure your CORS settings allow your frontend domain.
Frontend (React) on Netlify
Follow the instructions in the Netlify Deployment section to deploy your React app.
Update API URLs
Update the API URLs in the src/api.js file to point to your deployed backend.

Contributing
Feel free to open issues or create pull requests to improve this project.

License
This project is licensed under the MIT License - see the LICENSE file for details.

