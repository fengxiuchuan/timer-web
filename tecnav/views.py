from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.


def add(request):
	a = request.GET.get('a',0)
	b = request.GET.get('b',0)
	c = int(a) + int(b)
	return HttpResponse(str(c))