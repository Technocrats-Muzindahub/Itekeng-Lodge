from django.shortcuts import render
from . import forms
from .models import SingleRoom

# Create your views here.
def homepage(request):
	return render(request, "home.html", {})


def bookings(request):
	return render(request, "bookings2.html", {})

def singleview(request):
	form = forms.SingleRoomForm(request.POST or None)
	price = 500

	if form.is_valid():
		instance = form.save(commit=False)
		reservation_days = instance.departure_date - instance.arrival_date
		price_duration = price * reservation_days.days


		if instance.arrival_date in models.SingleRoom.values("arrival_date"):
			SingleRoom.num_of_rooms -= 1
			if SingleRoom.num_of_rooms == 0:
				context = {
					"form": form,
					"error_message": "The number of rooms have been fully booked for {} \n please try on another date".format(instance.arrival_date)
				}
				instance.delete()
				return render(request, "bookingssingle.html", context)
				
			instance.save()	
			return render(request, "cardverfications.html")

	return render(request, "bookingssingle.html", {"form": form})


