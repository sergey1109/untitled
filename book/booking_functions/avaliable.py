import datetime
from book.models import H_book,Booking

def  check_aviability(h_ranks, check_in,check_out):
    aviability_list = []
    booking_list =  Booking.objects.filter(h_ranks=h_ranks)
    for booking in booking_list:
        if booking.chek_in > check_out or booking.chek_out < check_in:
            aviability_list.append(True)
        else:
            aviability_list.append(False)
    return all(aviability_list)
