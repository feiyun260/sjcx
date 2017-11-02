# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2017-10-17 下午 11:11
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()