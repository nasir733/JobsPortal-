from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from jobs.models import Job
from django.core.paginator import Paginator

# Create your views here.

@login_required
def dashboard(request):
    # Get the list of objects that need to be paginated
    objects_list = Job.objects.all()
    if request.method=="POST":
        sort_by = request.POST.get('sort_by')
        if sort_by == 'descending':
            objects_list = Job.objects.all().order_by('-created_at')
        else:
            objects_list = Job.objects.all().order_by('created_at')
            
        print(sort_by)
        
        
    

    # Create a paginator object
    paginator = Paginator(objects_list, 10)  # Show 10 Jobs per page

    # Get the page number from the request
    page_number = request.GET.get('page')

    # Get the objects for the current page
    jobs = paginator.get_page(page_number)

    # Render the template with the paginated objects
    return render(request, 'dashboard.html', {'jobs': jobs})
