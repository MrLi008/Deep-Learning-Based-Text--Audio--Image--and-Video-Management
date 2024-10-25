from django import forms

from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(
        label="用　户　名",
        min_length=6,
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "不小于6位包含大小写字母和数字",
                "class": "form-control",
            }
        ),
    )

    password = forms.CharField(
        label="密　　　码",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "不小于6位包含大小写字母和数字",
                "class": "form-control",
            },
            render_value=True,
        ),
        required=True,
    )
    captcha = CaptchaField(label="验　证　码")

    class Meta:
        pass


class RegisterForm(forms.Form):
    username = forms.CharField(
        label="用　户　名",
        min_length=6,
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "不小于6位包含大小写字母和数字",
                "class": "form-control",
            }
        ),
    )
    password1 = forms.CharField(
        label="密　　　码",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "不小于6位包含大小写字母和数字",
                "class": "form-control",
            },
            render_value=True,
        ),
        required=True,
    )
    password2 = forms.CharField(
        label="密　　　码",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "不小于6位包含大小写字母和数字",
                "class": "form-control",
            },
            render_value=True,
        ),
        required=True,
    )

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        pass


class UserCenterForm(forms.Form):
    username = forms.CharField(
        label="用　户　名",
        min_length=6,
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "不小于6位包含大小写字母和数字",
                "class": "form-control",
            }
        ),
    )
    password1 = forms.CharField(
        label="密　　　码",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "不小于6位包含大小写字母和数字",
                "class": "form-control",
            },
            render_value=True,
        ),
        required=True,
    )
    password2 = forms.CharField(
        label="密　　　码",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "不小于6位包含大小写字母和数字",
                "class": "form-control",
            },
            render_value=True,
        ),
        required=True,
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    location = forms.CharField(
        label="地　　　址",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass
