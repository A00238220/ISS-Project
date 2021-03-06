#importing libraries
#import urllib.request, json
import requests, random

def country(name):  
  #making api call
    
  url = f'http://restcountries.com/v3.1/alpha/{name}'

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
  
  #request = urllib.request.urlopen(url)
  #result = json.loads(request.read())
  #result = requests.get(url, headers=headers).json()
  
  return result