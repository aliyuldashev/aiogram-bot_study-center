from django.urls import path
from . import views
urlpatterns = [
    path('big/', views.product_view.as_view(), name = 'agent'),
    path('second/', views.secand_view.as_view(), name = 'product'),
    path('video/',views.video_view.as_view())
]