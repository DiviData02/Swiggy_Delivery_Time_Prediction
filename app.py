import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Swiggy Delivery Time Prediction", page_icon="🚴", layout="centered")
st.title("🚴‍♂️ Swiggy Delivery Time Prediction")

# Load dataset for dropdown options
df = pd.read_csv('swiggy_cleaned (1).csv').dropna()

# Load model
model = joblib.load('model.pkl')

# Input columns (includes order_day)
input_columns = [
    'age', 'ratings', 'weather', 'traffic', 'vehicle_condition',
    'type_of_order', 'type_of_vehicle', 'multiple_deliveries', 'festival',
    'city_type', 'city_name', 'order_day', 'is_weekend',
    'pickup_time_minutes', 'order_time_hour', 'order_time_of_day', 'distance'
]

# Three-column layout
col1, col2, col3 = st.columns(3)

with col1:
    Age = st.number_input('Age of Partner', 18, 60, 25)
    Rating = st.number_input('⭐ Rating', 1, 5, 4)
    weather = st.selectbox('Weather', df['weather'].unique())
    traffic = st.selectbox('Traffic', df['traffic'].unique())
    vehicle_condition = st.selectbox('Vehicle Condition', df['vehicle_condition'].unique())
    type_of_order = st.selectbox('Order Type', df['type_of_order'].unique())

with col2:
    type_of_vehicle = st.selectbox('Vehicle Type', df['type_of_vehicle'].unique())
    order_day = st.number_input('Order Day', 1, 31, 15)
    multiple_deliveries = st.number_input('Deliveries', 1, 3, 1)
    festival = st.selectbox('Festival', df['festival'].unique())
    city_type = st.selectbox('City Type', df['city_type'].unique())
    city_name = st.selectbox('City Name', df['city_name'].unique())

with col3:
    is_weekend = st.number_input('Weekend? (1/0)', 0, 1, 0)
    pickup_time_minutes = st.number_input('Pickup Time (min)', 1, 100, 15)
    order_time_hour = st.number_input('Order Hour', 0, 23, 12)
    order_time_of_day = st.selectbox('Time of Day', df['order_time_of_day'].unique())
    distance = st.number_input('Distance (km)', 1, 100, 5)

# Prepare DataFrame
data = pd.DataFrame([[
    Age, Rating, weather, traffic, vehicle_condition, type_of_order,
    type_of_vehicle, multiple_deliveries, festival, city_type, city_name,
    order_day, is_weekend, pickup_time_minutes,
    order_time_hour, order_time_of_day, distance
]], columns=input_columns)

# Predict
if st.button("🔮 Predict Delivery Time"):
    result = model.predict(data)[0]
    st.success(f"🕐 Estimated Delivery Time: **{round(result, 2)} minutes**")
