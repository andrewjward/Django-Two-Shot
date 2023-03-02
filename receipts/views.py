from django.shortcuts import render
from receipts.models import Receipt


# Create your views here.
def receipts_list(request):
    receipts = Receipt.objects.all()
    context = {
        "receipts_lists": receipts,
    }
    return render(request, "receipts/list.html", context)
