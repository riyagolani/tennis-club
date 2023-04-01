from django import forms
from members.models import Member


# Create your forms here.
class MemberForm(forms.ModelForm):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100, widget=forms.PasswordInput)
	email = forms.CharField(widget=forms.EmailInput)
	firstname = forms.CharField(max_length=100)
	lastname = forms.CharField(max_length=100)
	proficiency = forms.ChoiceField(choices=[("1", "Beginner"), ("2", "Intermediate"), ("3", "Expert")])
	age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={"style": 'width: 7%'}))
	address = forms.CharField(widget=forms.Textarea(attrs={"rows": 2, "cols": 40}), required=False)
	contact = forms.CharField(max_length=10, required=False)

	class Meta:
		model = Member
		fields = ("username", "password", "email", "firstname", "lastname", "proficiency", "age", "address", "contact")

	def save(self):
		member = super(MemberForm, self).save()
		return member


class LoginForm(forms.ModelForm):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100, widget=forms.PasswordInput)

	class Meta:
		model = Member
		fields = ("username", "password")