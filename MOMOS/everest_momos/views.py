from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class IndexView(View):
    def get(self, request, *args):

        context = {
            'title': "Welcome tho momo shop",
        }

        return render(request, 'index.html', context)
