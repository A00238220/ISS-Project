
#importing libraries and modules
from address import address
from iss_loc import iss_loc
from weather import get_weather
from country import country
from distance import dist
from flask import Flask, render_template


#46.49400461430174, -80.99676848856024
#print(country('IN'))

#setting flask app
app = Flask('app')

@app.route('/')
def home():
  
  #assigning location of apace station to a variable
  data = iss_loc()
  lat, lon = data[0], data[1]

  print(lat, lon)
  #printing google map link of space station live position
  loc =  "https://www.google.com/maps/place/" + lat + "+" + lon
  print(f"google map: {loc}")

  #assigning weather below space station to a variable
  weather = get_weather(lat, lon)
  

  #calculating the distance between me and the space station
  distance = dist(lat, lon, 46.49400461430174, -80.99676848856024)
  print(f"I am {distance}kms away from the ISS")

  #setting address reverse geolocation
  addr = address(lat, lon)  
  print(addr["results"][0]['locations'][0]["adminArea1"])

  #setting conditional statements to check case when ISS is above water
  if addr["results"][0]['locations'][0]["adminArea1"] == "XZ":
    print('The ISS is above water')
    
    #setting country variables to an empty list 
    cont_code = addr["results"][0]['locations'][0]["adminArea1"]    
    flag = ""
    cont_name = ""
    coa = ""
    pop = ""
    
    #setting weather variables to an empty list  
    temp_c = ""
    desc = ""
    icon = ""
    feels_like = ""
    speed = ""


  else:
    #extracting country data and saving in a variable 
    cont_code = addr["results"][0]['locations'][0]["adminArea1"]
    flag = country(cont_code)[0]["flags"]["png"]
    cont_name = country(cont_code)[0]["name"]["common"]
    coa = country(cont_code)[0]["coatOfArms"]["png"]
    pop = country(cont_code)[0]["population"] 
    
    #extracting temperature data and saving in a variable 
    temp_c = round(weather["main"]["temp"] - 273.15,2)
    desc = weather["weather"][0]['description']
    icon = weather["weather"][0]['icon']
    feels_like = round(weather["main"]["feels_like"] - 273.15,2)
    speed = round(weather["wind"]["speed"],2)
    
  #creating dictionary to store extracted data
  data = {
  "latitude" : lat,
  "longitude" : lon,
  "location" : loc,
  "distance" : distance, 
  "cont_code" : cont_code,
  "flag" : flag,
  "temperature" : temp_c,
  "description" : desc,
  "icon" : icon,
  "feels_like" : feels_like,
  "speed" : speed,
  "cont_name" : cont_name,
  "coa" : coa,
  "pop" : pop,

  }
      
      
  return render_template('index.html', data=data)
  

app.run(host='0.0.0.0', port=8080, debug=True)





