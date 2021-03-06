from django import forms
from django.contrib.auth import authenticate
from .models import Account


class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('username', 'password')

	def clean(self):
		if self.is_valid():
			username = self.cleaned_data['username']
			password = self.cleaned_data['password']
			try:
				Account.objects.exclude(pk=self.instance.pk).get(username=username)
			except Account.DoesNotExist:
				raise forms.ValidationError("Nom d'utilisateur invalide")

			if not authenticate(username=username, password=password):
				raise forms.ValidationError("Mot de passe invalide")


class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = Account
		fields = ('username', 'email', 'alias', 'profile_picture')

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
		except Account.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	def save(self, commit=True):
		account = self.instance
		account.username = self.cleaned_data['username']
		account.email = self.cleaned_data['email']
		account.alias = self.cleaned_data['alias']


		if self.cleaned_data['profile_picture']:
			account.profile_picture = self.cleaned_data['profile_picture']

		if commit:
			account.save()
		return account
