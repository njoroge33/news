from app import app
from flask import render_template
from .request import get_sources

@app.route('/')
def index():
    sources = get_sources()
    return render_template('index.html', sources = sources)
