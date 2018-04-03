from django.shortcuts import render
from main.models import *
from django.http import HttpResponse, HttpResponsRedirect
from django.core.exception import ObjectDoesnotExist
from django.template.loader import render_to_string
from django.shortcuts import render
from django.template import Context, Template
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from dateline import *
import random
import string
# Create your views here.
def home(request):
    suppliers = []
    for x in range(0,3):
        suppliers.append(x)
    context = {
        'title' = 'Helloworld'
        'suppliers' = 'suppliers'
    }
    return HttpResponse(render_to_string('catalog.html', context))