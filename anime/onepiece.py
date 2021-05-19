
from django.shortcuts import render
import pyrebase
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


topr=db.child('anime').order_by_child('name').equal_to('One Piece').get()
op=topr.val()['1']


