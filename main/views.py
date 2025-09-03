from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406355136',
        'name': 'Bisma Zharfan SW',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)