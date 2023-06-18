from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.db.models import Count,Max,Min,Avg,Sum, Value, F, Func
from django.db.models.functions import Concat
from store.models import Product, OrderItem, Customer,Collection





def say_hello(request):
        # sorting
        # query_set = Product.objects.filter(unit_price__range = (20,30))
        #query_set = Product.objects.order_by('title')
        #query_set = Product.objects.order_by('-title')
        # query_set = Product.objects.order_by('unit_price','-title')
        #query_set = Product.objects.order_by('unit_price')[0]
        #query_set = Product.objects.filter(collection__title='john').order_by('unit_price')
        # query_set = Product.objects.latest('unit_price')
        # limiting results
        #query_set = Product.objects.all()[:15]
        #query_set = Product.objects.all()[5:15]
      #  query_set = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
      # Aggregate functions
      #   result = Product.objects.aggregate(Count('id'))
      #   result = Product.objects.aggregate(count=Count('id'), max= Max('unit_price'))
        # Annotations
       # result = Customer.objects.annotate(new_id = F('id')+1)
        #calling Dastabase functions
        # result = Customer.objects.annotate(
        #         full_name= Func(F('first_name'), Value(' '), F('last_name'), function = 'CONCAT')
        # )
        #result = Customer.objects.annotate(Full_name= Concat('first_name', Value(' '), 'last_name'))
        #result = Customer.objects.annotate(order_items = Count('order'))
        # collection = Collection()
        # collection.title = 'videogames'
        collection = Collection.objects.create(title = 'videogames')
        return render(request, 'hello.html', {'name': 'Mosh','result': collection})
