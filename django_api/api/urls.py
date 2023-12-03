from django.urls import path
from . import views

urlpatterns=[
    path('set_ecg_value',views.set_ecg_value),
    path('get_ecg_value',views.get_ecg_value),
    path('compute_total_value',views.compute_total_value),
    path('get_total_value',views.get_total_value),
    path('create_img',views.create_ecg_plot),
    path('get_ecg_plot',views.get_ecg_plot)
]