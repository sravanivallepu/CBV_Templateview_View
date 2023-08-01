from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *

class Data_render(View):
    def get(self,request):
        d={'name':'KANNA'}
        return render(request,'data_render.html',d)

def fbv_form(request):
    SFO=StudentForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('Data inserted')
    return render(request,'fbv_form.html',d)

class Cbv_form(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'Cbv_form.html',d)
    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('Data inserted')



class Temp(TemplateView):
    template_name='temp.html'