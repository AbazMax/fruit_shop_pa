# Generated by Django 4.1.2 on 2022-10-26 11:06

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_promo_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_line_1', models.CharField(blank=True, db_index=True, max_length=50)),
                ('title_line_2', models.CharField(blank=True, db_index=True, max_length=50)),
                ('paragraph_1', models.TextField(blank=True, db_index=True, max_length=500)),
                ('paragraph_2', models.TextField(blank=True, db_index=True, max_length=500)),
                ('video_link', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to=main.models.About.get_file_name)),
            ],
            options={
                'verbose_name_plural': 'About section',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('banner_image', models.ImageField(help_text='Recommended resolution: 1920x494px', upload_to=main.models.Banner.get_file_name)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Banner',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('address', models.TextField(max_length=500)),
                ('open_hours', models.TextField(max_length=1000)),
                ('contact', models.TextField(max_length=500)),
                ('about_short', models.TextField(max_length=300)),
                ('subscribe_text', models.TextField(max_length=200)),
                ('facebook', models.CharField(max_length=200)),
                ('instagram', models.CharField(max_length=200)),
                ('linkedin', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(db_index=True, max_length=50)),
                ('brand_logo', models.ImageField(upload_to=main.models.Info.get_file_name)),
                ('main_title_line_1', models.CharField(db_index=True, max_length=200)),
                ('main_title_line_2', models.CharField(db_index=True, max_length=200)),
                ('about_title_line_1', models.CharField(db_index=True, max_length=200)),
                ('about_title_line_2', models.CharField(db_index=True, max_length=200)),
                ('contact_title_line_1', models.CharField(db_index=True, max_length=200)),
                ('contact_title_line_2', models.CharField(db_index=True, max_length=200)),
                ('shop_title_line_1', models.CharField(db_index=True, max_length=200)),
                ('shop_title_line_2', models.CharField(db_index=True, max_length=200)),
                ('our_team_title', models.TextField(max_length=200)),
                ('related_prod_title', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Main information',
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to=main.models.Partners.get_file_name)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Partners logos',
            },
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('profession', models.CharField(max_length=50)),
                ('review', models.TextField(max_length=300)),
                ('position', models.SmallIntegerField()),
                ('photo', models.ImageField(upload_to=main.models.Testimonials.get_file_name)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Testimonials',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='WhyUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_title', models.CharField(max_length=50)),
                ('delivery_text', models.TextField(max_length=200)),
                ('price_title', models.CharField(max_length=50)),
                ('price_text', models.TextField(max_length=200)),
                ('service_title', models.CharField(max_length=50)),
                ('service_text', models.TextField(max_length=200)),
                ('refund_title', models.CharField(max_length=50)),
                ('refund_text', models.TextField(max_length=200)),
                ('photo', models.ImageField(upload_to=main.models.WhyUs.get_file_name)),
            ],
            options={
                'verbose_name_plural': 'WhyUs',
            },
        ),
    ]