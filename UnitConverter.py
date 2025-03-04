# Unit Converter Project (Sir Zia 2nd Project)
# Created By Huzaifa Ghouri (419013) 

import streamlit as st

st.set_page_config(
    page_title="Unit Converter",
    page_icon="📏",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #007bff;
        color: black;
        padding: 12px 25px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        width: 100%;
        font-size: 16px;
        transition: transform 0.2s ease, box-shadow 0.2s ease, background-color 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #0056b3;
        color : white;
        transform: translateY(-3px);
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.2);
    }

    .stButton>button:active {
        color : black;
        transform: scale(0.95);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def convert_units(value, from_unit, to_unit, conversion_type):
    try:
        if conversion_type == "Time":
            return convert_time(value, from_unit, to_unit)
        elif conversion_type == "Weight":
            return convert_weight(value, from_unit, to_unit)
        elif conversion_type == "Length":
            return convert_length(value, from_unit, to_unit)
        elif conversion_type == "Area":
            return convert_area(value, from_unit, to_unit)
        elif conversion_type == "Volume":
            return convert_volume(value, from_unit, to_unit)
        else:
            return "Invalid conversion type"

    except ValueError:
        return "Invalid input units"

def convert_time(value, from_unit, to_unit):
    units = {"seconds": 1, "minutes": 60, "hours": 3600, "days": 86400}
    return value * units[from_unit] / units[to_unit]

def convert_weight(value, from_unit, to_unit):
    units = {"grams": 1, "kilograms": 1000, "pounds": 453.592, "ounces": 28.3495}
    return value * units[from_unit] / units[to_unit]

def convert_length(value, from_unit, to_unit):
    units = {"meters": 1, "centimeters": 0.01, "kilometers": 1000, "feet": 0.3048, "inches": 0.0254, "miles": 1609.34}
    return value * units[from_unit] / units[to_unit]

def convert_area(value, from_unit, to_unit):
    units = {"square meters": 1, "square feet": 0.092903, "acres": 4046.86, "hectares": 10000}
    return value * units[from_unit] / units[to_unit]

def convert_volume(value, from_unit, to_unit):
    units = {"liters": 1, "milliliters": 0.001, "cubic meters": 1000, "gallons": 3.78541}
    return value * units[from_unit] / units[to_unit]

def main():
    st.title("Unit Converter Project")

    conversion_type = st.selectbox("Select Conversion Type", ["Time", "Weight", "Length", "Area", "Volume"])

    value = st.number_input("Enter Value", value=1.0)

    col1, col2 = st.columns(2)

    with col1:
        from_unit = st.selectbox("From Unit", get_units(conversion_type))
    with col2:
        to_unit = st.selectbox("To Unit", get_units(conversion_type))

    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit, conversion_type)
        if isinstance(result, str):
            st.write(result)
        else:
            rounded_result = round(result, 2)
            st.write(f"Result: {value} {from_unit} = {rounded_result} {to_unit}")

def get_units(conversion_type):
    if conversion_type == "Time":
        return ["seconds", "minutes", "hours", "days"]
    elif conversion_type == "Weight":
        return ["grams", "kilograms", "pounds", "ounces"]
    elif conversion_type == "Length":
        return ["meters", "centimeters", "kilometers", "feet", "inches", "miles"]
    elif conversion_type == "Area":
        return ["square meters", "square feet", "acres", "hectares"]
    elif conversion_type == "Volume":
        return ["liters", "milliliters", "cubic meters", "gallons"]
    else:
        return []

if __name__ == "__main__":
    main()