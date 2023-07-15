from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.db.models import Count, Max, Min, Avg, Sum, Value, F, Func
from django.db.models.functions import Concat
# from store.models import Product, OrderItem, Customer,Collection
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers
import requests
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

class HelloView(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
        return render(request, 'hello.html', {'name':'Naga'})

# function based cache
# @cache_page(60)
# def say_hello(request):
#     response = requests.get('https://httpbin.org/delay/2')
#     data = response.json()
#     return render(request, 'hello.html', {'name':'Naga'})


#Internal Working of Cache
# def say_hello(request):
#     key = 'httpbin_result'
#     if cache.get(key) is None:
#         response = requests.get('https://httpbin.org/delay/2')
#         data = response.json()
#         cache.set(key,data)
#     # notify_customers.delay('Messages sending task will complete shortly. Please wait.....')
#     return render(request, 'hello.html', {'name': cache.get(key)})

    # sorting
    # query_set = Product.objects.filter(unit_price__range = (20,30))
    # query_set = Product.objects.order_by('title')
    # query_set = Product.objects.order_by('-title')
    # query_set = Product.objects.order_by('unit_price','-title')
    # query_set = Product.objects.order_by('unit_price')[0]
    # query_set = Product.objects.filter(collection__title='john').order_by('unit_price')
    # query_set = Product.objects.latest('unit_price')
    # limiting results
    # query_set = Product.objects.all()[:15]
    # query_set = Product.objects.all()[5:15]
#  query_set = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
# Aggregate functions
#   result = Product.objects.aggregate(Count('id'))
#   result = Product.objects.aggregate(count=Count('id'), max= Max('unit_price'))
# Annotations
# result = Customer.objects.annotate(new_id = F('id')+1)
# calling Dastabase functions
# result = Customer.objects.annotate(
#         full_name= Func(F('first_name'), Value(' '), F('last_name'), function = 'CONCAT')
# )
# result = Customer.objects.annotate(Full_name= Concat('first_name', Value(' '), 'last_name'))
# result = Customer.objects.annotate(order_items = Count('order'))
# collection = Collection()
# collection.title = 'videogames'
# collection = Collection.objects.create(title = 'videogames')
# Send mail function
# try:
#         # mail_admins('This is a Admin mail','This is a Body of Admin mail',html_message='<h2>This is a HTML message</h2>')
#         # send_mail('This is my mail','this is the body','info@nagapavan.com',['bob@moshbuy.com','test@domain.com'])
#         # message = EmailMessage('THis is a attachment mail','This is a body of attachement mail','fromnaga.pavanfile.com',['recievenaga.pavanfile.com'],['kts@vas18.com'])
#         # message.attach_file('playground\\static\\images\\tiger.jpg')
#         # message.send()
#         message = BaseEmailMessage(
#                 context={'name':'Naga'},
#                 template_name='emails/hello.html'
#         )
#
#         message.send(['john@pavan.com'])
#
# except BadHeaderError:
#         pass
