import json
from pathlib import Path
from django.shortcuts import render
import json, os

# Create your views here.
def index(request):
    dirpath = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(dirpath, "stock_market_data.json")) as data:
        data = json.loads(data.read())
        print(type( data))

    return render(request, "stock/index.html", {"data": data})