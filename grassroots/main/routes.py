from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm, AdminForm, GeoForm


# @main.route('/', methods=['GET', 'POST'])
# def index():
#     """"Login form to enter a room."""
#     form = LoginForm()
#     if form.validate_on_submit():
#         session['name'] = form.name.data
#         session['location'] = form.loc.data
#         session['room'] = form.room.data
#         return redirect(url_for('.chat'))
#     elif request.method == 'GET':
#         form.name.data = session.get('name', '')
#         form.loc.data = session.get('location', '')
#         form.room.data = session.get('room', '')
#     return render_template('index.html', form=form)


@main.route('/', methods=['GET', 'POST'])
def index():
    """"Login form to enter a room."""
    form = GeoForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['lat'] = form.lat.data
        session['lon'] = form.lon.data
        session['w3w1'] = form.w3w1.data
        session['w3w2'] = form.w3w2.data
        session['w3w3'] = form.w3w3.data
        session['room'] = form.room.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.lat.data = session.get('lat', '')
        form.lon.data = session.get('lon', '')
        form.w3w1.data = session.get('w3w1', '')
        form.w3w2.data = session.get('w3w2', '')
        form.w3w3.data = session.get('w3w3', '')
        form.room.data = session.get('room', '')
    return render_template('geo_index.html', form=form)


@main.route('/admin', methods=['GET', 'POST'])
def admin():
    """"Login form to enter a room."""
    form = AdminForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('admin.html', form=form)


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    lat = session.get('lat', '')
    lon = session.get('lon', '')
    w3w1 = session.get('w3w1', '')
    w3w2 = session.get('w3w2', '')
    w3w3 = session.get('w3w3', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room)
