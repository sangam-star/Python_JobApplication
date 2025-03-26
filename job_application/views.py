from django.shortcuts import render
from .forms import ApplicationForm
#from database model import Form
from .models import Form

 
def index(request):
    if request.method == "POST":
        # Step 1: Handle the POST request
        form = ApplicationForm(request.POST)
        
        if form.is_valid():
            # Step 2: Extract data from the form
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']
            
            # Step 3: Save the data to the database
            Form.objects.create(
                first_name=first_name, 
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation
            )
            
            # Step 4: Return a success response
            return render(request, "index.html", {'form': form, 'success': True})
        
    else:
        # Step 5: Handle GET request (display empty form)
        form = ApplicationForm()
    
    return render(request, "index.html", {'form': form})
 
 
 
 