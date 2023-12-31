from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """ Allows us to add and edit line items in the admin right from inside the order model. """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """ Allows to add and edit orders in the admin. """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county',
              'grand_total', 'original_bag', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name', 'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)