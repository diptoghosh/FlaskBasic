from flask import request, render_template, redirect, send_file
from datetime import datetime, timedelta
import requests
from application import app, db, mqtt, socketio
from .models import ContactMe

def weather_report(location):
    api_key = "3ac8fa7abbf49bab6cce3ae2127e033a"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + location
    response = requests.get(complete_url)
    response_json = response.json()
    return response_json

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        new_stuff = ContactMe(name=request.form['_name'], email=request.form['_email'],\
            contact=request.form['_contact'], created = str(datetime.now()), message=request.form['_message'])
        try:
            db.session.add(new_stuff)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return repr(e)
    return render_template('index.html', message=message)

@app.route('/tools', methods=['GET','POST'])
def tools():
    return render_template('tools.html')

@app.route('/links', methods=['GET','POST'])
def links():
    selected = ''
    weather_main = ''
    weather_temp = ''
    weather_humid = ''
    weather_sunrise = ''
    weather_sunset = ''
    if request.method == 'POST':
        report_dict = weather_report(request.form['_location'])
        weather_main = 'Weather:     ' + report_dict["weather"][0]["description"].title()
        weather_temp = 'Temperature: ' + str(round(report_dict["main"]["temp"] - 273, 1)) + ' degC'
        weather_humid ='Humidity:    ' + str(round(report_dict["main"]["humidity"], 1)) + ' %'
        sunrise_dt = datetime.utcfromtimestamp(report_dict['sys']['sunrise']) + timedelta(hours=5,minutes=30)
        sunset_dt = datetime.utcfromtimestamp(report_dict['sys']['sunrise']) + timedelta(hours=5,minutes=30)
        weather_sunrise = 'Sunrise:     ' + sunrise_dt.strftime('%Y-%m-%d %H:%M:%S')
        weather_sunset = 'Sunset:      ' + sunset_dt.strftime('%Y-%m-%d %H:%M:%S')
        selected = request.form['_location']
    return render_template('links.html', selected= selected, weather_main=weather_main, weather_temp=weather_temp, weather_humid=weather_humid,\
        weather_sunrise=weather_sunrise, weather_sunset=weather_sunset)

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('house/sensor_data')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print(f'Received: {data["payload"]}')
    # emit a mqtt_message event to the socket containing the message data
    socketio.emit('mqtt_message', data=data)
