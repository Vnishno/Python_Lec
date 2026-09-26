locations = [("Tbilisi", 41.71, 44.82), ("Batumi", 41.64, 41.63), ("Kutaisi", 42.26, 42.71)]

for city, lat , long in locations:
    print(f"City: {city}, Latitude: {lat}, Longitude: {long}")

city_names = [city[0] for city in locations]
print(city_names)