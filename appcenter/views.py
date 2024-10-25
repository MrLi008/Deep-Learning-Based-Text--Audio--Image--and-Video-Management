from datetime import datetime
import os
import time

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as django_default_login
from django.contrib.auth.views import login_required
from django.contrib.auth.models import User
from .form import *
from .models import *


def index(request):
    if request.method == "GET":
        return HttpResponse(loader.get_template("appcenter/index.html"), locals())
    return HttpResponse(loader.get_template("appcenter/index.html"), locals())
