import json, pip._vendor.requests
import requests
import pprint

print("Welcome to Weather Lookup!\n")


def main():
    print("Search for weather conditions in your chosen location by entering the name of a place below...")

    # user input
    location = input("Location: ")

    print("\n")

    # location details api
    location_api_url = f"http://api.weatherapi.com/v1/current.json?key=ad894ffcc3824845a36215103241401&q={location}"

    # forecast details api
    forecast_api_url = f"http://api.weatherapi.com/v1/forecast.json?key=ad894ffcc3824845a36215103241401&q={location}&days=1"

    a = requests.get(location_api_url)
    locationData = a.json()

    p = requests.get(forecast_api_url)
    forecastData = p.json()

    if a.status_code == 200:

        print("It is", locationData['current']['condition']['text'], "as of", locationData['current']['last_updated'])

        print("\n")

        more = input(f"\nAre you interested in knowing more on {location}'s forecast? (y or n): ")
        print("\n")

        if more == "y":

            print(f"\nHere's what the weather forecast for {location} is looking like tomorrow:")
            print("It will be",
                  str(forecastData["forecast"]["forecastday"][0]["day"]["condition"]["text"]),
                  "with a high of",
                  str(forecastData["forecast"]["forecastday"][0]["day"]["maxtemp_c"]),"C",
                  "and a low of",
                  str(forecastData["forecast"]["forecastday"][0]["day"]["mintemp_c"]),"C")


            #print("It will be", str(forecastData['forecast']['forecastday']['day']['condition']['text']
             #     , "with a high of", str(forecastData['forecast']['forecastday']['day']['maxtemp_c']
              #    , "and a low of", str(forecastData['forecast']['forecastday']['day']['mintemp_c']))))
            #code doesn't work. not sure why, will re-write code above in different way and pray for the best


            print("\n")
            again()
        else:
            again()
    else:
        print("Oops! We can't find any forecast data for the location", location, "." "Please try again...\n")
        main()


def again():
    again = input("\nWould you like to search the WeatherAPI again? (y or n): ")
    print("\n")
    if again == "y":
        main()
    else:
        end()


def end():
    input("\nPress any key to close...")
    exit()


main()