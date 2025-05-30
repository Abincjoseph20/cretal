from django.contrib import admin
from.models import Payment,Order,OrderProduct
# Register your models here.


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment','user','product','quantity','product_price','ordered')
    extra = 0

class OrdreAdmin(admin.ModelAdmin):
    list_display = ['order_number','first_name', 'last_name', 'phone','email','address_line1','address_line2','country', 'state','city','created_at']
    list_filter = ['status','is_ordered']
    search_fields = ['order_number','first_name', 'last_name', 'phone','email']
    list_per_page = 20
    inlines = [OrderProductInline]
    

admin.site.register(Payment)
admin.site.register(Order,OrdreAdmin)
admin.site.register(OrderProduct)


