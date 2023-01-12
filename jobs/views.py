from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from .wwr import extract_wwr_jobs

# Create your views here.

@csrf_exempt
def wwwrScrapper(request):
    # jobs = extract_indeed_jobs("python")
    jobs = extract_wwr_jobs("python")
    return HttpResponse(jobs)