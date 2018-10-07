import sys, os

sys.path.append(os.getcwd() + '/web_app') # sesuai dg mark directory as sources

from app import create_app
from models import db, Page

app = create_app()

with app.app_context():
    page = Page()
    page.title = 'Halaman Awal'
    page.content = "<h1>Selamat Datang !</h1>"
    page.is_homepage= True

    db.session.add(page)
    db.session.commit()