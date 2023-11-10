from django.shortcuts import render

# Create your views here.
def Blog(request):
    return render(request,"Blog.html")
def chat(request):
    return render(request,'chat.html')