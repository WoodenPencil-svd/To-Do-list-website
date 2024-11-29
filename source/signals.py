from source.models import CustomUser

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=CustomUser)
def set_user_permission(sender,instance,created, **kwargs):
    instance.set_permission(instance)
