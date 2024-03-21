from django.urls import path, include
from . import views

# User rest_framework route.
# Eliminate the need of creating root path
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r"tables", views.BookingSet)

urlpatterns = [
    # add the rest_framework routr the partterns
    path("", include(router.urls)),
    path('restaurant/booking/', include(router.urls)),

    path("", views.index, name='index'),
    path("menu/", views.MenuItemsView.as_view()),
    path("menu/<int:pk>", views.SingleMenuView.as_view()),

]
