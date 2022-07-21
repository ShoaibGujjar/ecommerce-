# Generated by Django 4.0.3 on 2022-04-09 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('name', models.CharField(choices=[('Chair', 'chair'), ('Sofa', 'sofa')], max_length=200, primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('creatdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.type'),
        ),
    ]
