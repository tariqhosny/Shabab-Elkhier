# middleware.py
from django.middleware.csrf import CsrfViewMiddleware
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin

class CustomCsrfViewMiddleware(CsrfViewMiddleware):
    def _reject(self, request, reason):
        return render(request, 'errors.error.html', {'reason': reason})
