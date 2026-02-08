from django.shortcuts import render
import matplotlib.pyplot as plt
import pandas as pd
import io
import urllib, base64
import numpy as np
from datetime import datetime, time

def index(request):
    specific_time1 = time(22, 0, 0)
    specific_time2 = time(8, 0, 0)
    current_time = datetime.now().time()
    if current_time > specific_time1 or current_time < specific_time2:
        return render(request, 'main/main.html', {"time": 0})
    else:
        return render(request, 'main/main.html', {"time": 1})