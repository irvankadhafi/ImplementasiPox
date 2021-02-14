import os
from flask import Flask, session, redirect, url_for, escape, request, render_template, jsonify, Response
import mysql.connector
from hashlib import md5
from base64 import b64encode
from subprocess import Popen, call, PIPE
from celery import Celery

app = Flask(__name__)
config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'implementasipox'
    }
db = mysql.connector.connect(**config)
cur = db.cursor()
p="a"
#Celery configuration
app.config['CELERY_BROKEN_URL'] = 'redis://0.0.0.0:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://0.0.0.0:6379/0'

#initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKEN_URL'])
celery.conf.update(app.config)


@app.route('/test')
def main():
    return render_template('index.html')

@app.route('/')
def hello():
    return 'Hello Flask from alpine-linux! -IrvanKadhafi'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
