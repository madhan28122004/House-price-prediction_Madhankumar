import pandas as pd
import random

data = []

house_types = ["Apartment", "1BHK", "2BHK", "3BHK", "Villa", "Mansion"]

for i in range(100):
    house_type = random.choice(house_types)

    if house_type == "Apartment":
        area = random.randint(300, 800)
        bedrooms = 1
        bathrooms = random.randint(1, 2)
        floors = 1
        price = random.randint(2000000, 4000000)

    elif house_type == "1BHK":
        area = random.randint(500, 900)
        bedrooms = 1
        bathrooms = random.randint(1, 2)
        floors = 1
        price = random.randint(3000000, 5000000)

    elif house_type == "2BHK":
        area = random.randint(800, 1500)
        bedrooms = 2
        bathrooms = random.randint(2, 3)
        floors = random.randint(1, 2)
        price = random.randint(5000000, 8000000)

    elif house_type == "3BHK":
        area = random.randint(1200, 2500)
        bedrooms = 3
        bathrooms = random.randint(2, 4)
        floors = random.randint(1, 2)
        price = random.randint(7000000, 12000000)

    elif house_type == "Villa":
        area = random.randint(2000, 5000)
        bedrooms = random.randint(4, 5)
        bathrooms = random.randint(3, 5)
        floors = random.randint(1, 3)
        price = random.randint(15000000, 40000000)

    else:  # Mansion
        area = random.randint(5000, 10000)
        bedrooms = random.randint(5, 8)
        bathrooms = random.randint(5, 8)
        floors = random.randint(2, 4)
        price = random.randint(50000000, 100000000)

    age = random.randint(0, 20)
    parking = random.randint(1, 4)
    location_score = random.randint(1, 10)

    data.append([
        house_type, area, bedrooms, bathrooms,
        floors, age, parking, location_score, price
    ])

df = pd.DataFrame(data, columns=[
    "House_Type", "Area_sqft", "Bedrooms",
    "Bathrooms", "Floors", "Age",
    "Parking", "Location_Score", "Price"
])

df.to_csv("house.csv", index=False)

print("100-row house.csv created successfully!")