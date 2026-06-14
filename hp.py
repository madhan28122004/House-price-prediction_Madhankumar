import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 House Price Prediction")
st.write("Predict house prices using Machine Learning.")

# Load Dataset
data = pd.read_csv("house.csv")

# Encode House Type
encoder = LabelEncoder()
data['House_Type'] = encoder.fit_transform(data['House_Type'])

# Features and Target
X = data[['House_Type',
          'Area_sqft',
          'Bedrooms',
          'Bathrooms',
          'Floors',
          'Age',
          'Parking',
          'Location_Score']]

y = data['Price']

# Train Model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)
accuracy = r2_score(y_test, y_pred)

st.success(f"Model Accuracy (R² Score): {accuracy:.2f}")

st.subheader("Enter House Details")

house_name = st.selectbox(
    "House Type",
    encoder.classes_
)

area_sqft = st.number_input(
    "Area (sqft)",
    min_value=100,
    value=1000
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    value=2
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    value=2
)

floors = st.number_input(
    "Floors",
    min_value=1,
    value=1
)

age = st.number_input(
    "House Age",
    min_value=0,
    value=5
)

parking = st.number_input(
    "Parking Spaces",
    min_value=0,
    value=1
)

location_score = st.slider(
    "Location Score",
    1.0,
    10.0,
    5.0
)

if st.button("Predict Price"):

    house_type = encoder.transform([house_name])[0]

    new_house = pd.DataFrame(
        [[house_type,
          area_sqft,
          bedrooms,
          bathrooms,
          floors,
          age,
          parking,
          location_score]],
        columns=[
            'House_Type',
            'Area_sqft',
            'Bedrooms',
            'Bathrooms',
            'Floors',
            'Age',
            'Parking',
            'Location_Score'
        ]
    )

    predicted_price = model.predict(new_house)

    st.success(
        f"🏠 Predicted House Price: ₹ {predicted_price[0]:,.2f}"
    )

st.markdown("---")
st.caption("Developed by Madhankumar M")
