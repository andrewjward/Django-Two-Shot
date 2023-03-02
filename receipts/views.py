from django.shortcuts import render
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def receipts_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts_lists": receipts,
    }
    return render(request, "receipts/list.html", context)
