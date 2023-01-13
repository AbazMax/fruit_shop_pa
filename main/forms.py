from django import forms
from .models import UserMessage
from django.utils.translation import get_language

class UserMessage(forms.ModelForm):
    name = forms.CharField(
        max_length=50
    )

    email = forms.CharField(
        max_length=50,
    )

    phone = forms.CharField(
        max_length=15,
    )

    subject = forms.CharField(
        max_length=200
    )

    message = forms.CharField(
        max_length=1000
    )

    @staticmethod
    def _translate():
        """ Translating placeholders in forms"""
        current_lng = get_language()
        translate_text = {}
        if current_lng == 'en':
            translate_text['ph_name'] = 'Name'
            translate_text['ph_email'] = 'Email'
            translate_text['ph_subject'] = 'Subject'
            translate_text['ph_message'] = 'Message text'
            translate_text['ph_phone'] = 'Phone in format xxx xxx xxxx'
        elif current_lng == 'uk':
            translate_text['ph_name'] = 'Імʼя'
            translate_text['ph_email'] = 'Електронна адреса'
            translate_text['ph_subject'] = 'Тема повідомлення'
            translate_text['ph_message'] = 'Текст повідомлення'
            translate_text['ph_phone'] = 'Телефонний номер у форматі xxx xxx xxxx'
        return translate_text

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        translate_text = self._translate()
        self.fields['name'].widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': translate_text.get('ph_name', ''),
            'name': 'name',
            'id': 'name',
        })
        self.fields['email'].widget=forms.TextInput(attrs={
            'type': 'email',
            'placeholder': translate_text.get('ph_email', ''),
            'name': 'email',
            'id': 'email'
        })
        self.fields['subject'].widget = forms.TextInput(attrs={
            'type': 'text',
            'placeholder': translate_text.get('ph_subject', ''),
            'name': 'subject',
            'id': 'subject'
        })
        self.fields['message'].widget = forms.Textarea(attrs={
            'name': 'message',
            'id': 'message',
            'cols': '30',
            'rows': '10',
            'placeholder': translate_text.get('ph_message', '')
        })
        self.fields['phone'].widget=forms.TextInput(attrs={
            'type': 'tel',
            'placeholder': translate_text.get('ph_phone', ''),
            'name': 'phone',
            'id': 'phone',
            'required pattern': '^(\d{3}[- .]?){2}\d{4}$'
        })


    class Meta:
        model = UserMessage
        fields = ('name', 'phone', 'email', 'subject', 'message')

