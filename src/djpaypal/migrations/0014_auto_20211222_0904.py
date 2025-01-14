# Generated by Django 3.2.10 on 2021-12-22 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djpaypal', '0013_billing_agreement_plan_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingagreement',
            name='agreement_details',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='billingagreement',
            name='merchant',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='billingagreement',
            name='override_charge_mode',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='billingagreement',
            name='override_merchant_preferences',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='billingagreement',
            name='payer',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='billingagreement',
            name='plan',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='billingagreement',
            name='shipping_address',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='billingplan',
            name='merchant_preferences',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='dispute',
            name='dispute_outcome',
            field=models.JSONField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='dispute',
            name='disputed_transactions',
            field=models.JSONField(editable=False),
        ),
        migrations.AlterField(
            model_name='dispute',
            name='messages',
            field=models.JSONField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='dispute',
            name='offer',
            field=models.JSONField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='dispute',
            name='refund_details',
            field=models.JSONField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='payer',
            name='shipping_address',
            field=models.JSONField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payer',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='redirect_urls',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='transactions',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='preparedbillingagreement',
            name='data',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='sale',
            name='fmf_details',
            field=models.JSONField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='payment_hold_reasons',
            field=models.JSONField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='processor_response',
            field=models.JSONField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='webhookevent',
            name='resource',
            field=models.JSONField(editable=False),
        ),
        migrations.AlterField(
            model_name='webhookevent',
            name='transmissions',
            field=models.JSONField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='webhookeventtrigger',
            name='headers',
            field=models.JSONField(),
        ),
    ]
