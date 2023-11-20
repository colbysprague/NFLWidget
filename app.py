from flask import Flask
from flask_socketio import SocketIO
from random import random
from threading import Lock
from datetime import datetime
from utils import replay_game
import json

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')


thread = None
thread_lock = Lock()


def background_thread():
    while replay_game():
        runningTotals = next(replay_game())
        print(len(runningTotals))
        socketio.emit('data_update', json.dumps(runningTotals))
        socketio.sleep(5)

@socketio.on('connect')
def connect():
    global thread
    print('Client connected')

    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)

@socketio.on('disconnect')
def disconnect():
    print('Client Disconnect')

if __name__ == '__main__':
    socketio.run(app)



