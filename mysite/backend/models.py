from django.db import models

# Create your models here.
class Client (models.Model):
    name = models.CharField(max_length=20)
    client_type = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    job_title = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    office_phone = models.CharField(max_length=20)
    cell_phone = models.CharField(max_length=20)
    prefix = models.CharField(max_length=4)
    client_id = models.ForeignKey(Client, on_delete = models.CASCADE)

    def __str__(self):
        return self.first_name

class Location(models.Model):
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=5)
    country = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    fax_number = models.CharField(max_length=20)
    client_id = models.ForeignKey(Client,null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.address1

class TestStandard(models.Model):
    standard_name = models.CharField(max_length=50)
    description = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.standard_name

class Service(models.Model):
    service_name = models.CharField(max_length=20)
    description = models.TextField()
    is_fi_required = models.CharField(max_length=3)
    FI_required = models.CharField(max_length=20)
    standard_id = models.ForeignKey(TestStandard, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.service_name

class TestSequence(models.Model):
    sequence_name = models.CharField(max_length=20)

    def __str__(self):
        return self.sequence_name

class Product(models.Model):
    model_number = models.CharField(max_length=10, primary_key=True)
    product_name = models.CharField(max_length=20)
    cell_technology = models.CharField(max_length=20)
    cell_manufacturer = models.CharField(max_length=20)
    no_of_cells = models.IntegerField()
    no_of_cells_in_series = models.IntegerField()
    no_of_cells_in_strings = models.IntegerField()
    no_of_diodes = models.IntegerField()
    product_width = models.FloatField()
    product_length = models.FloatField()
    superstate_type = models.CharField(max_length=20)
    superstate_manufacturer = models.CharField(max_length=20)
    substrate_type = models.CharField(max_length=20)
    supstate_manufacturer = models.CharField(max_length=20)
    frame_type = models.CharField(max_length=20)
    frame_adhesive = models.CharField(max_length=20)
    encapsulate_type = models.CharField(max_length=20)
    encapsulate_manufacturer = models.CharField(max_length=20)
    junction_box_type = models.CharField(max_length=20)
    junction_box_manufacturer = models.CharField(max_length=20)

    def __str__(self):
        return self.product_name

class Certificate(models.Model):
    UserID = models.ForeignKey(User, on_delete = models.CASCADE)
    report_type = models.CharField(max_length=20)
    issue_date = models.DateField()
    standard_ID = models.ForeignKey(TestStandard, on_delete = models.CASCADE)
    location_ID = models.ForeignKey(Location, on_delete = models.CASCADE)
    model_number = models.ForeignKey(Product, on_delete = models.CASCADE)


class PerformanceData(models.Model):
    model_number = models.ForeignKey(Product, on_delete = models.CASCADE)
    sequence_ID = models.ForeignKey(TestSequence, on_delete = models.CASCADE)
    max_system_voltage = models.FloatField()
    voc = models.FloatField()
    isc = models.FloatField()
    vmp = models.FloatField()
    imp = models.FloatField()
    pmp = models.FloatField()
    ff = models.FloatField()
