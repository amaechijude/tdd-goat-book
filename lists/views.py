from django.shortcuts import render

from lists.models import Item

name : str = "Amaechi"
# Create your views here.
def home_page(request):
    if request.method == 'POST':
        item = Item()
        item.text = request.POST.get("item_text")
        item.save()
        return render(request, "home.html", {"new_item_data": request.POST.get("item_text")})
    return render(request, 'home.html')