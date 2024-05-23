
import json 
from  pprint import pprint 
 
 
data = { 
    "name":"Shams Shirali", 
    "version":"1.0.0", 
    "server": { 
      "port": "2024", 
      "port2": "2025" 
    }, 
    "openInBrowser": True, 
      "dist": { 
        "fonts": "NewsARoman", 
        "img": "icon.png" 
      } 
} 
 
with open('my_config.json', 'w', encoding="utf-8") as file: 
    json.dump(data, file, ensure_ascii=False, indent=4) 
 
pprint(data)