from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_kwargs):
        """Creates and saves an user"""
        user = self.model(username=username, **extra_kwargs)
        user.set_password(password)

        if not username:
            raise ValueError("User must have an username")

        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """Creates and saves a superuser"""
        user = self.create_user(username=username, password=password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model"""

    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_salesman = models.BooleanField(default=False)
    created_by = models.ForeignKey("self", on_delete=None, null=True)

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.name


class Shop(models.Model):
    """model for shop object"""

    name = models.CharField(max_length=255)
    money = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=None, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product model"""

    name = models.CharField(max_length=255)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    buying_price = models.PositiveIntegerField(default=0)
    selling_price = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    """Warehouse model"""

    name = models.CharField(max_length=255)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class WareHouseProducts(models.Model):
    """Model for warehouse products"""

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("warehouse", "product")


class Customer(models.Model):
    """Customer Model"""

    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=15, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    """Vendor Model"""

    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=15, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CustomerTrasnscation(models.Model):
    """Model for the transaction with Customer"""

    order_time = models.DateTimeField(auto_now_add=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Trans {self.pk}---{self.shop}"


class CustomerOrderedItems(models.Model):
    """Model for keeping customer ordered items"""

    order = models.ForeignKey(CustomerTrasnscation, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=0)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    bill = models.PositiveIntegerField(default=0)


class CustomerTrasnscationBill(models.Model):
    """Model for tracking the bill of a transaction"""

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    order = models.OneToOneField(
        CustomerTrasnscation,
        on_delete=models.CASCADE,
    )
    bill = models.PositiveIntegerField(default=0)
    paid = models.PositiveIntegerField(default=0)


class VendorTrasnscation(models.Model):
    """Model for the transaction with Vendor"""

    order_time = models.DateTimeField(auto_now_add=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=None)

    def __str__(self):
        return f"Trans {self.pk}---{self.shop}"


class VendorOrderedItems(models.Model):
    """Model for keeping vendor ordered items"""

    order = models.ForeignKey(VendorTrasnscation, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=0)
    delivery_warehouse = models.ForeignKey(Warehouse, on_delete=None, null=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    bill = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("order", "product", "delivery_warehouse")


class VendorTrasnscationBill(models.Model):
    """Model for tracking the bill of a transaction"""

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    order = models.OneToOneField(
        VendorTrasnscation,
        on_delete=models.CASCADE,
    )
    bill = models.PositiveIntegerField(default=0)
    paid = models.PositiveIntegerField(default=0)
    due = models.PositiveIntegerField(default=0)


class MoveShopToWarehouse(models.Model):
    """Model for moving product shop to warehouse"""

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
