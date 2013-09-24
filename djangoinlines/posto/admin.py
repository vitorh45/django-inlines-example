from django.contrib import admin
from djangoinlines.nested_inlines.admin import NestedModelAdmin, NestedTabularInline, NestedStackedInline

from .models import Posto, Bomba, Bico

class BicoInline(NestedTabularInline):
    model = Bico
    extra = 1

class BombaInline(NestedTabularInline):
    model = Bomba
    extra = 1
    inlines = [BicoInline,]
    
class PostoAdmin(NestedModelAdmin):
    inlines = [BombaInline,]

admin.site.register(Posto, PostoAdmin)
