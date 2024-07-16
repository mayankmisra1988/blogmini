from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Post

class SignupForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                 'first_name':forms.TextInput(attrs={'class':'form-control'}),
                 'last_name':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'}),
                }
        error_messages={
            'first_name':{'required':'This field is required. ?'},
            'last_name':{'required':'This field is required. ?'},
            'email':{'required':'This field is required. ?'},
            # 'password':{'required':'Please Fill Your Password ?'},
            # 'mobile':{'required':'Please Fill Your Mobile ?'},
        }
class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_("Password")
    ,strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','desc']
        labels={'title':'Title','desc':'Description'}
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
                 'desc':forms.Textarea(attrs={'class':'form-control'}),
                }

class contactForm(forms.Form):
    Full_name=forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class':'form-control'}))
    email_address=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    content=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    labels={'Full_name':'Full Name','last_name':'Last Name','email':'Email','content':'Messages'}    
    # widgets={'Full_name':forms.TextInput(attrs={'class':'form-control'}),
    #         'last_ame':forms.TextInput(attrs={'class':'form-control'}),
    #         'email':forms.TextInput(attrs={'class':'form-control'}),
    #         'content':forms.EmailInput(attrs={'class':'form-control'}),
    #         }





        