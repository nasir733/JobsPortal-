from django.http import HttpResponse
from django.shortcuts import render
from.wwr import extract_wwr_jobs
# Create your views here.



def wwwrScrapper(request):
    # jobs = extract_indeed_jobs("python")
    jobs = extract_wwr_jobs("python")
    return HttpResponse(jobs)