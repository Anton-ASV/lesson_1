from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError
# Create your views here.

def main_view(request):
    return render(request, 'tour/index.html')

def departure_view(request,departure):
    context = {"departure" : str}
    return render(request, 'tour/departure.html', context=context)

def tour_view(request, id ):
    context = {"id": id}
    return render(request, 'tour/tour.html', context=context)

def custom_handler404(request, exception):
    # Call when Http404 raised
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    # Call when raised some python exception
    return HttpResponseServerError('Ошибка сервера!')