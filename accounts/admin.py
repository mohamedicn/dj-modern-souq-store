from django.contrib import admin
from.models import Profile

# Register your models here.

# class ProfileAdmin(admin.ModelAdmin):
#     # def get_readonly_fields(self, request, obj=None):
#     #     if obj:
#     #         return ['password1']
#     #     else:
#     #         return []
#     def change_view(self, request, object_id, extra_context=None):       
#         self.exclude = ('user','slug',)
#         return super(ProfileAdmin, self).change_view(request, object_id, extra_context)

admin.site.register(Profile)