from django.urls import path
from Hosting import views

urlpatterns = [
    path("hosting/", views.HostingView.as_view(), name="HostingList"),
    path("videolesson/", views.VideoLesson.as_view(), name="VideoLesson"),
    path("builderOKS/", views.BuilderOKS.as_view(), name="BuilderOKS"),
    path("templates/", views.Template.as_view(), name="Template"),
    path(
        "hosting/approve/<int:pk>/",
        views.ApproveHostingView.as_view(),
        name="ApproveHosting",
    ),
    path(
        "hosting/refuse/<int:pk>/",
        views.RefuseHostingView.as_view(),
        name="RefuseHosting",
    ),
]
