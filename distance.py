#importing libraries
import geopy.distance

def dist(coords_1_lat, coords_1_lon, coords_2_lat, coords_2_lon):
  #setting coordinates
  coords_1 = (coords_1_lat, coords_1_lon)
  coords_2 = (coords_2_lat, coords_2_lon)
  
  #calculating geopy distance between coordinates
  return round(geopy.distance.distance(coords_1, coords_2).km,2)

  #https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude

