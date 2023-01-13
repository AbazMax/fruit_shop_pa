from django import forms
from .models import Order
from django.utils.translation import get_language

class OrderCreateForm(forms.ModelForm):

    """Creating order form"""

    name = forms.CharField(
        max_length=100
    )

    email = forms.CharField(
        max_length=50
    )

    address = forms.CharField(
        max_length=500
    )

    phone = forms.CharField(
        max_length=15
    )

    shipping_address = forms.CharField(
        max_length=500
    )

    comment = forms.CharField(
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
            translate_text['ph_phone'] = 'Phone in format xxx xxx xxxx'
            translate_text['ph_billing_address'] = 'Billing address'
            translate_text['ph_shipping_address'] = 'Shipping address'
            translate_text['ph_comment'] = 'Comment'
        elif current_lng == 'uk':
            translate_text['ph_name'] = 'Імʼя'
            translate_text['ph_email'] = 'Електронна адреса'
            translate_text['ph_phone'] = 'Телефонний номер у форматі xxx xxx xxxx'
            translate_text['ph_billing_address'] = 'Адреса для виставлення рахунку'
            translate_text['ph_shipping_address'] = 'Адреса доставки'
            translate_text['ph_comment'] = 'Коментар'
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
        self.fields['phone'].widget=forms.TextInput(attrs={
            'type': 'tel',
            'placeholder': translate_text.get('ph_phone', ''),
            'name': 'phone',
            'id': 'phone',
            'required pattern': '^(\d{3}[- .]?){2}\d{4}$'
        })
        self.fields['address'].widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': translate_text.get('ph_billing_address', ''),
        })
        self.fields['shipping_address'].widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': translate_text.get('ph_shipping_address', ''),
        })
        self.fields['comment'].widget=forms.Textarea(attrs={
            'name': 'bill',
            'id': 'bill',
            'cols': '30',
            'rows': '10',
            'placeholder': translate_text.get('ph_comment', ''),
        })

    class Meta:
        model = Order
        fields = ['name', 'email', 'address', 'phone', 'shipping_address', 'comment']
