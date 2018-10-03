from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from web_app.models import db, Page, Menu
from web_app.views import PageModelView


def create_app():
    app = Flask (__name__)
    app.config.from_pyfile('settings.py')

    db.init_app(app)

    admin = Admin(app, name="Flask01", template_mode="bootstrap3")
    admin.add_view(PageModelView(Page, db.session))
    admin.add_view(ModelView(Menu, db.session))

    @app.route('/')
    @app.route('/<url>')
    def index(url=None):
        if url is not None:
            page = Page.query.filter_by(url=url).first()

        content='empty'
        if page is not None:
            content=page.content
        menu = Menu.query.order_by('order')
        return render_template('index.html', TITLE = 'FLASK 01', CONTENT=content, menu=menu)

    # @app.route('/testdb')
    # def testdb():
    #     import psycopg2
    #
    #     con = psycopg2.connect('dbname=flash01 user=devuser password=devpassword host=postgres')
    #     cur = con.cursor()
    #     cur.execute('select * from page;')
    #     id, title = cur.fetchone()
    #     con.close()
    #     return 'Output DB page : {} - {}'.format(id, title)

    return app