#importing libraries
#import urllib.request
import requests, random

def iss_loc():
  
  url = "http://api.open-notify.org/iss-now.json"
  
  #result = requests.get(url).json()
  #request = urllib.request.urlopen(url)
  #result = json.loads(request.read())
  
  user_agents = [ 
  	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
  	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
  	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 
  	'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 
  	'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36' 
  ] 
  
  user_agent = random.choice(user_agents) 
  headers = {'User-Agent': user_agent,
            'Accept-Language': 'en-GB,en;q=0.5',
            'Referer' : 'https://google.com',
            'DNT' : "1",
             'John' : 'subtomeplease'
            } 
  
  result = requests.get(url, headers=headers).json()
  
  #print(result)
  #extracting latitude and longitude for space station
  lat = result['iss_position']['latitude']
  lon = result['iss_position']['longitude']
  
  return lat, lon
