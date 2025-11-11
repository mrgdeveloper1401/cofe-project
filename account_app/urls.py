from django.urls import path

from .views import (
    LoginPasswordView,
    RequestOtpPhoneView,
    VerifyOypPhoneView,
    ProfileView,
    WellcomeView,
    PersonalProfileView,
    ProfileOrderView,
    ReturnOrderView,
    SuccessOrderProfileView,
    ProfileFavoritView,
    ProfileAddressView
)


app_name = "auth_app"


urlpatterns = [
    path("login_by_password/", LoginPasswordView.as_view(), name="login_by_password"),
    path("request_otp_phone/", RequestOtpPhoneView.as_view(), name="request_otp_phone"),
    path("verify_otp_phone/", VerifyOypPhoneView.as_view(), name="verify_otp_phone"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("personal-profile/", PersonalProfileView.as_view(), name='personal-profile'),
    path("wellcome/", WellcomeView.as_view(), name='wellcome'),
    path("profile-order/", ProfileOrderView.as_view(), name='profile-order'),
    path("return-order/", ReturnOrderView.as_view(), name='return-order'),
    path("success-profile/", SuccessOrderProfileView.as_view(), name='success-profile'),
    path("profile-favorit/", ProfileFavoritView.as_view(), name='profile-favorit'),
    path("profile-address/", ProfileAddressView.as_view(), name='profile-address')
]
