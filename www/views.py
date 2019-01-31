import decimal
import json
import numpy as np
import os
import azure.cosmos.cosmos_client as cosmos_client
from django.http import HttpResponse
from django.shortcuts import render


def filter_data(arr, lower_bound=-127.00, upper_bound=134.00):
    return [ int(x) for x in arr if lower_bound <= int(x) <= upper_bound ]

def parse_data(items, lowest=-127.00, highest=134):
    data_pack = {}
    for item in items:
        filtered_arr = filter_data(item["Temperature_List"])
        av = np.average(filtered_arr)
        city_name = item["city"] + "," + item["country"]
        year = item["Year"]
        month = item["Month"]
        if city_name in data_pack:
            data_pack[city_name][year][month] = av
        else:
            data_pack[city_name] = { year : { month: av} }
    return data_pack


def get_cosmosdb_data():
    HOST = os.getenv("COSMOSDB_HOST")
    MASTER_KEY = os.getenv("COSMOSDB_MASTER_KEY")
    client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY})
    collection_link = 'dbs/weather-data/colls/weather-data'
    documentlist = list(client.ReadItems(collection_link, {'maxItemCount':10}))
    return documentlist

def weather(request):
    data = parse_data(get_cosmosdb_data())
    return render(
        request,
        'weather/weather_data.html',
        {
            'title': 'NOAA Weather Data',
            'content': json.dumps(data)
        }
    )
