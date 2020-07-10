from django.shortcuts import render, HttpResponse
from django.contrib import messages
from home.models import Contact
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['emai']
        content = request.POST['content']
        print(name, email, content)
        
        if len(name)<2 or len(email)<3 or len(content)<4:
            messages.error(request, "Please Fill The Form Correctly")
        else:
            contact = Contact(name=name, email=email, content=content)
            contact.save()
            messages.success(request, "Message Sent Successfully")

    return render(request, 'home/contact.html')

def privacypolicy(request):
    return render(request, 'home/privacypolicy.html')

