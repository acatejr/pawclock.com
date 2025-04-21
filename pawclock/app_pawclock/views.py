from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Render the index page.
    """
    return render(request, "index.html")

def about(request):
    """
    Render the about page.
    """
    return render(request, "about.html")

def contact(request):
    """
    Render the contact page.
    """
    return render(request, "contact.html")

def privacy(request):
    """
    Render the privacy policy page.
    """
    return render(request, "privacy.html")
