from django.shortcuts import render
import pyrebase
from django.contrib import auth
firebaseConfig = {
    'apiKey': "AIzaSyD_hCkHYvWxGBWfIO1Z0COFnt0UxvpOem4",
    'authDomain': "anitosho-1186b.firebaseapp.com",
    'projectId': "anitosho-1186b",
    'storageBucket': "anitosho-1186b.appspot.com",
    'messagingSenderId': "908609361113",
    'appId': "1:908609361113:web:83bf5907f2b29e83da9ac8",
    'measurementId': "G-8RB84DWZTC",
    'databaseURL': "ref"
  }
firebase=pyrebase.initialize_app(firebaseConfig)
authe=firebase.auth()
database=firebase.database()
def signIn(request):
    return render(request, "signIn.html")
def postsign(request):
    email=request.POST.get('email')
    passw=request.POST.get('passw')
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message="Invalid credentials"
        return render(request, "signIn.html", {"message":message})
    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"welcome.html",{"e":email})
def logout(request):
    auth.logout(request)
    return render(request, "signIn.html")
def signup(request):
    return render(request,"signup.html")
def postsignup(request):
    email=request.POST.get('email')
    passw=request.POST.get('passw')
    try:
        user=authe.create_user_with_email_and_password(email,passw)
    except:
        message="Unable to create account try again"
        return render(request, "signIn.html", {"message"})
        uid = user['localId']
    authe.send_email_verification(user['idToken'])
    return render(request, "signIn.html")