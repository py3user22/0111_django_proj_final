from django.shortcuts import render


def home(request):
    return render(request, '0111_final_proj_notes.html', {})