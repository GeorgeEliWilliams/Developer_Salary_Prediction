import streamlit as st
import pickle
import numpy as np

# Function to load the saved model and encoders
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

# Load the model and encoders
data = load_model()
regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]


# Function to display the prediction page
def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to make the prediction""")

   # Available countries and education levels for selection 
    countries = (
        'United States',
        'India',
        'United Kingdom',
        'Germany',
        'Canada',
        'Brazil',
        'France',
        'Spain',
        'Australia',
        'Netherlands',
        'Poland',
        'Italy',
        'Russian Federation',
        'Sweden'
        'United States',
        'India',
    )

    education = (
        "Less than a Bachelors",
        "Bachelor's degree",
        "Master's degree",
        "Post grad",
    )

# User input: country, education level, and years of experience
    country = st.selectbox("Country",countries)
    education = st.selectbox("Education Level",education)

    experience = st.slider("Years of Experience",0,50,3)

# Button to trigger salary calculation
    ok = st.button("Calculate Salary")
    # Calculate and display estimated salary when button is pressed
    if ok:
        X = np.array([[country, education, experience ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

# Predict salary and display
        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")

