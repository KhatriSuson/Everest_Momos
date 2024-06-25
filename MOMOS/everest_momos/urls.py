from django.urls import path
from everest_momos.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]