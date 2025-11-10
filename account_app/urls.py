from django.urls import path

from .views import (
    LoginPasswordView,
    RequestOtpPhoneView,
    VerifyOypPhoneView,
    ProfileView,
    WellcomeView
)


app_name = "auth_app"


urlpatterns = [
    path("login_by_password/", LoginPasswordView.as_view(), name="login_by_password"),
    path("request_otp_phone/", RequestOtpPhoneView.as_view(), name="request_otp_phone"),
    path("verify_otp_phone/", VerifyOypPhoneView.as_view(), name="verify_otp_phone"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("wellcome/", WellcomeView.as_view(), name='wellcome'),
]
