from flask import Flask, render_template


def create_app():
    app = Flask (__name__)
    app.config.from_pyfile('settings.py')

    @app.route('/')
    def index():
        import psycopg2

        con = psycopg2.connect('dbname=flash01 user=devuser password=devpassword host=postgres')
        cur = con.cursor()
        cur.execute('select content from page where id=1') # mengembalikan tuple (0,1,2)
        content = cur.fetchone()
        con.close()
        return render_template('index.html', TITLE = 'FLASK 01', CONTENT=content[0])


    @app.route('/about')
    def about():
        return render_template('about.html', TITLE = 'FLASK 01')

    @app.route('/testdb')
    def testdb():
        import psycopg2

        con = psycopg2.connect('dbname=flash01 user=devuser password=devpassword host=postgres')
        cur = con.cursor()
        cur.execute('select * from page;')
        id, title = cur.fetchone()
        con.close()
        return 'Output DB page : {} - {}'.format(id, title)

    return app