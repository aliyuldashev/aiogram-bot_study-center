from django.urls import path
from . import views
urlpatterns = [
    path('first/', views.product_view.as_view(), name = 'agent'),
    path('second/<int:pk>/', views.secand_view.as_view(), name = 'product'),
    path('last/',views.video_view.as_view()),
    path('post/<int:pk>/',views.post_ser_view.as_view())
]