#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from random import randrange,randint


# In[2]:


import datetime
datetime.datetime.now()


# In[3]:


data= { "time_stamp": "2021-11-07T20:30:46.425Z",
            "interface": [
                {
                    "name": "RX:vale0:G00/r",
                    "pps":randrange(50000),
                    "bps": randrange(50000)

                }
            ],
            "department": 1,
            "position": "Explicit_Down(DownStream)",
            "status": "Operational"
            }


# In[ ]:


allresult=[]
import time

import json
url = "http://127.0.0.1:8000/mitigated-statistics/"

payload=" { \"time_stamp\": \"2021-11-07T20:30:46.425Z\",\n            \"interface\": [\n                {\n                    \"name\": \"RX:vale0:G00/r\",\n                    \"pps\": 767250,\n                    \"bps\": 41444028\n\n                }\n            ],\n            \"department\": 1,\n            \"position\": \"Explicit_Down(DownStream)\",\n            \"status\": \"Operational\"\n            }"
headers = {
  'Authorization': 'ali eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb29rdXBfaWQiOjM4OCwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiIxIiwiZXhwIjoxMDI3NzE1MjY3NSwiZW1haWwiOiJhbGkxMzkxYWxpMTM5MUBnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTYzNzIzOTA3NX0.8mnRF9oeC_Yu-5xd3FATg_5YlM9vofImfwUP50fcaLk',
  'Content-Type': 'application/json',
  'Cookie': 'token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb29rdXBfaWQiOjM3NCwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiIxIiwiZXhwIjoxMDI1OTg2MTAzMCwiZW1haWwiOm51bGwsIm9yaWdfaWF0IjoxNjE5OTQ3NDMwfQ.wdjBzEb_EaTYDV5_hOmXUvF5oK_x6wARdli9WIbA19Q'
}
    
for _ in range(1000):
   
    
    interface=[]
    for _ in range(20):
        face={
  "rx_name": "string",
  "tx_name": "string",
  "rcv_pkt": randint(10000, 50000),
  "rcv_size": randint(10000, 50000),
  "drop_pkt": randint(1000, 5000),
  "drop_size":  randint(1000, 5000),
  "rule_based_drop_pkt": randrange(500),
  "rule_based_drop_size": randrange(500),
  "region_filter_drop_pkt": randrange(500),
  "region_filter_drop_size": randrange(500),
  "ttl_filter_drop_pkt": randrange(500),
  "ttl_filter_drop_size": randrange(50),

  "status": "Ready to Start",


                
        }
        interface.append(face)
#     date=fake.date_time_this_decade()
    data= { 
#         "time_stamp": str(fake.date_time_this_decade()),
         "time_stamp":str(datetime.datetime.now()),
            "department": 1,
        "name": "RX:vale0:G00/r",
       
        
            "position": "Explicit_Down(DownStream)",
            "status": "Operational"
           }
    data['interface']=interface
    allresult.append(data)

    response = requests.request("POST", url, headers=headers, data=json.dumps(data))
#     print(response.text)
    time.sleep(10) # Sleeping for ten second
    


# In[ ]:




