#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 14:25:21 2021

@author: greg
"""
import pandas as pd
import numpy as np
import xml.etree.ElementTree as et
import json

#reading the simple.json file
simplejson=pd.read_json("simple.json")

#reading xml and creating dataframe from the xml

simplexml=et.parse("simple.xml")
xroot = simplexml.getroot()

xid =simplexml.find("id").text
xbrand = simplexml.find("brand").text
xmodel = simplexml.find("model").text
xyear = simplexml.find("year").text
xown = simplexml.find("owned_by").text
xacc = simplexml.find("acquired").text
xprice = simplexml.find("price").text

df_data = []
df_cols = ["id","brand","model","year","owned_by","acquired","price"]
row = {
       "id":xid,
       "brand":xbrand,
       "model":xmodel,
       "year":xyear,
       "owned_by":xown,
       "acquired":xacc,
       "price":xprice
       }

df_data.append(row)

df = pd.DataFrame(data=df_data,columns=df_cols)








