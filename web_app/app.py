from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from models import db, Page, Menu
from views import PageModelView


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
        print('here', url)
        if url is not None:
            #/About
            page = Page.query.filter_by(url=url).first()
        else:
            #/
            page =Page.query.filter_by(is_homepage=True).first()

        if page is None:
            # TODO cure 404
            return 'Page not Found for {} or hompage not set'.format(url)

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