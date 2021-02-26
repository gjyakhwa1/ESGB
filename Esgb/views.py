from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,'Esgb/contact.html')
def index(request):
    return render(request,'Esgb/index.html',
                  {
                      'content':'Welcome to ESGB Database'
                      }
                  )
def addData(request):
    return render(request,'Esgb/addData.html',
                   {
                       'content':'Add Data',
                       })
def displayData(request):
    return render(request,'Esgb/displayData.html',
                  {
                      'content':'Display Data',
                      }
                  )