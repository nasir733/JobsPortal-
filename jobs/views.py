from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from .wwr import extract_wwr_jobs
from django.views.decorators.http import require_GET


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "Disallow: /login/",
        "Disallow: /register/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

# Create your views here.

@csrf_exempt
def wwwrScrapper(request):
    # jobs = extract_indeed_jobs("python")
    jobs = extract_wwr_jobs("python")
    return HttpResponse(jobs)