from django.shortcuts import render, HttpResponse, redirect

from . models import Contact
from . forms import Contacts_Form
from django.contrib import messages

from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'pages/Homepage.html',)
    
# to display info on the webpage
def display_contacts(request):
    all_Contacts = Contact.objects.all()
    # performing searches
    if 'q' in request.GET:
        q=request.GET['q']

         # Filtering by school name or school code
        all_Contacts = Contact.objects.filter(Q(school_name__icontains=q) | Q(school_code__icontains=q))

    # all_Contacts = Contact.objects.all()

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
            messages.success(request, 'school added')

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

# function to delete selected school
def delete_school_record(request, pk):
    if request.user.is_authenticated:
        delete_school_record = Contact.objects.get(id=pk)
        delete_school_record.delete()
        messages.success(request, "School Deleted")
        return redirect('display_Contacts')
    else:
        messages.success(request, "You must be logged in")
        return redirect('')
    
def update_school_record(request, pk):
    if request.user.is_authenticated:
        current_record = Contact.objects.get(id=pk)
        form = Contacts_Form(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated")
            return redirect('display_Contacts')
        return render(request, 'pages/contacts_form.html', {'form': form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')

# to display the privacy policy page
def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html')

# ==============================================================#
# Exporting data as excel
import openpyxl
from django.http import HttpResponse

def export_data_as_excel(request):
    data = Contact.objects.all()

    # Create a new workbook and get the active sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Get the fields dynamically from the model
    fields = Contact._meta.fields

    # Write the header row with field names
    header_row = [field.name for field in fields]
    for col_num, field_name in enumerate(header_row, start=1):
        sheet.cell(row=1, column=col_num, value=field_name)

    # Write the data rows
    for row_num, item in enumerate(data, start=2):
        for col_num, field in enumerate(fields, start=1):
            field_value = getattr(item, field.name)
            sheet.cell(row=row_num, column=col_num, value=field_value)

    # Set the response headers
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=mydata.xlsx'

    # Save the workbook to the response
    workbook.save(response)

    return response











