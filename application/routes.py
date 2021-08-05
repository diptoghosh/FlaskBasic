from flask import request, render_template, redirect, send_file
from datetime import datetime
from application import app, db
from .models import ContactMe

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
    return render_template('links.html')

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
