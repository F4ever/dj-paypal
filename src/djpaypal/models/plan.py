from django.contrib.auth.models import User
from django.db import models

from src.djpaypal import enums
from src.djpaypal.models.base import PaypalObject


class Product(PaypalObject):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=127)
    type = models.CharField(max_length=20)
    category = models.CharField(max_length=20)

    image_url = models.CharField(max_length=20)
    home_url = models.CharField(max_length=20)

    create_time = models.DateTimeField(db_index=True, editable=False)
    update_time = models.DateTimeField(db_index=True, editable=False)


class Plan(PaypalObject):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=127)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    usage_type = models.CharField(max_length=20, choices=enums.BillingPlanType.choices)
    status = models.CharField(max_length=20, choices=enums.BillingPlanState.choices)

    create_time = models.DateTimeField(db_index=True, editable=False)


class Subscription(PaypalObject):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    start_time = models.DateTimeField(db_index=True, editable=False)
    create_time = models.DateTimeField(db_index=True, editable=False)

    subscriber = models.ForeignKey(User, on_delete=models.CASCADE)

    status = models.CharField(max_length=24)
    status_update_time = models.DateTimeField(db_index=True, editable=False)
