# Generated by Django 4.1.4 on 2023-02-28 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_sentimentmodel_alter_lead_cust_probability_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='receiver_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='sender_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sentimentmodel',
            name='Sentence',
            field=models.CharField(max_length=60),
        ),
    ]