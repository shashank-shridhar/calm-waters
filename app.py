from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests

# api_1 = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}"

# api_2 = "http://api.openweathermap.org/geo/1.0/direct?q={},{},{}&limit={}&appid={API key}"

api_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

#File handling
api_file = 'API_KEY.key'
fin = ConfigParser()
fin.read(api_file)
api_key = fin['api_key']['key']

# def findLatLon(lat1,lon1):
#     x = requests.get(api_1.format(lat1,lon1,api_key))
#     if x:
#         json_file = x.json()
#         lat1 = json_file['lat']
#         lon1 = json_file['lon']

def findWeather(city):
    fin1 = requests.get(api_url.format(city, api_key))
    if fin1:
        json_file = fin1.json()
        print(json_file)  # Debugging line
        city = json_file['name']
        country_name = json_file['sys']['country']
        temperature_k = json_file['main']['temp']
        temp_c = (temperature_k - 273.15)
        print(temp_c)  # Debugging line
        dis_weather = json_file['weather'][0]['main']
        result = (city, country_name, temp_c, dis_weather)
        return result
    else:
        return None


def display_weather():
    city = search.get()
    weather = findWeather(city)
    if weather:
        loc['text'] = '{}, {}'.format(weather[0],weather[1])
        temp['text'] = '{}C,{}F'.format(weather[2],weather[3])
        weatherEntry['text'] = weather[3]
    else:
        messagebox.showerror('Error','Invalid City Name')

#tkinter window
app = Tk()
app.title("Calm Waters")
app.config(background = "gray")
app.geometry("700x400")

search = StringVar()  #Search City
inputCity = Entry(app,textvariable = search,fg="black",font=("Times New Roman",30,"bold")) #input

inputCity.pack() #packs all of this on the tkinter window

searchButton = Button(app, text="Search", width = 14, bg = "gray", fg = "black", font = ("Arial"), command = display_weather)  #Creating a search button

searchButton.pack()

loc = Label(app,text = '',font=("Arial",35,"bold"))
loc.pack()

temp = Label(app,text='',font=("Arial",35,"bold"))

weatherEntry = Label(app,text='',font=("Arial",35,"bold"))

weatherEntry.pack()


app.mainloop() 
