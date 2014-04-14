from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import User
from hackaglobal.models import Event, Staff
from hackacities.models import HackaCity
import datetime


class EventCreationForm(forms.ModelForm):
    error_messages = {
          'invalid_address': _("Please provide a valid address.")
        , 'invalid_start_date': _("Start date must be later than today")
        , 'invalid_end_date': _("End date must be later than start date")
        }

    class Meta:
        model = Event

    def clean_start(self):
        start_date = self.cleaned_data.get("start")
        if not start_date:
            raise forms.ValidationError('Start Date cannot be empty')
        today = datetime.datetime.now()
        if start_date < today:
            raise forms.ValidationError(self.error_messages['invalid_start_date'])
        return start_date

    def clean_end(self):
        start_date = self.cleaned_data.get("start")
        if not start_date:
            raise forms.ValidationError('Please fix start date')
        end_date = self.cleaned_data.get("end")
        if end_date < start_date:
            raise forms.ValidationError(self.error_messages['invalid_end_date'])
        return end_date

    def save(self, commit=True):
        event = super(EventCreationForm, self).save(commit=False)
        if commit:
            event.save()
        return event

class EFUserCreationForm(forms.ModelForm):
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
        }
    username = forms.RegexField(label=_("Username"), max_length=30,
        regex=r'^[a-zA-Z.-_]+@[a-zA-Z]+\.[a-zA-Z]+$',
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                    "@/./+/-/_ only."),
        error_messages={
            'invalid': _("The email must be a valid address.")})

    first_name = forms.RegexField(label=_("First Name"), max_length=30,
                    regex=r'^[a-zA-Z]+$',
                    help_text=_("Required. 30 characters or fewer. Letters only."),
                    error_messages={'invalid': _("This value may contain only letters.")})

    last_name = forms.RegexField(label=("Last Name"), max_length=30,
                    regex=r'^[a-zA-Z]+$',
                    help_text=_("Required. 30 characters or fewer. Letters only."),
                    error_messages={'invalid': _("This value may contain only letters.")})

    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput, max_length=20)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        max_length=20,
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username","first_name","last_name")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        user = super(EFUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class EFPasswordChangeForm(forms.Form):

    error_messages = {
            'invalid_password': _("Your password is invalid, please try again."),
        }

    old_password = forms.CharField(label=_("Old Password"),
        widget=forms.PasswordInput, max_length=20)

    new_password = forms.CharField(label=_("New Password"),
        widget=forms.PasswordInput, max_length=20)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(EFPasswordChangeForm, self).__init__(*args, **kwargs)

    def clean_new_password(self):
        password = self.cleaned_data.get("old_password")
        if not self.user.check_password(password):
            raise forms.ValidationError(self.error_messages['invalid_password'])

        return self.cleaned_data.get("new_password")

    def save(self, commit=True):
        if self.user.check_password(self.cleaned_data["old_password"]):
            self.user.set_password(self.cleaned_data["new_password"])
        if commit:
            self.user.save()
        return self.user


class EFUserEditForm(forms.Form):

    first_name = forms.RegexField(label=_("First Name"), max_length=30,
        regex=r'^[a-zA-Z]+$',
        help_text=_("Required. 30 characters or fewer. Letters only."),
        error_messages={'invalid': _("This value may contain only letters.")})

    last_name = forms.RegexField(label=("Last Name"), max_length=30,
        regex=r'^[a-zA-Z]+$',
        help_text=_("Required. 30 characters or fewer. Letters only."),
        error_messages={'invalid': _("This value may contain only letters.")})

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(EFUserEditForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        self.user.first_name = self.cleaned_data["first_name"]
        self.user.last_name = self.cleaned_data["last_name"]
        if commit:
            self.user.save()
        return self.user

class HackaCityCreationForm(forms.ModelForm):

    class Meta:
        model = HackaCity
        exclude = ("city","name","lead")

    def save(self, commit=True):
        hc = super(HackaCityCreationForm, self).save(commit=False)
        if commit:
            hc.save()
        return hc