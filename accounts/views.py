from django.shortcuts import render
from django.http import HttpResponse, response

import logging
logger = logging.getLogger(__name__)
logger = logging.getLogger('django')
logger_api = logging.getLogger('api')

def index(request):
        
    return HttpResponse("Hello, world. You're at the polls index.")

def temp(request):
    return render(request, 'accounts/login.html')   