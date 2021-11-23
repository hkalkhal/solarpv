# Generated by Django 3.2.8 on 2021-11-20 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('client_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('model_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=20)),
                ('cell_technology', models.CharField(max_length=20)),
                ('cell_manufacturer', models.CharField(max_length=20)),
                ('no_of_cells', models.IntegerField()),
                ('no_of_cells_in_series', models.IntegerField()),
                ('no_of_cells_in_strings', models.IntegerField()),
                ('no_of_diodes', models.IntegerField()),
                ('product_width', models.FloatField()),
                ('product_length', models.FloatField()),
                ('superstate_type', models.CharField(max_length=20)),
                ('superstate_manufacturer', models.CharField(max_length=20)),
                ('substrate_type', models.CharField(max_length=20)),
                ('supstate_manufacturer', models.CharField(max_length=20)),
                ('frame_type', models.CharField(max_length=20)),
                ('frame_adhesive', models.CharField(max_length=20)),
                ('encapsulate_type', models.CharField(max_length=20)),
                ('encapsulate_manufacturer', models.CharField(max_length=20)),
                ('junction_box_type', models.CharField(max_length=20)),
                ('junction_box_manufacturer', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TestSequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TestStandard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('published_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(default='Password', max_length=32)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(blank=True, max_length=20, null=True)),
                ('job_title', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('office_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('cell_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('prefix', models.CharField(choices=[('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms.')], max_length=4)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.client')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('is_fi_required', models.CharField(max_length=3)),
                ('FI_required', models.CharField(max_length=20)),
                ('standard_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.teststandard')),
            ],
        ),
        migrations.CreateModel(
            name='PerformanceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_system_voltage', models.FloatField()),
                ('voc', models.FloatField()),
                ('isc', models.FloatField()),
                ('vmp', models.FloatField()),
                ('imp', models.FloatField()),
                ('pmp', models.FloatField()),
                ('ff', models.FloatField()),
                ('model_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.product')),
                ('sequence_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.testsequence')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('postal_code', models.CharField(max_length=5)),
                ('country', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('fax_number', models.CharField(max_length=20)),
                ('client_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.client')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(max_length=20)),
                ('issue_date', models.DateField()),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
                ('location_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.location')),
                ('model_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.product')),
                ('standard_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.teststandard')),
            ],
        ),
    ]