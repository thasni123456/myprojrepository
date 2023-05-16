from django.shortcuts import render

#create your vies here
def newapp(request):
    return render(request,'newapp/newapp.html')

def aboutus(request):
    return render(request,'newapp/aboutus.html')