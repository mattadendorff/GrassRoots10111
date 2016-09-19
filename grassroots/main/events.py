from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
from utils import process_w3w

@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    if 'Admin' in session.get('name'):
        emit('status', {'msg': session.get('name') + ' is online'}, room=room)
    else:
        if session.get('lat'):
            lat = session.get('lat')
            lon = session.get('lon')
        else:
            lat, lon = process_w3w(session.get('w3w1'), session.get('w3w2'), session.get('w3w3'))
        emit('status', {'msg': '%s needs help at (%s, %s)' % (session.get('name'), lat, lon)}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)

