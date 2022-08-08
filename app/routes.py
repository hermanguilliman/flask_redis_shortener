from operator import methodcaller
import os
from flask import send_from_directory, render_template, flash, redirect, request, url_for

from app import app
from app.forms import AddUrlForm
from app.services import get_short_url, get_full_url

title=app.config.get('SITE_NAME', 'shortener')


@app.route('/favicon.ico')
async def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/', methods=['GET'])
async def index():
    return render_template("index.html", title=title)

    
@app.route('/success/<short>', methods=['GET'])
async def success_page(short):
    full: str = get_full_url(short)
    if full:
        urls = {
            "short": short,
            "full": full,
            }
        return render_template('success.html', urls=urls)
    else:
        return redirect('/')


@app.route('/add', methods=['GET', 'POST'])
async def add():
    form = AddUrlForm()
    if form.validate_on_submit() and request.method == "POST":
        full_url = form.data.get("url")
        short_url = get_short_url(full_url, app.config.get("URL_LEN"))
        return redirect(url_for('.success_page', short=short_url))
    return render_template('add_url.html', form=form, title=title)


@app.route('/<short>', methods=['GET'])
async def go_to_full_url(short):
    full: str = get_full_url(short)
    if full:
        return redirect(full)
    else:
        return redirect('/')
    