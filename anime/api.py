from jikanpy import Jikan
import requests
import urllib.parse

from django.shortcuts import render
import pyrebase
# jikan = Jikan()
#
#
#
#
# winter_2018_anime = jikan.season(year=2021, season='winter')
# # archive = jikan.top('')
# # xraq=archive
#
#
# xraq=winter_2018_anime


firebaseConfig = {
    'apiKey': "AIzaSyD_hCkHYvWxGBWfIO1Z0COFnt0UxvpOem4",
    'authDomain': "anitosho-1186b.firebaseapp.com",
    'projectId': "anitosho-1186b",
    'storageBucket': "anitosho-1186b.appspot.com",
    'messagingSenderId': "908609361113",
    'appId': "1:908609361113:web:83bf5907f2b29e83da9ac8",
    'measurementId': "G-8RB84DWZTC",
    'databaseURL': "https://anitosho-1186b-default-rtdb.asia-southeast1.firebasedatabase.app/"
  }
firebase=pyrebase.initialize_app(firebaseConfig)


db=firebase.database()
tops=db.child('anime').order_by_child('name').equal_to('Attack on Titan').get()
topf=db.child('anime').order_by_child('name').equal_to('Naruto: Shippuuden').get()
topr=db.child('anime').order_by_child('name').equal_to('One Piece').get()
topt=db.child('anime').order_by_child('name').equal_to('Violet Evergarden').get()
topy=db.child('anime').order_by_child('name').equal_to('Black Clover').get()
topu=db.child('anime').order_by_child('name').equal_to('Sword Art Online').get()

op=topr.val()['1']
vio=topt.val()['5']
bc=topy.val()['7']
sao=topu.val()['8']

def onepiece(request):
    return render(request,'welcome.html',{'op':op})