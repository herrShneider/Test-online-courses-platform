from django.contrib import admin
from django.contrib.auth.models import Group

from .models import CustomUser


admin.site.unregister(Group)


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'id',
        'username',
        'first_name',
        'last_name',
    )
    list_filter = (
        'email',
        'username',
    )
    fields = (
        'email',
        'username',
        'first_name',
        'last_name',
    )
    #
    # @admin.display(description='Кол-во рецептов')
    # def recipes_count(self, obj):
    #     return obj.recipes.count()
    #
    # @admin.display(description='Кол-во подписчиков')
    # def subscribers_count(self, obj):
    #     return obj.subscription_as_author.count()
