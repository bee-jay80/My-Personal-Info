from django.shortcuts import render, redirect
import os
from dotenv import load_dotenv
load_dotenv()


def get_user_info():
    return {
        'name': 'John Bright Ikechukwu',
        'bvn': os.getenv('BVN', 'N/A'),
        'nin': os.getenv('NIN', 'N/A'),
        'email': os.getenv('EMAIL', 'N/A'),
        'phone': os.getenv('PHONE', 'N/A'),
    }


def login_view(request):
    """Render the password page and validate password on POST.

    Sets `request.session['authenticated'] = True` on success and redirects
    to the dashboard.
    """
    error = ''
    if request.method == 'POST':
        pw = request.POST.get('password', '')
        correct = os.getenv('PASSWORD')
        if correct and pw == correct:
            request.session['authenticated'] = True
            return redirect('dashboard')
        else:
            error = 'Incorrect password. Try again.'
    return render(request, 'login.html', {'error': error})


def dashboard_view(request):
    # require authentication in session
    if not request.session.get('authenticated'):
        return redirect('login')
    user_info = get_user_info()
    return render(request, 'dashboard.html', {'user_info': user_info})


def me(request):
    # Keep old entry point – redirect to login
    return redirect('login')