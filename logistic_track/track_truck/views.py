from django.shortcuts import render,redirect
import requests
import json
import folium
from django.http import HttpResponse

# Create your views here.
def trip_view(request):
    return render(request,'trip.html')

def trip_track_view(request):
    if request.method =='POST':
        trip_id=request.POST['trip_id']
        truck_no=request.POST['truck_no']
        global track_url
        track_url=request.POST['track_url']
        print(trip_id)
        print(track_url)
        print(truck_no)
        return redirect('track_details')
    #     <QueryDict: {'trip_id': ['123'], 'truck_no': ['ABC'], 'track_url': ['URL'], 'csrfmiddlewaretoken': ['KTW36Cmb
    # f44zZp3XgtdvSvYTDOVghxspX218aVjRF5ZbuleQZEdXzTxwMEuwYHRC'], 'submit': ['submit']}>
    return render(request,'track_trip.html')


def track_details(request):
    ip=requests.get(track_url)#'https://api.ipify.org?format=json')
    # s1=json.dumps(ip.next)
    ip_data=json.loads(ip.text)
    print(ip_data)
    responce=requests.get('http://ip-api.com/json/'+ip_data['ip'])
    location_data_one=responce.text
    location_data=json.loads(location_data_one)
    print('location_data.lat :',location_data)
    global lat,lon
    lat=location_data['lat']
    lon=location_data['lon']
    print('lat',lat)
    print('lon',lon)
    return render(request,'track_details.html',{'data':location_data})

def track_details_2(request):
    m= folium.Map()
    folium.Marker([lat,lon]).add_to(m)
    m=m._repr_html_()
    # context={'m':m}
    return render (request,'track_details_2.html',{'m':m})