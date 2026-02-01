# Coordinates of the three points
latitudes = [41.1257402, 35.6588976, 1.2839244]
longitudes = [71.4441618, 139.7451182, 103.8607049]

# Calculating the centroid (average of latitudes and longitudes)
centroid_lat = sum(latitudes) / len(latitudes)
centroid_lon = sum(longitudes) / len(longitudes)

print("Centroid Latitude:", centroid_lat)
print("Centroid Longitude:", centroid_lon)
