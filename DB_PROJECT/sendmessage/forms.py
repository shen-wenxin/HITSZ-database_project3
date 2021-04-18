
from django import forms

class MessageForm(forms.Form):
    reciever_id = forms.CharField(label="接收者编号", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    theme = forms.CharField(label="主题", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label = "私信内容", max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control','rows':'8'}))


class RecallMessageForm(forms.Form):
    theme = forms.CharField(label="主题", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label = "私信内容", max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control'}))
