import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="X-Y Data Calculator", page_icon="📊", layout="centered")

st.markdown("""
    <h2 style='text-align: center; color: #4CAF50;'>Curve Fitting Data Calculator</h2>
    <p style='text-align: center; font-size:14px;'>Made by Mohit Kumar A</p>
    """, unsafe_allow_html=True)
st.write("---")

# Input Section
st.subheader("Enter your data")

with st.form(key="data_form"):
    x_values = st.text_input("Enter values of X (comma separated):", "1,2,3,4,5")
    y_values = st.text_input("Enter values of Y (comma separated):", "2,4,6,8,10")
    submit = st.form_submit_button("Generate Table")

if submit:
    try:
        # Convert input to lists of numbers
        x = np.array([float(i.strip()) for i in x_values.split(",") if i.strip() != ""])
        y = np.array([float(i.strip()) for i in y_values.split(",") if i.strip() != ""])

        if len(x) == 0 or len(y) == 0:
            st.error("❌ Please enter both X and Y values.")
        elif len(x) != len(y):
            st.error("❌ Number of X and Y values must be the same.")
        else:
            # Calculations
            df = pd.DataFrame({
                "X": x,
                "Y": y,
                "X²": x**2,
                "X³": x**3,
                "X⁴": x**4,
                "X*Y": x*y,
                "X²*Y": (x**2)*y
            })

            st.subheader("Calculated Table")
            st.dataframe(df, use_container_width=True)

            # Summations
            sums = {
                "ΣX": np.sum(x),
                "ΣY": np.sum(y),
                "ΣX²": np.sum(x**2),
                "ΣX³": np.sum(x**3),
                "ΣX⁴": np.sum(x**4),
                "Σ(X*Y)": np.sum(x*y),
                "Σ(X²*Y)": np.sum((x**2)*y),
            }
            st.subheader("Summations")
            st.write(pd.DataFrame([sums]))

            # Graphical Representation
            st.subheader("Graphical Representation")
            st.line_chart(df[["X", "Y"]])  # Plot only X vs Y for clarity
            # Optional: Let user select columns to plot with st.multiselect

            st.info("✅ Table and graph generated successfully!")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")

st.write("---")
st.markdown("<p style='text-align: center;'>Created by <a href='https://github.com/Mohitkumar2007'>Mohit Kumar A</a></p>", unsafe_allow_html=True)