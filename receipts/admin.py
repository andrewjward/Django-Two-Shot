from django.contrib import admin
from receipts.models import ExpenseCategory, Account, Receipt


# Register your models here.
@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
        "owner",
    )


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
        "number",
        "owner",
    )


@admin.register(Receipt)
class ReAdmin(admin.ModelAdmin):
    list_display = (
        "vendor",
        "id",
        "total",
        "tax",
        "date",
        "purchaser",
    )
