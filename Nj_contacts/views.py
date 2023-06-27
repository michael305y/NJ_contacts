from django.shortcuts import render, HttpResponse, redirect

from . models import Contact
from . forms import Contacts_Form
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'pages/Homepage.html',)
    return HttpResponse('cool welcome')

def display_contacts(request):
    all_Contacts = Contact.objects.all()

    context = {
        'all_Contacts': all_Contacts
    }

    return render(request, 'pages/contacts.html', context=context)

def show_Contact_Form(request):
    form = Contacts_Form()

    if request.method == 'POST':
        form = Contacts_Form(request.POST)

        # checking validity of the form b4 saving
        if form.is_valid():
            form.save()
            messages.info(request, 'school added')

            return redirect('display_Contacts')
        
    context = {
        'form' : form
    }

    return render(request, 'pages/contacts_form.html', context=context)

# displays the school details
def school_details(request, pk):
    specific_School = Contact.objects.get(id=pk)

    context = {
       'specific_School': specific_School
    }

    return render(request, 'pages/school_details.html', context=context)

# to display the privacy policy page
def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html')








