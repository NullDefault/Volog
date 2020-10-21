from django.contrib import admin

from auth_backend.modules.user.models import BaseVologUser, Referral

models = [BaseVologUser, Referral]

for model in models:
    admin.site.register(model)
