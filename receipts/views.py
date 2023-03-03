from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm, CategoryForm, AccountForm


# Create your views here.
@login_required
def receipts_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts_lists": receipts,
    }
    return render(request, "receipts/list.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()
    context = {
        "form": form,
    }
    return render(request, "receipts/create_receipt.html", context)


@login_required
def expense_category_list(request):
    expense_category = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "expense_category_list": expense_category,
    }
    return render(request, "receipts/category.html", context)


@login_required
def account_list(request):
    accounts = Account.objects.filter(owner=request.user)
    context = {
        "accounts": accounts,
    }
    return render(request, "receipts/accounts.html", context)


@login_required
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.owner = request.user
            category.save()
            return redirect("category_list")
    else:
        form = CategoryForm()
    context = {
        "form": form,
    }
    return render(request, "receipts/create_category.html", context)


@login_required
def create_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.owner = request.user
            account.save()
            return redirect("account_list")
    else:
        form = AccountForm()
    context = {
        "form": form,
    }
    return render(request, "receipts/create_account.html", context)
