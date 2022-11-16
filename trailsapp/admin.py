from django.contrib import admin
from .models import trail_id, trail_name, length_miles, difficulty, completion_time, img_url, description, location

# Register your models here.
admin.site.register(trail_id)
admin.site.register(trail_name)
admin.site.register(length_miles)
admin.site.register(difficulty)
admin.site.register(completion_time)
admin.site.register(img_url)
admin.site.register(description)
admin.site.register(location)