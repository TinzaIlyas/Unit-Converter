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








# import streamlit as st
# import pandas as pd
# import os
# from io import BytesIO

# # Set up our App
# st.set_page_config(page_title="💿 Data Sweeper")
# st.title("💿Data Sweeper")
# st.write("Transform your files between CSV and Excel formats.")

# uploaded_files = st.file_uploader("Upload your files", accept_multiple_files=True)

# if uploaded_files:
#     for file in uploaded_files:
#         file_ext = os.path.splitext(file.name)[-1].lower()  # Ensure lowercase for comparison

#         if file_ext == ".csv":
#             df = pd.read_csv(file)
#         elif file_ext == ".xlsx":
#             df = pd.read_excel(file)
#         else:
#             st.error(f"Unsupported file type: {file_ext}")
#             continue  # This is fine if inside a loop
# st.write(f"**File Name:** {file.name}")
# st.write(f"**File Size:** {file.size/1024:.2f}KB")

# st.write("###Preview the Head of the DataFrame")
# st.dataframe(df.head())

# st.subheader("Data Cleaning Options")

# if st.checkbox(f"Clean Data for {file.name}"):
#      col1, col2 = st.columns(2)



# with col1:
#      if st.button(f"Remove Duplicates from {file.name}"):
#           df.drop_duplicates(inplace=True)
#           st.success("Duplicates Removed!")


# with col2:
#      if st.button(f"Fill Missing Value for {file.name}"):
#           numeric_cols= df.select_dtypes(include=['numbers']).columns
# df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
# st.success("Missing Values have been Filled!")

# import streamlit as st
# import pandas as pd
# import os
# from io import BytesIO

# # Set up our App
# st.set_page_config(page_title="💿 Data Sweeper")
# st.title("💿 Data Sweeper")
# st.write("Transform your files between CSV and Excel formats.")

# uploaded_files = st.file_uploader("Upload your files", accept_multiple_files=True)

# if uploaded_files:
#     for file in uploaded_files:
#         file_ext = os.path.splitext(file.name)[-1].lower()  # Ensure lowercase for comparison
#         df = None  # Initialize df to avoid 'not defined' error

#         if file_ext == ".csv":
#             df = pd.read_csv(file)
#         elif file_ext == ".xlsx":
#             df = pd.read_excel(file)
#         else:
#             st.error(f"Unsupported file type: {file_ext}")
#             continue  # Skip this file if unsupported

#         # ✅ Check if df exists before using it
#         if df is not None:
#             st.write(f"**File Name:** {file.name}")
#             st.write(f"**File Size:** {file.size / 1024:.2f} KB")

#             st.write("### Preview the Head of the DataFrame")
#             st.dataframe(df.head())

#             st.subheader("Data Cleaning Options")

#             # ✅ Unique checkbox for each file
#             if st.checkbox(f"Clean Data for {file.name}"):
#                 col1, col2 = st.columns(2)

#                 with col1:
#                     if st.button(f"Remove Duplicates from {file.name}"):
#                         df.drop_duplicates(inplace=True)
#                         st.success("Duplicates Removed!")

#                 with col2:
#                     if st.button(f"Fill Missing Values for {file.name}"):
#                         numeric_cols = df.select_dtypes(include=['number']).columns  # ✅ Correct dtype
#                         df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#                         st.success("Missing Values have been Filled!")
