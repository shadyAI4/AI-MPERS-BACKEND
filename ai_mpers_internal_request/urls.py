from django.urls import path
from .views import UserVerifierView
from . import routing
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("internal_request",csrf_exempt(routing.MessageChannelsView.as_view())),
    path("user_verifier",csrf_exempt(UserVerifierView.as_view())),
]
