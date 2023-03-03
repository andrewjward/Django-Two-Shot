from django.urls import path
from receipts.views import (
    receipts_list,
    create_receipt,
    expense_category_list,
    account_list,
)

urlpatterns = [
    path("", receipts_list, name="home"),
    path("create/", create_receipt, name="create_receipt"),
    path("categories/", expense_category_list, name="category_list"),
    path("accounts/", account_list, name="account_list"),
]
