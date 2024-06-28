# middleware.py
from django.shortcuts import redirect

class ClearPostOnReloadMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.method == 'POST' and not request.POST:
            return redirect(request.path_info)

        return response
