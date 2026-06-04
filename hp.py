import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score
data = pd.read_csv("house.csv")
print("Dataset:")
print(data.head())
print("\nMissing Values:")
print(data.isnull().sum())
encoder = LabelEncoder()
data['House_Type'] = encoder.fit_transform(data['House_Type'])
print("\nHouse Type Encoding:")
for house, code in zip(encoder.classes_,
                       encoder.transform(encoder.classes_)):
    print(f"{house} = {code}")
X = data[['House_Type',
          'Area_sqft',
          'Bedrooms',
          'Bathrooms',
          'Floors',
          'Age',
          'Parking',
          'Location_Score']]
y = data['Price']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("\nModel Performance:")
print("R2 Score:", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("\nAvailable House Types:")
for house in encoder.classes_:
    print("-", house)
house_name = input("\nEnter House Type: ")
house_type = encoder.transform([house_name])[0]
area_sqft = float(input("Enter Area in sqft: "))
bedrooms = int(input("Enter Number of Bedrooms: "))
bathrooms = int(input("Enter Number of Bathrooms: "))
floors = int(input("Enter Number of Floors: "))
age = int(input("Enter House Age (years): "))
parking = int(input("Enter Parking Spaces: "))
location_score = float(input("Enter Location Score: "))
new_house = pd.DataFrame(
    [[house_type,
      area_sqft,
      bedrooms,
      bathrooms,
      floors,
      age,
      parking,
      location_score]],
    columns=['House_Type',
             'Area_sqft',
             'Bedrooms',
             'Bathrooms',
             'Floors',
             'Age',
             'Parking',
             'Location_Score']
)
predicted_price = model.predict(new_house)
print("\nPredicted House Price: ₹ {:.2f}".format(predicted_price[0]))