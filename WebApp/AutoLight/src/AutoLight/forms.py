from django import forms

class ComplaintForm(forms.Form):
	fullname = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class":"form-control",
				"id":"form_full_name",
				"placeholder":"Your full name please."
			}
		)
	)
	nearest_location = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class":"form-control",
				"placeholder":"Where is the light affected ? Nearest location please."
			}
		)
	)
	complaint = forms.CharField(
		widget=forms.Textarea(
			attrs={
				"class":"form-control",
				"placeholder":"Fill your complaint here please."
			}
		)
	)

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(
			attrs={
				"class":"form-control form-group",
				"id":"form_full_name"
			}
		)
	)
	
	password = forms.CharField(
		widget=forms.PasswordInput(
		attrs={
				"class":"form-control form-group"
			}
		)
	)