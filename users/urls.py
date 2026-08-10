from django.urls import path

from.views import CustomPasswordChangeView, MyAccountPageView

urlpatterns= [
  path(
    "password/change/", CustomPasswordChangeView.as_view(),
  ),
  path('my-account/', MyAccountPageView.as_view(), name='my-account'),
]