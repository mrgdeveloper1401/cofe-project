from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class MobileRegexValidator(RegexValidator):
    regex = r'^09\d{9}'
    message = _("phone must be start 09 and eleven digits")
