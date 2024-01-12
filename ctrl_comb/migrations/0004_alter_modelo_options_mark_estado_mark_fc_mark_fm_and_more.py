# Generated by Django 4.2.5 on 2023-11-22 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ctrl_comb', '0003_alter_modelo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modelo',
            options={'verbose_name': 'Modelo', 'verbose_name_plural': 'Modelos'},
        ),
        migrations.AddField(
            model_name='mark',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mark',
            name='fc',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mark',
            name='fm',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='mark',
            name='uc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mark',
            name='um',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='modelo',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='modelo',
            name='fc',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modelo',
            name='fm',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='modelo',
            name='uc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modelo',
            name='um',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]