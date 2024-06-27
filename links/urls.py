from django.urls import path

from .views import index, route_link, new_link

urlpatterns = [
    path("", index, name="home"),
    path("<str:link_slug>", route_link),
    path("new/", new_link, name="new-link")
]
