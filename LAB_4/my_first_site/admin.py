from django.contrib import admin

# Register your models here.

from my_first_site.models import Topic, Entry, Successes

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Successes)
