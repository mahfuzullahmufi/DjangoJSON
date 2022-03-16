from datetime import date
from django.core.management.base import BaseCommand
import os, json

from stock.models import Stock


class Command(BaseCommand):
    help = "Adds stock data from JSON to database"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        dirpath = os.path.dirname(os.path.abspath(__file__))

        print("Clearing old data...")

        Stock.objects.all().delete()

        print("Uploading data to database...")

        with open(os.path.join(dirpath, "stock_market_data.json")) as data:
            data = json.loads(data.read())
            # print(type( data))

            for stock in data:
                # print(stock)
                # print(type(stock))
                Stock.objects.create(date=stock['date'], 
                                        trade_code=stock['trade_code'], 
                                        high=float(stock['high'].replace(",", "")),
                                        low=float(stock['low'].replace(",", "")),
                                        open=float(stock['open'].replace(",", "")),
                                        close=float(stock['close'].replace(",", "")),
                                        volume=int(stock['volume'].replace(",", ""))                                    
                                    )

        print("Uploaded Data Successfully.")
