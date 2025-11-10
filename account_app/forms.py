from django import forms


class LoginPasswordForm(forms.Form):
    phone = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RequestOtpPhoneForm(forms.Form):
    phone = forms.CharField()


class VerifyOtpPhoneForm(forms.Form):
    code = forms.CharField()
