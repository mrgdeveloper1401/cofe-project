from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from core_app.models import CreateMixin, UpdateMixin
from .validator import MobileRegexValidator


class User(AbstractBaseUser, PermissionsMixin, UpdateMixin, CreateMixin):
    mobile_phone = models.CharField(
        _("mobile phone"), 
        max_length=15,
        unique=True,
        validators=(MobileRegexValidator,)
    )
    username = models.CharField(
        _("username"),
        max_length=150,
        blank=True,
        null=True
    )
    email = models.EmailField(
        _("email address"), 
        blank=True, 
        null=True, 
        # unique=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    birth_date = models.DateField(blank=True, null=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True, null=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True, null=True)
    profile_image = models.ForeignKey(
        "core_app.Media",
        on_delete=models.PROTECT,
        related_name="profile_media",
        blank=True,
        null=True,
    )
    USERNAME_FIELD = 'mobile_phone'
    REQUIRED_FIELDS = ('email', "username", "first_name", "last_name")

    objects = UserManager()

    class Meta:
        ordering = ("-id",)
        db_table = "auth_user"


class State(models.Model):
    name = models.CharField(_("state name"), max_length=150)
    slug = models.SlugField(max_length=150, allow_unicode=True, null=True)
    tel_prefix = models.CharField(max_length=6, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-id',)
        db_table = "state"


class City(models.Model):
    name = models.CharField(_("city name"), max_length=150)
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name="cities")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-id',)
        db_table = "city"


class UserAddress(CreateMixin, UpdateMixin):
    user = models.ForeignKey("User", verbose_name=_("user"), on_delete=models.PROTECT)
    state = models.ForeignKey("state", verbose_name=_("state"), on_delete=models.PROTECT, related_name="user_states")
    city = models.ForeignKey("City", verbose_name=_("city"), on_delete=models.PROTECT, related_name="user_city")
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)

    class Meta:
        ordering = ("-id",)
        db_table = "user_address"
