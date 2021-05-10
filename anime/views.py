import json

import requests
from django.http import HttpResponse
from django.shortcuts import render
import http.client
from .models import APIData
from .service import PaginationAnime
from . import api
def allanime(request):
    x_val = api.xraq
    return render(request,'welcome.html',{'res':x_val})




