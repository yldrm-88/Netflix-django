from django.contrib import admin
from.models import*
# Register your models here.

class MoviesAdmin(admin.ModelAdmin):
    list_display=["id","filmismi","kategori"] #görüntülenecek yerler bunlar.
    list_display_links=["id"] #üzerine basılan link idye verildi.
    list_filter=["filmismi","kategori"] #filtreleme işlemi yapacaktır.
    list_editable=["filmismi"] #filmi ismini değişebilirsiniz.
    list_per_page=2

admin.site.register(Movies,MoviesAdmin)
admin.site.register(Kategori)
admin.site.register(Izlenenler) 