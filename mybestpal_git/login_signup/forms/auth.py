from django import forms



class SignUpForm(forms.Form):


    username = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'})
    )

    password = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )
    phno = forms.CharField(
        max_length=75,

        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phno'})
    )
    email = forms.CharField(
        max_length=75,

        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email id'})
    )
    dob=forms.DateField(


        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter dob'})
    )



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'})
    )

    password = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'})
    )