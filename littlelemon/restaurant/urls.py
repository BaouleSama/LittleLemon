from django.urls import path, include
from . import views

from rest_framework.authtoken.views import obtain_auth_token

# User rest_framework route.
# Eliminate the need of creating root path
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r"tables", views.BookingSet)

urlpatterns = [
    # add the rest_framework routr the partterns
    path('booking/', include(router.urls)),

    path("", views.index, name='index'),
    path("menu/", views.MenuItemsView.as_view()),
    path("menu/<int:pk>", views.SingleMenuView.as_view()),

    path('api-token-auth/', obtain_auth_token)

]
