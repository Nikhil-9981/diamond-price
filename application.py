import streamlit as st
import pandas as pd
from src.DiamondPricePrediction.pipelines.Prediction_Pipeline import CustomData, PredictPipeline

# Set up the title and description of the app
st.title("Diamond Price Prediction App")
st.write("Enter the details of the diamond to predict its price.")

# Create input fields for the user to provide data
carat = st.number_input("Carat", min_value=0.0, step=0.01, format="%.2f")
depth = st.number_input("Depth", min_value=0.0, step=0.01, format="%.2f")
table = st.number_input("Table", min_value=0.0, step=0.01, format="%.2f")
x = st.number_input("X Dimension (mm)", min_value=0.0, step=0.01, format="%.2f")
y = st.number_input("Y Dimension (mm)", min_value=0.0, step=0.01, format="%.2f")
z = st.number_input("Z Dimension (mm)", min_value=0.0, step=0.01, format="%.2f")

cut = st.selectbox("Cut", options=["Fair", "Good", "Very Good", "Premium", "Ideal"])
color = st.selectbox("Color", options=["J", "I", "H", "G", "F", "E", "D"])
clarity = st.selectbox("Clarity", options=["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"])

# Function to handle predictions
if st.button("Predict Price"):
    # Create the CustomData object using user inputs
    data = CustomData(
        carat=carat,
        depth=depth,
        table=table,
        x=x,
        y=y,
        z=z,
        cut=cut,
        color=color,
        clarity=clarity
    )
    
    # Convert to dataframe
    final_data = data.get_data_as_dataframe()

    # Make prediction
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(final_data)

    # Display the prediction result
    result = round(pred[0], 2)
    st.success(f"The predicted price of the diamond is: {result}")

# Run the streamlit app with: `streamlit run app.py`
