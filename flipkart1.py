#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 13:28:36 2018

@author: sapansoni
"""

import requests
from bs4 import BeautifulSoup as bs

url=requests.get("https://www.flipkart.com/mobiles/pr?sid=tyy%2F4io&p%5B%5D=facets.brand%255B%255D%3DApple&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=clp_metro_expandable_1_apple-categ-94e9d_iPhone_apple-products-store_90ff40fd-a46b-4a40-9440-fbe783136afb_DesktopSite_wp1&fm=neo/merchandising&iid=M_c33a4ac8-1251-4f4e-8d98-a89a8f924a07_1.90ff40fd-a46b-4a40-9440-fbe783136afb_DesktopSite&ppt=CLP&ppn=CLP:apple-products-store")
data= url.content


soup=bs(data,"html.parser")
#print(soup.prettify())
all_mobile_name=soup.find_all("div",{"class":"_3wU53n"})
len(all_mobile_name)    #####showing 24 iphone 

all=soup.find("div",{"class":"_3wU53n"}).text #imp line

all_mobile_name=soup.find_all("div",{"class":"_3wU53n"})

all_mobile=soup.find_all("div",{"class":"_1-2Iqu row"})
len(all_mobile)

for i in all_mobile:
    print(i.find("div",{"class":"_3wU53n"}).text)
    print(i.find("div",{"class":"hGSR34 _2beYZw"}).text)
    print(i.find("div",{"class":"_1vC4OE _2rQ-NK"}).text)
    sap1=soup.find("div",{"class":"_3ULzGw"})
    for set in sap1:
        sap2=set.text
        sap3=[x.strip() for x in sap2.split('|')]
        for val in sap3:
            print(val)
    print(" ")

sap3
my_dict = {}
for k in sap3:
    my_dict[k] = 0

my_dict

new_dict = dict(zip(my_dict.values(),my_dict.keys()))

new_dict














#sap1=soup.find("div",{"class":"_3ULzGw"})
#len(sap1)
#type(sap1)
#for set in sap1:
#    sap2=set.text
#    sap3=[x.strip() for x in sap2.split('|')]
#    for val in sap3:
#        print(val)
#type(val)
#
#
##sap1[0]
##for value in sap1[22]:
##    (value.find_all("li",{"class":"tVe95H"}).text)
#
##abc=(sap1[0].find_all("li",{"class":"tVe95H"}))
##abc
##
##for value in abc:
##    print(value.text)