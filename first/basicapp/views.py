from django.shortcuts import render
from basicapp.forms import application
import csv
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')

def users(request):
    form = application()

    if request.method =="POST":
        form=application(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save(commit=True)
            return index(request)
        else:
            print("not valid")

    return render(request,'basicapp/form_page.html',{'form':form})

def download_forms(request):
    return render(request,'basicapp/Application Forms Download Links.html')


def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="info.csv"'
    writer = csv.writer(response)
    writer.writerow(['1001', 'John', 'Domil', 'CA'])
    writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])
    return response
