from django.shortcuts import render, HttpResponse

def index(request):
    print ("Hello Wooooorld!")
    return render(request, 'helloworld/index.html')
