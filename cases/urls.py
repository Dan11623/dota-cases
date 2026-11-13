from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('case/<int:case_id>/', views.case_detail, name='case_detail'),
    path('case/<int:case_id>/open/', views.open_case, name='open_case'),
]
