from django.urls import path
from . import views
urlpatterns = [
    path('big/<int:pk>', views.product_view1().as_view(), name = 'tests'),
    path('small/',views.product_view2.as_view(), name = 'test_name'),
]