from django.shortcuts import render

def login(request):
    return render(request, 'pages/login.html', {})

def register(request):
    return render(request, 'pages/register.html', {})

def forgot_password(request):
    return render(request, 'pages/forgot_password.html', {})

def change_password(request):
    return render(request, 'pages/change_password.html', {})

def otp(request):
    return render(request, 'pages/otp.html', {})

def dashboard(request):
    return render(request, 'pages/dashboard.html', {})

def profile(request):
    return render(request, 'pages/profile.html', {})

def upgrade_plan(request):
    return render(request, 'pages/upgrade_plan.html', {})

def lookalike_finder(request):
    return render(request, 'pages/lookalike_finder.html', {})

def lookalike_finder_sidebar(request):
    return render(request, 'pages/lookalike_finder_sidebar.html', {})

def search(request):
    return render(request, 'pages/search.html', {})

def search_company(request):
    return render(request, 'pages/search_company.html', {})

def search_person(request):
    return render(request, 'pages/search_person.html', {})

def company_profile(request):
    return render(request, 'pages/company_profile.html', {})

def person_profile(request):
    return render(request, 'pages/person_profile.html', {})

def list(request):
    return render(request, 'pages/list.html', {})
    
def export_log(request):
    return render(request, 'pages/export_log.html', {})

def saved_search(request):
    return render(request, 'pages/saved_search.html', {})

def email_personalization(request):
    return render(request, 'pages/email_personalization.html', {})
