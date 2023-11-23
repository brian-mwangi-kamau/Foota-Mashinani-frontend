from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
from dotenv import load_dotenv
load_dotenv()


def homepage(request):
    url = 'https://foota.pythonanywhere.com/api/v1/clubs/'
    api_key = os.environ['api_key']
    
    headers = {
        'X-API-KEY': api_key,
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        
        serialized_data = [
            {
                'name': club['name'],
                'founded': club['founded'],
                'coach': club['coach'],
                'players': club['players'],
            }
            for club in data
        ]
        
        return render(request, 'homepage.html', {'data': serialized_data})
    else:
        return HttpResponse(f"Error: {response.status_code}")
