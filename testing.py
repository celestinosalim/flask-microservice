import requests 
import itertools

# r = requests.get("http://localhost:5000/voter/1")    

for _ in itertools.repeat(requests.get("http://localhost:5000/voter/1"), 15):
    r = requests.get("http://localhost:5000/voter/1")   
    print(r.status_code) 



    
    
