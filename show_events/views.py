from datetime import datetime
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Events, Categories


# Admin home page
class HomeAdmin(View):
    def get(self, request):
        data = {}
        events = Events.objects.filter(end_Date__gte=datetime.now(), published = True)       
        categories = Categories.objects.all()

        # Creating paginator object
        paginator_object = Paginator(events, 1)
        # getting the desired page number from url
        page_number = request.GET.get('page')
        try:
            page_object = paginator_object.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_object = paginator_object.page(1)
        except EmptyPage:
            # if page is empty then return last page
            page_object = paginator_object.page(paginator_object.num_pages)

        data['page_object'] = page_object
        data['categories'] = categories
       

        return render(request, 'home_admin.html', data)
        

# User home page
class HomeUser(View):
    def get(self, request):
        return render(request, 'home_user.html')