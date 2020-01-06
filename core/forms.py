from django import forms, ModelForm
from django.contrib.auth.models import User
from .models import Room, Reservation

class SingleRoomForm(forms.ModelForm):
	class Meta:
		model = Room
		fields= [
			"name",
			"surname",
			"email",
			"arrival_date",
			"departure_date",
		]
		widgets = {
			'arrival_date': forms.SelectDateWidget(),
			'departure_date': forms.SelectDateWidget(),
		}

	
class RoomForm(forms.ModelForm):
	class Meta:
		model = Room
		fields= [
			"name",
			"surname",
			"email",
			"arrival_date",
			"departure_date",
		] 

		widgets = {
			'arrival_date': forms.SelectDateWidget(),
			'departure_date': forms.SelectDateWidget(),
		}    

    
class CheckAvailability(forms.ModelForm):
	class Meta:
		model = Room
		fields = [
			"room_type",
			"arrival_date",
			"departure_date",
		]
		widgets = {
			'arrival_date': forms.SelectDateWidget(),
			'departure_date': forms.SelectDateWidget(),
		}
		
		
class ConfirmForm(object):
	class Meta:
		model = Reservation
		fields = [
			" check_in",
			" check_out",
		]

						