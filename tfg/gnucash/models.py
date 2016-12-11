# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Accounts(models.Model):
    guid = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=2048)
    account_type = models.CharField(max_length=2048)
    commodity_guid = models.CharField(max_length=32, blank=True, null=True)
    commodity_scu = models.IntegerField()
    non_std_scu = models.IntegerField()
    parent_guid = models.CharField(max_length=32, blank=True, null=True)
    code = models.CharField(max_length=2048, blank=True, null=True)
    description = models.CharField(max_length=2048, blank=True, null=True)
    hidden = models.IntegerField(blank=True, null=True)
    placeholder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'


class Billterms(models.Model):
    guid = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=2048)
    description = models.CharField(max_length=2048)
    refcount = models.IntegerField()
    invisible = models.IntegerField()
    parent = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=2048)
    duedays = models.IntegerField(blank=True, null=True)
    discountdays = models.IntegerField(blank=True, null=True)
    discount_num = models.BigIntegerField(blank=True, null=True)
    discount_denom = models.BigIntegerField(blank=True, null=True)
    cutoff = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billterms'


class Books(models.Model):
    guid = models.CharField(primary_key=True, max_length=32)
    root_account_guid = models.CharField(max_length=32)
    root_template_guid = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'books'


class BudgetAmounts(models.Model):
    budget_guid = models.CharField(max_length=32)
    account_guid = models.CharField(max_length=32)
    period_num = models.IntegerField()
    amount_num = models.BigIntegerField()
    amount_denom = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'budget_amounts'


class Budgets(models.Model):
    guid = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=2048)
    description = models.CharField(max_length=2048, blank=True, null=True)
    num_periods = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'budgets'


class Commodities(models.Model):
    guid = models.CharField(primary_key=True, max_length=32)
    namespace = models.CharField(max_length=2048)
    mnemonic = models.CharField(max_length=2048)
    fullname = models.CharField(max_length=2048, blank=True, null=True)
    cusip = models.CharField(max_length=2048, blank=True, null=True)
    fraction = models.IntegerField()
    quote_flag = models.IntegerField()
    quote_source = models.CharField(max_length=2048, blank=True, null=True)
    quote_tz = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commodities'


class Customers(models.Model):
    guid = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=2048)
    id = models.CharField(max_length=2048)
    notes = models.CharField(max_length=2048)
    active = models.IntegerField()
    discount_num = models.BigIntegerField()
    discount_denom = models.BigIntegerField()
    credit_num = models.BigIntegerField()
    credit_denom = models.BigIntegerField()
    currency = models.CharField(max_length=32)
    tax_override = models.IntegerField()
    addr_name = models.CharField(max_length=1024, blank=True, null=True)
    addr_addr1 = models.CharField(max_length=1024, blank=True, null=True)
    addr_addr2 = models.CharField(max_length=1024, blank=True, null=True)
    addr_addr3 = models.CharField(max_length=1024, blank=True, null=True)
    addr_addr4 = models.CharField(max_length=1024, blank=True, null=True)
    addr_phone = models.CharField(max_length=128, blank=True, null=True)
    addr_fax = models.CharField(max_length=128, blank=True, null=True)
    addr_email = models.CharField(max_length=256, blank=True, null=True)
    shipaddr_name = models.CharField(max_length=1024, blank=True, null=True)
    shipaddr_addr1 = models.CharField(max_length=1024, blank=True, null=True)
    shipaddr_addr2 = models.CharField(max_length=1024, blank=True, null=True)
    shipaddr_addr3 = models.CharField(max_length=1024, blank=True, null=True)
    shipaddr_addr4 = models.CharField(max_length=1024, blank=True, null=True)
    shipaddr_phone = models.CharField(max_length=128, blank=True, null=True)
    shipaddr_fax = models.CharField(max_length=128, blank=True, null=True)
    shipaddr_email = models.CharField(max_length=256, blank=True, null=True)
    terms = models.CharField(max_length=32, blank=True, null=True)
    tax_included = models.IntegerField(blank=True, null=True)
    taxtable = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class Employees(models.Model):
    guid = models.CharField(primary_key=True, max_length=32)
    username = models.CharField(max_length=2048)
    id = models.CharField(max_length=2048)
    language = models.CharField(max_length=2048)
    acl = models.CharField(max_length=2048)
    active = models.IntegerField()
    currency = models.CharField(max_length=32)
    ccard_guid = models.CharField(max_length=32, blank=True, null=True)
    workday_num = models.BigIntegerField()
    workday_denom = models.BigIntegerField()
    rate_num = models.BigIntegerField()
    rate_denom = models.BigIntegerField()
    addr_name = models.CharField(max_length=1024, blank=True, null=True)
    addr_addr1 = models.CharField(max_length=1024, blank=True, null=True)
    addr_addr2 = models.CharField(max_length=1024, blank=True, null=True)
    addr_addr3 = models.CharField(max_length=1024, blank=True, null=True)
    addr_addr4 = models.CharField(max_length=1024, blank=True, null=True)
    addr_phone = models.CharField(max_length=128, blank=True, null=True)
    addr_fax = models.CharField(max_length=128, blank=True, null=True)
    addr_email = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class Entries(models.Model):
    guid = models.CharField(primary_key=True, max_length=32)
    date = models.DateTimeField()
    date_entered = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=2048, blank=True, null=True)
    action = models.CharField(max_length=2048, blank=True, null=True)
    notes = models.CharField(max_length=2048, blank=True, null=True)
    quantity_num = models.BigIntegerField(blank=True, null=True)
    quantity_denom = models.BigIntegerField(blank=True, null=True)
    i_acct = models.CharField(max_length=32, blank=True, null=True)
    i_price_num = models.BigIntegerField(blank=True, null=True)
    i_price_denom = models.BigIntegerField(blank=True, null=True)
    i_discount_num = models.BigIntegerField(blank=True, null=True)
    i_discount_denom = models.BigIntegerField(blank=True, null=True)
    invoice = models.CharField(max_length=32, blank=True, null=True)
    i_disc_type = models.CharField(max_length=2048, blank=True, null=True)
    i_disc_how = models.CharField(max_length=2048, blank=True, null=True)
    i_taxable = models.IntegerField(blank=True, null=True)
    i_taxincluded = models.IntegerField(blank=True, null=True)
    i_taxtable = models.CharField(max_length=32, blank=True, null=True)
    b_acct = models.CharField(max_length=32, blank=True, null=True)
    b_price_num = models.BigIntegerField(blank=True, null=True)
    b_price_denom = models.BigIntegerField(blank=True, null=True)
    bill = models.CharField(max_length=32, blank=True, null=True)
    b_taxable = models.IntegerField(blank=True, null=True)
    b_taxincluded = models.IntegerField(blank=True, null=True)
    b_taxtable = models.CharField(max_length=32, blank=True, null=True)
    b_paytype = models.IntegerField(blank=True, null=True)
    billable = models.IntegerField(blank=True, null=True)
    billto_type = models.IntegerField(blank=True, null=True)
    billto_guid = models.CharField(max_length=32, blank=True, null=True)
    order_guid = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entries'


class Gnclock(models.Model):
    hostname = models.CharField(db_column='Hostname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pid = models.IntegerField(db_column='PID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gnclock'


class Invoices(models.Model):
    guid = models.CharField(primary_key=True, max_length=32)
    id = models.CharField(max_length=2048)
    date_opened = models.DateTimeField(blank=True, null=True)
    date_posted = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=2048)
    active = models.IntegerField()
    currency = models.CharField(max_length=32)
    owner_type = models.IntegerField(blank=True, null=True)
    owner_guid = models.CharField(max_length=32, blank=True, null=True)
    terms = models.CharField(max_length=32, blank=True, null=True)
    billing_id = models.CharField(max_length=2048, blank=True, null=True)
    post_txn = models.CharField(max_length=32, blank=True, null=True)
    post_lot = models.CharField(max_length=32, blank=True, null=True)
    post_acc = models.CharField(max_length=32, blank=True, null=True)
    billto_type = models.IntegerField(blank=True, null=True)
    billto_guid = models.CharField(max_length=32, blank=True, null=True)
    charge_amt_num = models.BigIntegerField(blank=True, null=True)
    charge_amt_denom = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoices'


class Jobs(models.Model):
    guid = models.CharField(primary_key=True, max_length=32)
    id = models.CharField(max_length=2048)
    name = models.CharField(max_length=2048)
    reference = models.CharField(max_length=2048)
    active = models.IntegerField()
    owner_type = models.IntegerField(blank=True, null=True)
    owner_guid = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'


class Lots(models.Model):
    guid = models.CharField(primary_key=True, max_length=32)
    account_guid = models.CharField(max_length=32, blank=True, null=True)
    is_closed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lots'


class Orders(models.Model):
    guid = models.CharField(primary_key=True, max_length=32)
    id = models.CharField(max_length=2048)
    notes = models.CharField(max_length=2048)
    reference = models.CharField(max_length=2048)
    active = models.IntegerField()
    date_opened = models.DateTimeField()
    date_closed = models.DateTimeField()
    owner_type = models.IntegerField()
    owner_guid = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'orders'


class Prices(models.Model):
    guid = models.CharField(primary_key=True, max_length=32)
    commodity_guid = models.CharField(max_length=32)
    currency_guid = models.CharField(max_length=32)
    date = models.DateTimeField()
    source = models.CharField(max_length=2048, blank=True, null=True)
    type = models.CharField(max_length=2048, blank=True, null=True)
    value_num = models.BigIntegerField()
    value_denom = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'prices'


class Recurrences(models.Model):
    obj_guid = models.CharField(max_length=32)
    recurrence_mult = models.IntegerField()
    recurrence_period_type = models.CharField(max_length=2048)
    recurrence_period_start = models.DateField()
    recurrence_weekend_adjust = models.CharField(max_length=2048)

    class Meta:
        managed = False
        db_table = 'recurrences'


class Schedxactions(models.Model):
    guid = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=2048, blank=True, null=True)
    enabled = models.IntegerField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    last_occur = models.DateField(blank=True, null=True)
    num_occur = models.IntegerField()
    rem_occur = models.IntegerField()
    auto_create = models.IntegerField()
    auto_notify = models.IntegerField()
    adv_creation = models.IntegerField()
    adv_notify = models.IntegerField()
    instance_count = models.IntegerField()
    template_act_guid = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'schedxactions'


class Slots(models.Model):
    obj_guid = models.CharField(max_length=32)
    name = models.CharField(max_length=4096)
    slot_type = models.IntegerField()
    int64_val = models.BigIntegerField(blank=True, null=True)
    string_val = models.CharField(max_length=4096, blank=True, null=True)
    double_val = models.FloatField(blank=True, null=True)
    timespec_val = models.DateTimeField(blank=True, null=True)
    guid_val = models.CharField(max_length=32, blank=True, null=True)
    numeric_val_num = models.BigIntegerField(blank=True, null=True)
    numeric_val_denom = models.BigIntegerField(blank=True, null=True)
    gdate_val = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'slots'


class Splits(models.Model):
    guid = models.CharField(primary_key=True, max_length=32)
    tx_guid = models.CharField(max_length=32)
    account_guid = models.CharField(max_length=32)
    memo = models.CharField(max_length=2048)
    action = models.CharField(max_length=2048)
    reconcile_state = models.CharField(max_length=1)
    reconcile_date = models.DateTimeField(blank=True, null=True)
    value_num = models.BigIntegerField()
    value_denom = models.BigIntegerField()
    quantity_num = models.BigIntegerField()
    quantity_denom = models.BigIntegerField()
    lot_guid = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'splits'


class TaxtableEntries(models.Model):
    taxtable = models.CharField(max_length=32)
    account = models.CharField(max_length=32)
    amount_num = models.BigIntegerField()
    amount_denom = models.BigIntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'taxtable_entries'


class Taxtables(models.Model):
    guid = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=50)
    refcount = models.BigIntegerField()
    invisible = models.IntegerField()
    parent = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taxtables'


class Transactions(models.Model):
    guid = models.CharField(primary_key=True, max_length=32)
    currency_guid = models.CharField(max_length=32)
    num = models.CharField(max_length=2048)
    post_date = models.DateTimeField(blank=True, null=True)
    enter_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'


class Vendors(models.Model):
    guid = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=2048)
    id = models.CharField(max_length=2048)
    notes = models.CharField(max_length=2048)
    currency = models.CharField(max_length=32)
    active = models.IntegerField()
    tax_override = models.IntegerField()
    addr_name = models.CharField(max_length=1024, blank=True, null=True)
    addr_addr1 = models.CharField(max_length=1024, blank=True, null=True)
    addr_addr2 = models.CharField(max_length=1024, blank=True, null=True)
    addr_addr3 = models.CharField(max_length=1024, blank=True, null=True)
    addr_addr4 = models.CharField(max_length=1024, blank=True, null=True)
    addr_phone = models.CharField(max_length=128, blank=True, null=True)
    addr_fax = models.CharField(max_length=128, blank=True, null=True)
    addr_email = models.CharField(max_length=256, blank=True, null=True)
    terms = models.CharField(max_length=32, blank=True, null=True)
    tax_inc = models.CharField(max_length=2048, blank=True, null=True)
    tax_table = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendors'


class Versions(models.Model):
    table_name = models.CharField(primary_key=True, max_length=50)
    table_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'versions'
