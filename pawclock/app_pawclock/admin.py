from django.contrib import admin

from .models import Pet, Owner

class PetsInline(admin.TabularInline):
    model = Pet.owners.through
    extra = 1
    verbose_name = "Pet"
    verbose_name_plural = "Pets"
    max_num = 10
    min_num = 1
    can_delete = True
    show_change_link = True


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name']
    list_per_page = 15
    empty_value_display = '-empty-'


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):

    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['first_name', 'last_name']
    list_per_page = 15
    empty_value_display = '-empty-'
    inlines = [PetsInline]


admin.site.site_header = "Pawclock Admin"
admin.site.site_title = "Pawclock Admin Portal"
admin.site.index_title = "Welcome to Pawclock Admin"
admin.site.site_url = "https://pawclock.com"
