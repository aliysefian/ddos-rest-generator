#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from random import randrange


# In[2]:


import datetime
datetime.datetime.now()


# In[ ]:


allresult=[]
import time

import json
url = "http://127.0.0.1:8000/DetectdStat/logger/"

headers = {
  'Authorization': 'frd eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb29rdXBfaWQiOjM4OCwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiIxIiwiZXhwIjoxMDI3NzE1MjY3NSwiZW1haWwiOiJhbGkxMzkxYWxpMTM5MUBnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTYzNzIzOTA3NX0.8mnRF9oeC_Yu-5xd3FATg_5YlM9vofImfwUP50fcaLk',
  'Content-Type': 'application/json',
  'Cookie': 'token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb29rdXBfaWQiOjM3NCwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiIxIiwiZXhwIjoxMDI1OTg2MTAzMCwiZW1haWwiOm51bGwsIm9yaWdfaWF0IjoxNjE5OTQ3NDMwfQ.wdjBzEb_EaTYDV5_hOmXUvF5oK_x6wARdli9WIbA19Q'
}
    
for _ in range(1000):
    data={
           "time_stamp":str(datetime.datetime.now()),
           "state":{
              "TCP_CNT":"AttackLevel:5",
              "TCP_BYTE":"AttackLevel:9",
              "UDP_CNT":"Normal",
              "UDP_BYTE":"Normal",
              "OTHER_CNT":"Normal",
              "OTHER_BYTE":"Normal",
              "AVG_PKT_SIZE":"Normal",
              "FLOW_CNT":"AttackLevel:5",
              "SYN_CNT":"Normal",
              "FIN_CNT":"Normal",
              "ACK_CNT":"AttackLevel:5",
              "RST_CNT":"Normal",
              "PSH_CNT":"AttackLevel:5",
              "TCP_OTHER_IP_FLAG_CNT":"Normal",
              "INVALID_PKT_CNT":"Normal",
              "SMALL_PKT_CNT":"AttackLevel:5"
           },
           "current":{
              "TCP_CNT":randrange(500000),
              "TCP_BYTE":randrange(500000),
              "UDP_CNT":randrange(500000),
              "UDP_BYTE":randrange(500000),
              "OTHER_CNT":randrange(500),
              "OTHER_BYTE":randrange(500),
              "AVG_PKT_SIZE":randrange(1500),
              "FLOW_CNT":randrange(1500),
              "SYN_CNT":randrange(1500),
              "FIN_CNT":randrange(1500),
              "ACK_CNT":randrange(1500),
              "RST_CNT":randrange(1500),
              "PSH_CNT":randrange(1500),
              "TCP_OTHER_IP_FLAG_CNT":randrange(80),
              "INVALID_PKT_CNT":randrange(1500),
              "SMALL_PKT_CNT":randrange(1500)
           },
           "average":{
              "TCP_CNT":randrange(1500),
              "TCP_BYTE":randrange(1500),
              "UDP_CNT":randrange(1500),
              "UDP_BYTE":randrange(1500),
              "OTHER_CNT":randrange(1500),
              "OTHER_BYTE":randrange(1500),
              "AVG_PKT_SIZE":randrange(1500),
              "FLOW_CNT":randrange(1500),
              "SYN_CNT":randrange(1500),
              "FIN_CNT":randrange(1500),
              "ACK_CNT":randrange(1500),
              "RST_CNT":randrange(1500),
              "PSH_CNT":randrange(1500),
              "TCP_OTHER_IP_FLAG_CNT":randrange(1500),
              "INVALID_PKT_CNT":randrange(1500),
              "SMALL_PKT_CNT":randrange(1500)
           },
           "std":{
              "TCP_CNT":randrange(1500),
              "TCP_BYTE":randrange(1500),
              "UDP_CNT":randrange(1500),
              "UDP_BYTE":randrange(1500),
              "OTHER_CNT":randrange(1500),
              "OTHER_BYTE":randrange(1500),
              "AVG_PKT_SIZE":randrange(1500),
              "FLOW_CNT":randrange(1500),
              "SYN_CNT":randrange(1500),
              "FIN_CNT":randrange(1500),
              "ACK_CNT":randrange(1500),
              "RST_CNT":randrange(1500),
              "PSH_CNT":randrange(1500),
              "TCP_OTHER_IP_FLAG_CNT":randrange(1500),
              "INVALID_PKT_CNT":randrange(1500),
              "SMALL_PKT_CNT":randrange(1500)
           },
           "department":1
        }
    allresult.append(data)
    response = requests.request("POST", url, headers=headers, data=json.dumps(data))
#     print(response.text)
    time.sleep(20) # Sleeping for ten second
#     6f137f44-5834-41cd-b4b3-c5f5eaaa3eb4


# In[42]:


allresult=[]
import time

import json
url = "http://127.0.0.1:8000/DetectdStat/logger/"

headers = {
  'Authorization': 'ali eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb29rdXBfaWQiOjM4OCwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiIxIiwiZXhwIjoxMDI3NzE1MjY3NSwiZW1haWwiOiJhbGkxMzkxYWxpMTM5MUBnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTYzNzIzOTA3NX0.8mnRF9oeC_Yu-5xd3FATg_5YlM9vofImfwUP50fcaLk',
  'Content-Type': 'application/json',
  'Cookie': 'token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb29rdXBfaWQiOjM3NCwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiIxIiwiZXhwIjoxMDI1OTg2MTAzMCwiZW1haWwiOm51bGwsIm9yaWdfaWF0IjoxNjE5OTQ3NDMwfQ.wdjBzEb_EaTYDV5_hOmXUvF5oK_x6wARdli9WIbA19Q'
}
    
for _ in range(1000):
    data={
           "time_stamp":str(datetime.datetime.now()),
           "state":{
              "TCP_CNT":"Normal",
              "TCP_BYTE":"Normal",
              "UDP_CNT":"Normal",
              "UDP_BYTE":"Normal",
              "OTHER_CNT":"Normal",
              "OTHER_BYTE":"Normal",
              "AVG_PKT_SIZE":"Normal",
              "FLOW_CNT":"AttackLevel:5",
              "SYN_CNT":"Normal",
              "FIN_CNT":"Normal",
              "ACK_CNT":"AttackLevel:5",
              "RST_CNT":"Normal",
              "PSH_CNT":"AttackLevel:5",
              "TCP_OTHER_IP_FLAG_CNT":"Normal",
              "INVALID_PKT_CNT":"Normal",
              "SMALL_PKT_CNT":"AttackLevel:5"
           },
           "current":{
              "TCP_CNT":randrange(500000),
              "TCP_BYTE":randrange(500000),
              "UDP_CNT":randrange(500000),
              "UDP_BYTE":randrange(500000),
              "OTHER_CNT":randrange(500),
              "OTHER_BYTE":randrange(500),
              "AVG_PKT_SIZE":randrange(1500),
              "FLOW_CNT":randrange(1500),
              "SYN_CNT":randrange(1500),
              "FIN_CNT":randrange(1500),
              "ACK_CNT":randrange(1500),
              "RST_CNT":randrange(1500),
              "PSH_CNT":randrange(1500),
              "TCP_OTHER_IP_FLAG_CNT":randrange(80),
              "INVALID_PKT_CNT":randrange(1500),
              "SMALL_PKT_CNT":randrange(1500)
           },
           "average":{
              "TCP_CNT":randrange(1500),
              "TCP_BYTE":randrange(1500),
              "UDP_CNT":randrange(1500),
              "UDP_BYTE":randrange(1500),
              "OTHER_CNT":randrange(1500),
              "OTHER_BYTE":randrange(1500),
              "AVG_PKT_SIZE":randrange(1500),
              "FLOW_CNT":randrange(1500),
              "SYN_CNT":randrange(1500),
              "FIN_CNT":randrange(1500),
              "ACK_CNT":randrange(1500),
              "RST_CNT":randrange(1500),
              "PSH_CNT":randrange(1500),
              "TCP_OTHER_IP_FLAG_CNT":randrange(1500),
              "INVALID_PKT_CNT":randrange(1500),
              "SMALL_PKT_CNT":randrange(1500)
           },
           "std":{
              "TCP_CNT":randrange(1500),
              "TCP_BYTE":randrange(1500),
              "UDP_CNT":randrange(1500),
              "UDP_BYTE":randrange(1500),
              "OTHER_CNT":randrange(1500),
              "OTHER_BYTE":randrange(1500),
              "AVG_PKT_SIZE":randrange(1500),
              "FLOW_CNT":randrange(1500),
              "SYN_CNT":randrange(1500),
              "FIN_CNT":randrange(1500),
              "ACK_CNT":randrange(1500),
              "RST_CNT":randrange(1500),
              "PSH_CNT":randrange(1500),
              "TCP_OTHER_IP_FLAG_CNT":randrange(1500),
              "INVALID_PKT_CNT":randrange(1500),
              "SMALL_PKT_CNT":randrange(1500)
           },
           "department":1
        }
    allresult.append(data)
    response = requests.request("POST", url, headers=headers, data=json.dumps(data))
#     print(response.text)
    time.sleep(10) # Sleeping for ten second
    




