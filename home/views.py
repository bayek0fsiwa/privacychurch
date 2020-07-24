from django.shortcuts import render, HttpResponse
from django.contrib import messages
from home.models import Contact
from django.contrib import messages
from blog.models import Post
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
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

def search(request):
    query = request.GET['query']
    if len(query) > 50:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    if allPosts.count() == 0:
        messages.warning(request, "No Search result found")
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)

