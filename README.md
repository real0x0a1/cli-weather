# **Weather CLI**
================

A simple command-line interface to get the current weather for a given city or postal code.

## **Usage**

```
python weather.py <city> [-f | -c]
```

## **Options**

* `<city>`: City name or postal code
* `-f`, `--fahrenheit`: Use Fahrenheit units
* `-c`, `--celsius`: Use Celsius units (default)

**Example**

```
python main.py New York -f
```

## **Features**

* Get current weather for a given city or postal code
* Supports both Fahrenheit and Celsius units
* Displays weather condition, temperature, and humidity
* Uses ASCII art to display weather icons

## **Requirements**

* Python 3.x
* `requests` library (install with `pip install requests`)
* OpenWeatherMap API key (sign up for a free account at [openweathermap.org](https://openweathermap.org/))

## **Author**

- Ali (Real0x0a1)

---