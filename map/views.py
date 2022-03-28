from django.shortcuts import render
import folium
# Create your views here.

def index_map(request):
    if request.method == 'POST':
        longitude = request.POST['longitude']
        latitude = request.POST['latitude']
        m_one = folium.Map(location=[longitude, latitude],)._repr_html_()
        m_two = folium.Map(location=[longitude, latitude], zoom_start=13)._repr_html_()
        m_three = folium.Map(location=[longitude, latitude],tiles="Stamen Toner")._repr_html_()
        m_four = folium.Map(location=[longitude, latitude],tiles="Stamen Terrain")._repr_html_()
        m_five = folium.Map(location=[longitude, latitude],tiles="cartodbpositron")._repr_html_()
        contex = {'m_one':m_one,'m_two':m_two,'m_three':m_three,'m_four':m_four,'m_five':m_five}
        return render(request,'index.html',contex)
    return render(request,'index.html',)