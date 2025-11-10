from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from account_app.forms import (
    LoginPasswordForm,
    RequestOtpPhoneForm,
    VerifyOtpPhoneForm
)


class LoginPasswordView(View):
    template_name = 'auth/login_password.html'
    form_class = LoginPasswordForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        pass


class RequestOtpPhoneView(View):
    template_name = "auth/request_otp_phone.html"
    form_class = RequestOtpPhoneForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class()
        if form.is_valid():
            # get phone
            phone = form.cleaned_data['phone']
            # check user and create user
            # send sms into phone
        return render(request, self.template_name, {'form': form})


class VerifyOypPhoneView(View):
    template_name = "auth/verify_otp_phone.html"
    form_class = VerifyOtpPhoneForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        pass


class ProfileView(View):
    template_name = "partials/profile/profile.html"

    def get(self, request):
        return render(request, self.template_name)


class WellcomeView(TemplateView):
    template_name = "auth/wellcome.html"
