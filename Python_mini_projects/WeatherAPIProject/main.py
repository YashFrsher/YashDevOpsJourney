# -------- Challenge: Real-Time Weather Logger (API + CSV) --------------

import os
import csv
import requests
import datetime
import pandas as pd
from requests.exceptions import HTTPError
from tabulate import tabulate
from statistics import mode
from dotenv import load_dotenv

# Improting Environment Variable
load_dotenv()

# Data Ingestion and API Call.

def getData():
    city = input("Enter Your City Name: ").lower().strip()
    key = os.getenv("API_KEY")
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

    try:
        response = requests.get(api)  # Sending a GET request to the API and authenticating using api key.
        if response.status_code == 404:
            print("Invalid City Name. Please Try Again...")
            return
        response.raise_for_status()
    except HTTPError as http_err:
        print("HTTP Error Occured:", http_err)
    except Exception as e:
        print("Other Errors Occured: ", e)
    else:
        json_content = response.json()
        return json_content

def fileCheck():
    filename = "citytemp.csv"
    if os.path.exists(filename):
        pass
    else:
        try:
            df = pd.DataFrame()
            df.to_csv(filename, index=False)
        except Exception as e:
            print(f"Error has occurred: {e}")
        else:
            # print(f"{filename} is created successfully...")
            headers = ["Date", "CityName", "Temperature(in Celcius)", "WeatherCondition"]
            df = pd.read_csv(filename,header=None, names=headers)
            df.to_csv(filename,index=False)
    return filename

def addData():
    content = getData()
    if content is None:
        print("Invalid City Name Entry. Code Exiting")
        return
    file = fileCheck()
    currentDate = datetime.datetime.now().date().strftime("%Y-%m-%d")
    cityName = content["name"] 
    currentTemp = f"{round(content["main"]["temp"] - 272.15, 2)}"
    currentCondition = content["weather"][0]["main"]
    
    df = pd.read_csv(fileCheck(),usecols=["CityName","Date"])
    if ((df["CityName"] == cityName) & (df["Date"] == currentDate)).any():
        print("Duplicate Entry For city on the same date...")
        return

    append_data = pd.DataFrame([[currentDate, cityName, currentTemp, currentCondition]])
    append_data.to_csv(file, mode="a", index=False, header=False)
    print("Data Added...")

def viewData():
    with open(fileCheck(),"r",newline="",encoding="utf-8") as tracker:
        reader = csv.reader(tracker)
        print(tabulate(reader, headers="firstrow", tablefmt="pipe"))

def viewStats():
    df = pd.read_csv(fileCheck(),usecols=["Temperature(in Celcius)","WeatherCondition"])
    temp = df["Temperature(in Celcius)"].to_list()
    condition = df["WeatherCondition"].to_list()
    averageTemp = round(sum(temp) / len(temp),2)
    maxTemp = max(temp)
    minTemp = min(temp)
    commonCondition = mode(condition)
        
    stats = [
        ["Max Temperature",maxTemp],
        ["Min Temperature",minTemp],
        ["Average Temperature",averageTemp],
        ["Common Weather Condition",commonCondition]
    ]
    
    headers = ["Stats Name","Stats Value"]
    print(tabulate(stats,headers=headers))


# CLI Menu
def menu():
    fileCheck()
    while True:
        print("===== Welcome To Live Weather APP =====")
        print("1. Add Weather Data")
        print("2. View Weather Data")
        print("3. View Weather Data statistics")
        print("4. Exit Menu")
        
        try:
            choice = int(input("Choose your operation: "))
        except ValueError:
            print("Choice Values should be integer. Try Again...")
        else:
            if choice == 1:
                addData()
            elif choice == 2:
                viewData()
            elif choice == 3:
                viewStats()
            elif choice == 4:
                print("Exiting Menu...")
                break
            else:
                print("Invalid Entry.. Try Again!!!")

menu()