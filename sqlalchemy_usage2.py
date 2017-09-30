# coding: utf-8
from models import House,Rent,Price,DBSession
session = DBSession()
'''
a=session.query(House.id,House.url).all()
for i in a:
    print i
'''
h_id=82
h = session.query(House).filter(House.id==h_id).first()
print type(h)
print h.id