from django.shortcuts import render

def handler404(request, exception):
    context = {}
    response = render(request, "404.html", context=context)
    response.status_code = 404
    return response

def handler500(request):
    context = {}
    response = render(request, "500.html", context=context)
    response.status_code = 500
    return response