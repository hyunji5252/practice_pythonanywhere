from django.shortcuts import render, redirect
from random import *
from .models import *
from django.db import connection
from django.urls import reverse
from django.db.models import Q # Q는 Django내 Model을 관리할 때 사용되는 ORM으로 SQL의 WHERE절과 같은 조건문을 추가할 때 사용한다.
#from .forms import *
from datetime import datetime

from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello, World. You're at the polls index.")