from django.shortcuts import render
import util.util as ut
from django.http import HttpResponse
# Create your views here.

def time(request):
    time = ut.getDate()
    return render(request, "index.html", context={"msg": time})