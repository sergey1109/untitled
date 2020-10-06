from django.urls import path , include 
from .views import RoomListView as RLV, BookingList as BL,home as H, BookingView as BW,RoomDetailView as RDV

app_name = 'book'

urlpatterns = [
    path('', H ,name='RoomList'),
    path('room_list/', RLV ,name='RoomList'),
    path('booking_list/', BL.as_view(template_name='book/booking_list.html') ,name='BookingList'),
    path('book/', BW.as_view(template_name='avaliability_form.html') ,name='BookingView'),
    path('room/<str:ranks>', RDV.as_view() ,name='RoomDetailView'),

]