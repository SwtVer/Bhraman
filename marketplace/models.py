from django.db import models
from accounts.models import User
from menu.models import PackageItem

# Create your models here.


## maybe we should include booking date here-abhishek
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    packageitem = models.ForeignKey(PackageItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user