# 🌦️ Real-Time Weather Logger (API + CSV)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![API](https://img.shields.io/badge/API-OpenWeatherMap-orange) ![CLI
Tool](https://img.shields.io/badge/Tool-CLI-green)
![Status](https://img.shields.io/badge/Project-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

A **Python CLI application** that fetches **real-time weather data**
from the **OpenWeatherMap API** and logs it into a CSV file for daily
tracking.

This project demonstrates **API integration, data logging, CLI
development, and basic analytics** --- common patterns used in **DevOps
automation scripts**.

------------------------------------------------------------------------

# 📌 Features

✅ Fetch **real-time weather data** using an API\
✅ Store weather logs in a **CSV file**\
✅ Prevent **duplicate entries for the same city on the same day**\
✅ View stored weather logs in a **formatted table**\
✅ Generate **weather statistics**:

-   📊 Average temperature
-   🔥 Highest temperature
-   ❄️ Lowest temperature
-   🌥️ Most frequent weather condition

------------------------------------------------------------------------

# 🛠️ Tech Stack

  Technology              Usage
  ----------------------- ---------------------------
  🐍 Python               Core programming language
  🌐 OpenWeatherMap API   Weather data source
  📊 Pandas               Data processing
  📄 CSV                  Data storage
  🖥️ CLI                  User interaction
  📦 Tabulate             Table formatting

------------------------------------------------------------------------

# 📂 Project Structure

    WeatherAPIProject/
    │
    ├── weather_logger.py
    ├── citytemp.csv
    ├── requirements.txt
    ├── .gitignore
    └── README.md

------------------------------------------------------------------------

# ⚙️ Installation

### 1️⃣ Clone the repository

``` bash
git clone https://github.com/YOUR_USERNAME/YashDevOpsJourney.git
```

### 2️⃣ Navigate to the project

``` bash
cd YashDevOpsJourney/Python_mini_projects/WeatherAPIProject
```

### 3️⃣ Create a virtual environment

``` bash
python3 -m venv venv
```

Activate it:

**Linux / Mac**

``` bash
source venv/bin/activate
```

**Windows**

``` bash
venv\Scripts\activate
```

### 4️⃣ Install dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

# 🔑 Setup API Key

Create an account and generate an API key:

https://openweathermap.org/api

Add the API key inside your script:

``` python
key = "YOUR_API_KEY"
```

⚠️ Never commit your API key to GitHub.

------------------------------------------------------------------------

# ▶️ Running the Application

Run the CLI tool:

``` bash
python weather_logger.py
```

You will see the menu:

    ===== Welcome To Live Weather APP =====

    1. Add Weather Data
    2. View Weather Data
    3. View Weather Data statistics
    4. Exit Menu

------------------------------------------------------------------------

# 📊 Example Output

### Weather Log Table

    | Date       | CityName  | Temperature(in Celcius) | WeatherCondition |
    |------------|-----------|-------------------------|------------------|
    | 2026-03-16 | Delhi     | 34.5                    | Clouds           |
    | 2026-03-16 | Mumbai    | 28.7                    | Clouds           |

### Weather Statistics

    Stats Name                Stats Value
    -------------------------------------
    Max Temperature           39.84
    Min Temperature           28.72
    Average Temperature       34.1
    Common Weather Condition  Clouds

------------------------------------------------------------------------

# 🚀 DevOps Concepts Demonstrated

  Concept           Example
  ----------------- --------------------------
  API Integration   Fetch weather data
  Data Logging      CSV file storage
  Error Handling    API response validation
  CLI Tools         Terminal-based interface
  Data Analytics    Temperature statistics
