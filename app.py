import streamlit as st
import numpy as np

# Set Streamlit page configuration
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

# Taylor series expansion for sine
def sine(x):
    x = x % 360  # Normalize to 0-360 degrees
    x = x * (np.pi / 180)  # Convert degrees to radians
    sin_x = 0
    term = x  # First term of the series
    i = 1
    while abs(term) > 1e-10:  # Continue until terms are small
        sin_x += term
        i += 1
        term *= -1 * x**2 / ((2 * i - 2) * (2 * i - 1))
    return sin_x

# Taylor series expansion for cosine
def cosine(x):
    x = x % 360  # Normalize to 0-360 degrees
    x = x * (np.pi / 180)  # Convert degrees to radians
    cos_x = 0
    term = 1  # First term of the series
    i = 0
    while abs(term) > 1e-10:  # Continue until terms are small
        cos_x += term
        i += 1
        term *= -1 * x**2 / ((2 * i - 1) * (2 * i))
    return cos_x

# Tangent calculation using sine and cosine
def tangent(x):
    cos_x = cosine(x)
    if abs(cos_x) < 1e-10:  # Prevent division by zero
        return float('inf') if sine(x) > 0 else float('-inf')
    return sine(x) / cos_x

# Title and Introduction
st.title("🧮 Scientific Calculator")
st.write("Perform basic, advanced mathematical operations, and solve equations!")

# Sidebar for user input
st.sidebar.title("Select Operation")
operation = st.sidebar.selectbox(
    "Choose a mathematical operation:",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Power",
        "Square Root",
        "Logarithm",
        "Trigonometry (sin, cos, tan)",
        "Solve n-th Degree Equation"
    ]
)

# Input Fields
st.write("### Enter Input Values")
if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Power"]:
    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)

elif operation == "Square Root":
    num1 = st.number_input("Enter the number to find the square root:", value=0.0)

elif operation == "Logarithm":
    num1 = st.number_input("Enter the number:", value=0.0)
    base = st.number_input("Enter the base (default: 10):", value=10.0)

elif operation == "Trigonometry (sin, cos, tan)":
    angle = st.number_input("Enter the angle in degrees:", value=0.0)

elif operation == "Solve n-th Degree Equation":
    st.write("Enter the coefficients of the polynomial equation:")
    st.write("Example: For \(2x^3 - 4x^2 + 3x - 5 = 0\), enter coefficients as `2, -4, 3, -5`")
    coefficients = st.text_input("Enter coefficients (comma-separated):", value="")

# Perform Calculation
st.write("### Result")
try:
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The sum of {num1} and {num2} is {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The difference between {num1} and {num2} is {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The product of {num1} and {num2} is {result}")
    elif operation == "Division":
        result = num1 / num2
        st.success(f"The division of {num1} by {num2} is {result}")
    elif operation == "Power":
        result = num1**num2
        st.success(f"{num1} raised to the power of {num2} is {result}")
    elif operation == "Square Root":
        result = num1**0.5
        st.success(f"The square root of {num1} is {result}")
    elif operation == "Logarithm":
        result = np.log(num1) / np.log(base)
        st.success(f"The logarithm of {num1} with base {base} is {result}")
    elif operation == "Trigonometry (sin, cos, tan)":
        sin_val = sine(angle)
        cos_val = cosine(angle)
        tan_val = tangent(angle)
        st.success(f"sin({angle}) = {sin_val:.6f}")
        st.success(f"cos({angle}) = {cos_val:.6f}")
        if tan_val == float('inf') or tan_val == float('-inf'):
            st.warning(f"tan({angle}) is undefined (division by zero).")
        else:
            st.success(f"tan({angle}) = {tan_val:.6f}")
    elif operation == "Solve n-th Degree Equation":
        if coefficients:
            coeff_list = [float(c.strip()) for c in coefficients.split(",")]
            roots = np.roots(coeff_list)
            st.success(f"The roots of the equation are: {', '.join(map(str, roots))}")
        else:
            st.warning("Please enter the coefficients to solve the equation.")
except Exception as e:
    st.error(f"Error: {e}")

# Footer
st.write("---")
st.write("Designed with ❤️ by Harsha")
