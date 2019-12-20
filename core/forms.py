from django import forms
from django.contrib.auth.models import User
from .models import SingleRoom


class SingleRoomForm(forms.ModelForm):
	class Meta:
		model = SingleRoom
		fields= [
			"name",
			"surname",
			"email",
			"arrival_date",
			"departure_date",
		]
		
            
    

		