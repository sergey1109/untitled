from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View
from django.urls import reverse
from .booking_functions.avaliable import check_aviability
from .forms import AvaliablityForm
from .models import H_book, Booking


# Create your views here.


def home(request):
    all_hotels = H_book.objects.all()
    for hotel in all_hotels:
        print('title', hotel.title)
    return render(request, 'index.html',
                  {'hotels': all_hotels}
                  )


def RoomListView(request):
    h_ranks = H_book.objects.all()[0]
    room_categories = dict(h_ranks.HOTEL_RANK_STARS)
    #print('categories= ', room_categories)

    room_values = room_categories.values()
    #print('categories= ', room_values)

    room_list = []
    for room_category in room_categories:

        h_ranks = room_categories.get(room_category)
        room_url = reverse('book:RoomDetailView',kwargs={
           'ranks':room_category,
        })

        room_list.append((h_ranks,room_url))
    ctx = {
        'room_list':room_list,
    }

    return render(request, 'room_list_view.html', ctx)


class BookingList(ListView):
    model = Booking

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list


class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        ranks = self.kwargs.get('ranks', None)
        form = AvaliablityForm()
        room_list = H_book.objects.filter(ranks=ranks)

        if len(room_list) > 0:
            h_ranks = room_list[0]
            room_category = dict(h_ranks.HOTEL_RANK_STARS).get(h_ranks.ranks, None)

            ctx = {
                'room_category': room_category,
                'form': form,
            }
            return render(request, 'room_detail_view.html', ctx)
        else:
            return HttpResponse('Category does not exist')

    def post(self, request, *args, **kwargs):
        ranks = self.kwargs.get('ranks', None)
        room_list = H_book.objects.filter(ranks=ranks)
        form = AvaliablityForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

        avaliabile_rooms = []
        for h_ranks in room_list:
            if check_aviability(h_ranks, data['check_in'], data['check_out']):
                avaliabile_rooms.append(h_ranks)

        if len(avaliabile_rooms) > 0:
            h_ranks = avaliabile_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,
                h_ranks=h_ranks,
                chek_in=data['check_in'],
                chek_out=data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('This category of rooms are booked!Try another one')


class BookingView(FormView):
    form_class = AvaliablityForm
    template_name = 'avaliability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = H_book.objects.filter(ranks=data['room_category'])
        avaliabile_rooms = []
        for h_ranks in room_list:
            if check_aviability(h_ranks, data['check_in'], data['check_out']):
                avaliabile_rooms.append(h_ranks)

        if len(avaliabile_rooms) > 0:
            h_ranks = avaliabile_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,
                h_ranks=h_ranks,
                chek_in=data['check_in'],
                chek_out=data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('This category of rooms are booked!Try another one')
