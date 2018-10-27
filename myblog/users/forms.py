from django import forms
from django.forms import fields

class UserRegisterForm(forms.Form):
    username =fields.CharField(max_length=18,min_length=2,error_messages={'required':'用户名必须填写',
                                                                          'max_length':'用户名不能超过18位',
                                                                          'min_length':'用户名不能少于2位'})
    password =fields.CharField(max_length=18,min_length=6,error_messages={'required':'密码必须填写',
                                                                          'max_length':'密码不能超过18位',
                                                                          'min_length':'密码不能少于6位'})
    password1 =fields.CharField(max_length=18,min_length=6,error_messages={'required':'确认密码必须填写',
                                                                          'max_length':'确认密码不能超过18位',
                                                                            'min_length':'确认密码不能少于6位'})

class UserLoginForm(forms.Form):
        username = fields.CharField(max_length=18, min_length=2, error_messages={'required': '用户名必须填写',
                                                                                 'max_length': '用户名不能超过18位',
                                                                                 'min_length': '用户名不能少于2位'})
        password = fields.CharField(max_length=18, min_length=6, error_messages={'required': '密码必须填写',
                                                                                 'max_length': '密码不能超过18位',})
