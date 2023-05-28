from .models import *
from django import forms
from django.forms import ModelForm
from .models import SentimentModel


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets={
                   "name":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "phone":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "email":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "address":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                }  

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        widgets={
                   "text": forms.Textarea(attrs={'class': "form-control form-control-md"}),
                }

class Form(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets={
                   "product":forms.Select(attrs={'class': "form-control form-control-sm"}),
                   "customer":forms.Select(attrs={'class': "form-control form-control-sm"}),
                   "status":forms.Select(attrs={'class': "form-control form-control-sm"}),
                }  


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets={
                   "name":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "product":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "vendor":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "discount":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "cost":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                }


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'
        widgets={
                   "name":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "phone":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "priority":forms.Select(attrs={'class': "form-control form-control-sm"}),
                   "cust_probability":forms.Select(attrs={'class': "form-control form-control-sm"}),
                }


class SentimentForm(forms.ModelForm):
    Sentence = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = SentimentModel
        fields = [
            'Sentence'
        ]