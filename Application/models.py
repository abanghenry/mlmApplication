from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group

# Create your models here.


# bellow are existing old mysql databse schema

class Awards1(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    pv = models.CharField(max_length=255)
    cash_equivalent = models.FloatField(blank=True, null=True)
    rank = models.CharField(max_length=191, blank=True, null=True)
    rank_image = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'awards'


class Banks(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveIntegerField()
    currency_id = models.PositiveIntegerField()
    bank_name = models.CharField(max_length=255)
    bank_holder_name = models.CharField(max_length=255)
    bank_account_number = models.CharField(max_length=255)
    bank_branch = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    swift = models.CharField(max_length=255, blank=True, null=True)
    bic = models.CharField(max_length=255, blank=True, null=True)
    sort_code = models.CharField(max_length=255, blank=True, null=True)
    routing_no = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(db_comment='1=active 0=pending')
    default = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    bank_code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banks'


class BinaryPaymentLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveIntegerField(blank=True, null=True)
    strong_leg_id = models.IntegerField()
    strong_leg_pv = models.CharField(max_length=255)
    strong_leg_cf = models.CharField(max_length=255, blank=True, null=True)
    weak_leg_id = models.IntegerField()
    weak_leg_pv = models.CharField(max_length=255)
    weak_leg_cf = models.CharField(max_length=255, blank=True, null=True)
    match_sv_used = models.CharField(max_length=255)
    no_of_match = models.CharField(max_length=255)
    pv_to_amount = models.CharField(max_length=255)
    estimate_earning = models.CharField(max_length=255)
    earning = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'binary_payment_logs'


class BTC(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    bit_address = models.CharField(max_length=255)
    status = models.CharField(max_length=255, db_comment='1=active 0=pending')
    default = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bit_coins'


class BonusBinaries(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveIntegerField(db_comment='owner')
    referral_id = models.PositiveIntegerField(db_comment="user who's action created the bonus")
    pv = models.FloatField(blank=True, null=True)
    date_time_earned = models.DateTimeField()
    source = models.CharField(max_length=255, ) #db_comment='referral, upgrade, stockist, product_direct, product_indirect')    date_time_paid = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField(db_comment='0=pending 1=processing 2=paid 3=flushed 4=cforward')
    details = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bonus_binaries'


class BonusDirectPurchases(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveIntegerField(db_comment='owner')
    pv = models.FloatField(blank=True, null=True)
    date_time_earned = models.DateTimeField()
    source = models.CharField(max_length=255, db_comment='product_direct')
    date_time_paid = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(db_comment='0=pending 1=processing 2=paid 3=flushed 4=cforward')
    details = models.CharField(max_length=255, blank=True, null=True)
    transaction_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bonus_direct_purchases'
complex

class BonusLoyalties(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveIntegerField()
    referral_id = models.PositiveIntegerField()
    currency_id = models.PositiveIntegerField(blank=True, null=True)
    currency_code = models.CharField(max_length=255, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    date_time_earned = models.DateTimeField()
    payment_id = models.PositiveIntegerField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    date_time_paid = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(db_comment='0=pending 1=processing 2=paid 3=cforward')
    details = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bonus_loyalties'


class BonusReferrals(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveIntegerField()
    referral_id = models.PositiveIntegerField()
    currency_id = models.PositiveIntegerField(blank=True, null=True)
    currency_code = models.CharField(max_length=199, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    pv = models.FloatField(blank=True, null=True)
    date_time_earned = models.DateTimeField()
    date_time_paid = models.DateTimeField(blank=True, null=True)
    payment_id = models.PositiveIntegerField(blank=True, null=True)
    source = models.CharField(max_length=199, blank=True, null=True)
    status = models.IntegerField(db_comment='0=pending 1=processing 2=paid 3=cforward')
    details = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bonus_referrals'


class Countries(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    capital = models.CharField(max_length=255, blank=True, null=True)
    citizenship = models.CharField(max_length=255, blank=True, null=True)
    country_code = models.CharField(max_length=3)
    currency = models.CharField(max_length=255, blank=True, null=True)
    currency_code = models.CharField(max_length=255, blank=True, null=True)
    currency_sub_unit = models.CharField(max_length=255, blank=True, null=True)
    currency_symbol = models.CharField(max_length=3, blank=True, null=True)
    currency_decimals = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    iso_3166_2 = models.CharField(max_length=2)
    iso_3166_3 = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    region_code = models.CharField(max_length=3)
    sub_region_code = models.CharField(max_length=3)
    eea = models.IntegerField()
    calling_code = models.CharField(max_length=3, blank=True, null=True)
    flag = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class Currencies(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(unique=True, max_length=255)
    prefix = models.CharField(max_length=255)
    suffix = models.CharField(max_length=255, blank=True, null=True)
    format = models.FloatField()
    baserate = models.FloatField(db_column='BaseRate')  # Field name made lowercase.
    pv_rate = models.FloatField()
    base = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currencies'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=255)
    payload = models.TextField()
    attempts = models.PositiveIntegerField()
    reserved_at = models.PositiveIntegerField(blank=True, null=True)
    available_at = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class NigeriaBanks(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    country = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    bank_code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nigeria_banks'


class OrderItemMetas(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_item_id = models.PositiveIntegerField()
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

class Orderproduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_item_id = models.PositiveIntegerField()
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_metas'


class OrderItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.PositiveIntegerField()
    product_id = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, db_comment='item, tax')
    qty = models.FloatField()
    currency_id = models.PositiveIntegerField()
    amount = models.FloatField()
    discount = models.FloatField()
    total = models.FloatField()
    status = models.CharField(max_length=255)
    store_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_items'


class Orders(models.Model):
    id = models.BigAutoField(primary_key=True)
    orderref = models.CharField(db_column='orderRef', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parent_id = models.PositiveIntegerField(blank=True, null=True)
    user_id = models.PositiveIntegerField()
    owner_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    currency_id = models.PositiveIntegerField()
    number_of_items = models.IntegerField()
    total_sales = models.FloatField()
    total_tax = models.FloatField()
    total_shipping = models.FloatField()
    transaction_fee = models.FloatField()
    total_discount = models.FloatField()
    net_total = models.FloatField()
    status_order = models.CharField(max_length=255)
    invoice_no = models.CharField(max_length=255, blank=True, null=True)
    payment_method = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)
    amount_paid = models.CharField(max_length=255, blank=True, null=True)
    amount_balance = models.CharField(max_length=255, blank=True, null=True)
    payment_ref = models.CharField(max_length=255, blank=True, null=True)
    payment_details = models.TextField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    stockist_paid = models.IntegerField(blank=True, null=True, db_comment='1 if stockist bonus has been paid for this order')
    global_paid = models.IntegerField(blank=True, null=True, db_comment='1 if Global Sales bonus has been paid for this order')
    special_paid = models.IntegerField(blank=True, null=True, db_comment='1 if Special bonus has been paid for this order')

    class Meta:
        managed = False
        db_table = 'orders'


class PackagePrices(models.Model):
    id = models.BigAutoField(primary_key=True)
    package_id = models.PositiveBigIntegerField()
    currency_id = models.PositiveBigIntegerField()
    currency_code = models.CharField(max_length=255)
    price = models.FloatField()
    capping = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package_prices'


class Packages(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255)
    referral_bonus = models.CharField(max_length=255, blank=True, null=True)
    pv = models.FloatField()
    image = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, db_comment='1=active 0=inactive')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'packages'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PaymentAwards(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveIntegerField(blank=True, null=True)
    current_pv_used = models.FloatField(blank=True, null=True)
    award_id = models.IntegerField()
    award_name = models.CharField(max_length=255)
    cash_equivalent = models.FloatField(blank=True, null=True)
    currency_id = models.PositiveIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, db_comment='pending, processing, paid')
    description = models.CharField(max_length=255, blank=True, null=True)
    date_time_paid = models.DateTimeField(blank=True, null=True)
    date_time_to_pay = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_awards'


class PaymentBonuses(models.Model):
    id = models.BigAutoField(primary_key=True)
    payment_id = models.PositiveIntegerField()
    bonus_id = models.PositiveIntegerField()
    bonus_type = models.CharField(max_length=255, db_comment='referral, binary')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_bonuses'


class PaymentJobLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    job_name = models.CharField(max_length=255)
    date_from = models.DateTimeField(blank=True, null=True)
    date_to = models.DateTimeField(blank=True, null=True)
    no_of_payment_generated = models.IntegerField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_job_logs'


class Payments(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveIntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    currency_id = models.PositiveIntegerField(blank=True, null=True)
    bonus_type = models.CharField(max_length=255, db_comment='referral, binary, unilevel')
    status = models.CharField(max_length=255, db_comment='paid, flushed, cforward')
    date_time_paid = models.DateTimeField(blank=True, null=True)
    date_time_to_pay = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments'


class PersonalAccessTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    tokenable_type = models.CharField(max_length=255)
    tokenable_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    token = models.CharField(unique=True, max_length=64)
    abilities = models.TextField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_access_tokens'


class PinRequests(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    package = models.ForeignKey(Packages, models.DO_NOTHING)
    currency_id = models.PositiveIntegerField()
    transaction_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField()
    amount_paid = models.CharField(max_length=255)
    payment_mode = models.CharField(max_length=255, blank=True, null=True)
    account_number = models.CharField(max_length=255, blank=True, null=True)
    bank = models.CharField(max_length=255, blank=True, null=True)
    payment_details = models.CharField(max_length=255, blank=True, null=True)
    transaction_teller = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pin_requests'


class Pins(models.Model):
    id = models.BigAutoField(primary_key=True)
    pin_number = models.CharField(unique=True, max_length=255)
    package_id = models.PositiveBigIntegerField()
    owner_id = models.PositiveBigIntegerField(blank=True, null=True)
    pin_request_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, db_comment='1=used, 0=unused, 2=cancelled')
    used_for = models.PositiveBigIntegerField(blank=True, null=True)
    package_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pins'


class ProductCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_categories'


class ProductDiscounts(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=10)
    value = models.FloatField(db_comment='percentage value or amount')
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_discounts'


class ProductImages(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.IntegerField()
    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_images'


class ProductInventories(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.IntegerField()
    store_id = models.IntegerField()
    quantity = models.IntegerField()
    starting_inventory = models.IntegerField()
    inventory_received = models.IntegerField()
    inventory_shipped = models.IntegerField()
    minimum_required = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_inventories'


class ProductMetas(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.IntegerField()
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_metas'


class ProductPrices(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.IntegerField()
    currency_id = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_prices'


class ProductPurchases(models.Model):
    id = models.BigAutoField(primary_key=True)
    supplier_id = models.IntegerField()
    product_id = models.PositiveBigIntegerField()
    store_id = models.IntegerField()
    number_received = models.IntegerField()
    purchase_date = models.DateField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_purchases'


class ProductReviews(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent = models.IntegerField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()
    rating = models.IntegerField()
    review = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=8)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_reviews'


class ProductSuppliers(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_suppliers'


class ProductTags(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.IntegerField()
    tag_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_tags'


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=255)
    category_id = models.IntegerField()
    type = models.IntegerField(blank=True, null=True, db_comment='1: mlm & retail, 2: mlm only, 3: retail only')
    pv = models.FloatField()
    active = models.IntegerField()
    image_url = models.CharField(max_length=255, blank=True, null=True)
    inventory_id = models.IntegerField(blank=True, null=True)
    discount_id = models.IntegerField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Sessions(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    payload = models.TextField()
    last_activity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sessions'


class Settings(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    type = models.CharField(max_length=255,) # db_comment='text, date, select, check, options') db comment in django issues 
    options = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tooltip = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settings'


class Stores(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    package_id = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    map = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    main = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores'


class Supports(models.Model):
    id = models.BigAutoField(primary_key=True)
    ticket_id = models.CharField(max_length=199, blank=True, null=True)
    parent_id = models.PositiveIntegerField(blank=True, null=True)
    user_id = models.PositiveIntegerField()
    reply_admin_id = models.PositiveIntegerField(blank=True, null=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    status_id = models.PositiveIntegerField()
    urgency = models.CharField(max_length=199, db_comment='low, mid, high')
    last_reply = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supports'


class Tags(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'


class TelescopeEntries(models.Model):
    sequence = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=36)
    batch_id = models.CharField(max_length=36)
    family_hash = models.CharField(max_length=255, blank=True, null=True)
    should_display_on_index = models.IntegerField()
    type = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telescope_entries'


class TelescopeEntriesTags(models.Model):
    entry_uuid = models.CharField(max_length=36)
    tag = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'telescope_entries_tags'


class TelescopeMonitoring(models.Model):
    tag = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'telescope_monitoring'


class Testimonials(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveIntegerField()
    message = models.TextField()
    status = models.CharField(max_length=255, db_comment='pending, active, published')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testimonials'


class TicketStatuses(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    sort_order = models.IntegerField()
    show_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_statuses'


class UpgradeRecords(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveIntegerField()
    sponsor_id = models.PositiveIntegerField()
    old_package_id = models.CharField(max_length=255)
    old_package_name = models.CharField(max_length=255)
    old_package_pv = models.CharField(max_length=255)
    old_package_cost = models.CharField(max_length=255)
    new_package_id = models.CharField(max_length=255)
    new_package_name = models.CharField(max_length=255)
    new_package_pv = models.CharField(max_length=255)
    new_package_cost = models.CharField(max_length=255)
    balance_pv = models.CharField(max_length=255, blank=True, null=True)
    balance_referral_bonus = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upgrade_records'


class UserStores(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    store_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_stores'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username = models.CharField(unique=True, max_length=255)
    gender = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255)
    referred_by = models.PositiveBigIntegerField(blank=True, null=True)
    parent = models.PositiveBigIntegerField(blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    stage_id = models.PositiveIntegerField()
    package_id = models.PositiveBigIntegerField()
    payment_method = models.CharField(max_length=191, blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(db_comment='default currency id')
    active = models.IntegerField()
    welcomed = models.IntegerField()
    link_activated = models.IntegerField(blank=True, null=True)
    upgrade_welcomed = models.IntegerField()
    upgrade_record_id = models.IntegerField(blank=True, null=True)
    date_activated = models.DateTimeField(blank=True, null=True)
    verification_token = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)
    rank = models.CharField(max_length=191, blank=True, null=True)
    registration_pin = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    last_login_date = models.DateTimeField(blank=True, null=True)
    last_login_ip = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    current_binary_pv = models.FloatField(blank=True, null=True)
    spill_over_binary_pv = models.FloatField(blank=True, null=True)
    cumulative_binary_pv = models.FloatField(blank=True, null=True)
    last_cycle_binary = models.DateField(blank=True, null=True)
    current_direct_pv = models.FloatField(blank=True, null=True)
    spill_over_direct_pv = models.FloatField(blank=True, null=True)
    cumulative_direct_pv = models.FloatField(blank=True, null=True)
    last_cycle_direct = models.DateField(blank=True, null=True)
    award_pv_left = models.FloatField(blank=True, null=True)
    award_pv_right = models.FloatField(blank=True, null=True)
    wallet = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersLoginLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    username = models.CharField(max_length=255, blank=True, null=True)
    ip_address = models.CharField(max_length=255, blank=True, null=True)
    date_time = models.DateTimeField()
    action = models.CharField(max_length=255, db_comment='login, logout')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_login_logs'


class WalletTransactions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    amount = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=255, db_comment='debit,credit')
    currency_code = models.CharField(max_length=255)
    currency_id = models.IntegerField()
    details = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wallet_transactions'