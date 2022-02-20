from django.shortcuts import render


# Create your views here.

def main_view(request):
    return render(request, 'tour/index.html')

def departure_view(request,departure):
    context = {"departure" : str}
    return render(request, 'tour/departure.html', context=context)

def tour_view(request, id ):
    context = {"id": id}
    return render(request, 'tour/tour.html', context=context)
