from django.contrib import admin

from mail.models import Mail

@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    fields = ('id', 'email', 'subject', 'message', 'from_email', 'is_mass', 'created_at', )
    list_display = ('id', 'subject', 'from_email', 'is_mass', 'created_at', )
    list_display_links = ('id', 'subject', 'is_mass', 'created_at',)
    list_filter = ('is_mass', 'created_at',)
    readonly_fields = ('created_at',)
    empty_value_display = '-пустой-'
    list_per_page = 64
    list_max_show_all = 8
    search_fields = ['subject', 'is_mass', 'email', 'message']
