from .models import Experience, Resume
from django import forms
from .widgets import CustomClearableFileInput
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already registered.')
        return email

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

class ResumeForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=CustomClearableFileInput())

    class Meta:
        model = Resume
        fields = ['image', 'name', 'email', 'telephone', 'linkedin', 'github',
                  'website', 'description', 'career_summary', 'template']
        widgets = {
            'career_summary': CKEditorWidget(config_name='CVBuilder_Config')
        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'company', 'duration', 'text', 'tech']
        widgets = {
            'text': CKEditorWidget(config_name='CVBuilder_Config'),
        }