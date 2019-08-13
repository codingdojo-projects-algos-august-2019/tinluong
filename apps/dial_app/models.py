from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=45)
    lasst_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    pw_hashed = models.CharField(max_length=60)
    user_level = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = UserManager()


class Address(models.Model):
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=55)
    zip_code = models.CharField(max_length=10)


class Client(models.Model):
    name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=45)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)
    start_date = models.DateField
    remark = models.TextField
    tax_id_type = models.CharField(max_length=255)
    tax_id_no = models.CharField(max_length=9)
    bank_acc_no = models.CharField(max_length=12)
    credit_score = models.IntegerField
    credit_type = models.CharField(max_length=25)
    credit_limit = models.IntegerField
    payment_term = models.CharField(max_length=25)
    credit_hold = models.CharField(max_length=25)
    note = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Delivery_location(models.Model):
    name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=45)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)
    remark = models.TextField


class Contact(models.Model):
    name = models.CharField(max_length=255)
    postion = models.CharField(max_length=150)
    office_num = models.CharField(max_length=12)
    cell_num = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    remark = models.TextField
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    delivery_location = models.ForeignKey(
        Delivery_location, on_delete=models.CASCADE)


class Shipment(models.Model):
    mode = models.CharField(max_length=5)
    file_code = models.CharField(max_length=3)
    file_num = models.CharField(max_length=5)
    status = models.CharField(max_length=10)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    carrier = models.CharField(max_length=4)
    master_bl = models.CharField(max_length=12)
    house_bl = models.CharField(max_length=12)
    terminal = models.CharField(max_length=4)
    eta = models.DateField
    entry_date = models.DateField
    devanning = models.CharField(max_length=5)
    created_by = models.ForeignKey(
        User, related_name='shipments', on_delete=models.CASCADE)


class Container(models.Model):
    shipment = models.ForeignKey(
        Shipment, related_name='containers', on_delete=models.CASCADE)
    number = models.CharField(max_length=7)
    size = models.CharField(max_length=2)
    quantity = models.SmallIntegerField
    weight = models.SmallIntegerField
    dimension = models.DecimalField
    discharge_date = models.DateField
    lfd = models.DateField
    pu_date = models.DateField
    pu_time = models.TimeField
    outgate_time = models.TimeField
    waiting_time = models.DecimalField
    demurrage = models.IntegerField
    tmf = models.DecimalField
    yard_storage = models.IntegerField
    exam_fee = models.DecimalField
    demurrange_fee = models.DecimalField
    detention_fee = models.DecimalField
    doc_fee = models.DecimalField
    freight_status = models.CharField(max_length=5)
    customs_status = models.CharField(max_length=5)
    remark = models.TextField
    container_detention_date = models.DateField
    empty_return_date = models.DateField
    container_detention = models.IntegerField
    chasis_num = models.CharField(max_length=7)
    chasis_detention_date = models.DateField
    chasis_return_date = models.DateField
    chasis_detention = models.IntegerField
    new_chasis_num = models.CharField(max_length=7)


class Delivery(models.Model):
    container = models.ForeignKey(
        Container, related_name='deliveries', on_delete=models.CASCADE)
    delivery_location = models.ForeignKey(
        Delivery_location, on_delete=models.CASCADE)
    delivery_date = models.DateField
    delivery_time = models.TimeField
    quantity = models.SmallIntegerField
    weight = models.SmallIntegerField
    dimension = models.DecimalField
