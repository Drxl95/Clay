from django.shortcuts import render


def listing(request):
    return render(request, 'listing.html')
