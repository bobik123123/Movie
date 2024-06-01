from rest_framework.routers import DefaultRouter

from . import views



cinematic_routes = DefaultRouter()

cinematic_routes.register(r"top_list", views.MovieList, basename='movie')

cinematic_routes.register(r"janr", views.JanrList)

cinematic_routes.register(r"author", views.AuthourList)