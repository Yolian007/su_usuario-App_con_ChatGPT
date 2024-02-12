import streamlit as st

# Funciones de conversión de temperatura
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Funciones de conversión de longitud
def feet_to_meters(feet):
    return feet * 0.3048

def meters_to_feet(meters):
    return meters / 0.3048

def inches_to_centimeters(inches):
    return inches * 2.54

def centimeters_to_inches(centimeters):
    return centimeters / 2.54

# Funciones de conversión de peso/masa
def pounds_to_kilograms(pounds):
    return pounds * 0.453592

def kilograms_to_pounds(kilograms):
    return kilograms / 0.453592

def ounces_to_grams(ounces):
    return ounces * 28.3495

def grams_to_ounces(grams):
    return grams / 28.3495

# Funciones de conversión de volumen
def gallons_to_liters(gallons):
    return gallons * 3.78541

def liters_to_gallons(liters):
    return liters / 3.78541

def cubic_inches_to_cubic_centimeters(cubic_inches):
    return cubic_inches * 16.3871

def cubic_centimeters_to_cubic_inches(cubic_centimeters):
    return cubic_centimeters / 16.3871

# Funciones de conversión de tiempo
def hours_to_minutes(hours):
    return hours * 60

def minutes_to_seconds(minutes):
    return minutes * 60

def days_to_hours(days):
    return days * 24

def weeks_to_days(weeks):
    return weeks * 7

# Funciones de conversión de velocidad
def mph_to_kph(mph):
    return mph * 1.60934

def kph_to_mps(kph):
    return kph * 0.277778

def knots_to_mph(knots):
    return knots * 1.15078

def mps_to_fps(mps):
    return mps * 3.28084

# Funciones de conversión de área
def sq_meters_to_sq_feet(sq_meters):
    return sq_meters * 10.7639

def sq_feet_to_sq_meters(sq_feet):
    return sq_feet / 10.7639

def sq_kilometers_to_sq_miles(sq_kilometers):
    return sq_kilometers * 0.386102

def sq_miles_to_sq_kilometers(sq_miles):
    return sq_miles / 0.386102

# Funciones de conversión de energía
def joules_to_calories(joules):
    return joules * 0.239006

def calories_to_kilojoules(calories):
    return calories * 4.184

def kw_hour_to_megajoules(kw_hour):
    return kw_hour * 3.6

def megajoules_to_kw_hour(megajoules):
    return megajoules / 3.6

# Funciones de conversión de presión
def pascals_to_atmospheres(pascals):
    return pascals * 9.86923e-6

def atmospheres_to_pascals(atmospheres):
    return atmospheres * 101325

def bars_to_psi(bars):
    return bars * 14.5038

def psi_to_bars(psi):
    return psi / 14.5038

# Funciones de conversión de tamaño de datos
def megabytes_to_gigabytes(megabytes):
    return megabytes / 1024

def gigabytes_to_terabytes(gigabytes):
    return gigabytes / 1024

def kilobytes_to_megabytes(kilobytes):
    return kilobytes / 1024

def terabytes_to_petabytes(terabytes):
    return terabytes / 1024

# Selección de categoría y tipo de conversión
categoria = st.selectbox("Selecciona una categoría:", ["Temperatura", "Longitud", "Peso/Masa", "Volumen", "Tiempo", "Velocidad", "Área", "Energía", "Presión", "Tamaño de datos"])

if categoria == "Temperatura":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:", ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"])
    valor = st.number_input("Ingresa el valor a convertir:")

    if tipo_conversion == "Celsius a Fahrenheit":
        resultado = celsius_to_fahrenheit(valor)
    elif tipo_conversion == "Fahrenheit a Celsius":
        resultado = fahrenheit_to_celsius(valor)
    elif tipo_conversion == "Celsius a Kelvin":
        resultado = celsius_to_kelvin(valor)
    elif tipo_conversion == "Kelvin a Celsius":
        resultado = kelvin_to_celsius(valor)

elif categoria == "Longitud":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:", ["Pies a Metros", "Metros a Pies", "Pulgadas a Centímetros", "Centímetros a Pulgadas"])
    valor = st.number_input("Ingresa el valor a convertir:")

    if tipo_conversion == "Pies a Metros":
        resultado = feet_to_meters(valor)
    elif tipo_conversion == "Metros a Pies":
        resultado = meters_to_feet(valor)
    elif tipo_conversion == "Pulgadas a Centímetros":
        resultado = inches_to_centimeters(valor)
    elif tipo_conversion == "Centímetros a Pulgadas":
        resultado = centimeters_to_inches(valor)

# Aquí se incluyen las demás opciones de conversión para las categorías restantes, siguiendo el mismo patrón que las anteriores

# Mostrar resultado
st.write(f"El resultado de la conversión es: {resultado}")
