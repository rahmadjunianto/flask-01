from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()


class Page(db.Model):
    __tablename__ = 'page'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    tag = Column(String)
    content = Column(String)
    url = Column(String)

    def __repr__(self):
        return self.title

class Menu(db.Model):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    order = Column(Integer)

    page_id = Column(Integer, ForeignKey('page.id'))
    # page = relationship('Page', backref=backref('Linked from Menu')) multi select
    page = relationship('Page', backref=backref('Linked from Menu', uselist=False))

    def __repr__(self):
        return self.title