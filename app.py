import streamlit as st

# Conversion functions
def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084,
        "Inches": 39.3701
    }

    if from_unit in conversion_factors and to_unit in conversion_factors:
        return round(value * (conversion_factors[to_unit] / conversion_factors[from_unit]), 4)
    return None

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return round(value, 4)
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return round((value * 9/5) + 32, 4)
    if from_unit == "Fahrenheit" and to_unit == "Celsius":
        return round((value - 32) * 5/9, 4)
    if from_unit == "Celsius" and to_unit == "Kelvin":
        return round(value + 273.15, 4)
    if from_unit == "Kelvin" and to_unit == "Celsius":
        return round(value - 273.15, 4)
    return None

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }

    if from_unit in conversion_factors and to_unit in conversion_factors:
        return round(value * (conversion_factors[to_unit] / conversion_factors[from_unit]), 4)
    return None

# Steamlit UI
st.title("🔄 Unit Converter")

# jDropdown for unit type
unit_type = st.selectbox("📏 Select Unit Type", ["Length", "Temperature", "Weight"])

# Length Conversion
if unit_type == "Length":
    st.subheader("📏 Length Conversion")
    value = st.number_input("🔢 Enter value:")
    from_unit = st.selectbox("🔄 From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
    to_unit = st.selectbox("➡️ To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])

    if st.button("🔄 Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"✅ Converted Value: {result} {to_unit}")

# Temperature Conversion
elif unit_type == "Temperature":
    st.subheader("🌡️ Temperature Conversion")
    value = st.number_input("🔢 Enter value:")
    from_unit = st.selectbox("🔄 From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("➡️ To", ["Celsius", "Fahrenheit", "Kelvin"])

    if st.button("🔄 Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"✅ Converted Value: {result} {to_unit}")

# Weight Conversion
elif unit_type == "Weight":
    st.subheader("⚖️ Weight Conversion")
    value = st.number_input("🔢 Enter value:")
    from_unit = st.selectbox("🔄 From", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("➡️ To", ["Kilograms", "Grams", "Pounds", "Ounces"])

    if st.button("🔄 Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"✅ Converted Value: {result} {to_unit}")








