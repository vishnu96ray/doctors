from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

STATUS_CHOICE = ((1, "Registration Completed"), (2, "Account UnderReview"), (3, "Accounts Verified"))
GENDER = ((0,'MALE'), (1, 'FEMALE'), (2, 'OTHER'))
USER_ROLE = ((1, "Super Admin"), (2, "Doctor"), (3, "Patient"))

class Accounts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userdetail")
    parentuser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="parentuser")
    mobile = models.BigIntegerField()
    gender = models.IntegerField(choices=GENDER, default=0)
    dob	= models.DateField(auto_now=False, auto_now_add=False)
    address = models.TextField(null=True, blank=True)
    userstatus = models.IntegerField(choices=STATUS_CHOICE, default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    used_amount = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    skypeid = models.CharField(max_length=100, null=True, blank=True)
    key = models.CharField(max_length=30, null=True, blank=True)
    is_api_enabled = models.BooleanField(default=False)
    #myplan = models.ForeignKey(PaymentPlan, on_delete=models.CASCADE, null=True, blank=True, related_name='myplan')
    userrole = models.IntegerField(choices=USER_ROLE, default=4)

    def __str__(self):
        return str(self.user.username)