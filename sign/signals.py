from sign.models import SignModel,SignalModel
from django.db.models.signals import post_save,pre_save,pre_delete,post_delete
from django.dispatch import receiver


@receiver(post_save, sender = SignModel)
def create_sign(sender, instance, created, **kwargs):
    if created:
        print(instance)
        print("000000000000000000000")
        SignalModel.objects.create(product=instance)
        print("Product Created.....")

post_save.connect(create_sign,sender=SignModel)