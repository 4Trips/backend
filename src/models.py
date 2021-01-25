from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import datetime

#from flask_appbuilder import Model

db = SQLAlchemy()

class Userpro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(35), unique=True, nullable=False)
    password = db.Column(db.String(40), unique=False, nullable=False)
    phone= db.Column(db.String(20), unique = True , nullable=False)
    url = db.Column(db.String(120))
    location = db.Column(db.String(40) , nullable= False)
    direction = db.Column(db.String(40), nullable=False)
    vat_number = db.Column(db.String(20))
    social_reason = db.Column(db.String(20))
    avatar= db.Column(db.String(120), nullable=False)
    photos = db.Column(db.String(180))
    registr_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    rol = db.Column(db.String(30))
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    Ofertas = db.relationship("Offers")

    def __init__(self,user_name,email,password,phone,url,location,direction,vat_number,social_reason,avatar,photos,registr_date,rol,is_active):
        self.user_name = user_name
        self.email = email
        self.password = password
        self.phone = phone
        self.url= url
        self.location = location
        self.direction = direction
        self.vat_number = vat_number
        self.social_reason =social_reason
        self.avatar = avatar
        self.photos = photos
        self.registr_date = registr_date

    def __repr__(self):
        return '<Userpro %r>' % self.user_name
      
     
    def serialize(self,user_name,email,phone,url,location,direction,vat_number,social_reason,avatar,photos,registr_date,rol):
        return {
            "id": self.id,
            "user_name":self.user_name,
            "email": self.email,
            "phone": self.phone,
            "url": self.url,
            "location": self.location,
            "direction":self.direction,
            "vat_number":self.vat_number,
            "social_reason": self.social_reason,
            "avatar": self.avatar,
            "photos": self.photos,
            "registr_date": self.registr_date,
            "rol": self.rol
            # do not serialize the password, its a security breach
        }
      
      
     

class Traveler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(15), nullable=False)
    avatar = db.Column(db.String(180), nullable=True)
    rol = db.Column(db.String(10), nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    trip = relationship("Trip")
    fecha_registro = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
  

    def __init__(self,username,email,password,avatar,rol,is_active):
        self.username = username
        self.email = email
        self.password = password
        self.avatar = avatar
        self.rol = rol
        self.is_active = True

    
    def __repr__(self):
        return '<Traveler %r>' % self.username

    def __password__bcrypt(self):
        return password

    def serialize(self): 
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "avatar": self.avatar,
            "rol": self.rol,   
            "create_date":self.fecha_registro,
        }

class Offers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_pro =db.Column(db.Integer, db.ForeignKey("userpro.id"), nullable=False)
    id_trip = db.Column(db.Integer, db.ForeignKey("trip.id"),nullable=False)
    date = db.Column(db.DateTime,nullable=False,default=datetime.datetime.utcnow)
    text = db.Column(db.String(200),nullable=False)

    def __init__(self,text,id_pro,id_trip):
        self.text: text
        self.id_pro: id_pro
        self.id_trip: id_trip
        
    def __repr__(self):
        return '<Offers %r>' % self.id

    def serialize(self):
        return {
            "id":self.id,
            "date":self.date,
            "text":self.text,
            "date":self.date,
            "id_pro":self.id_pro,
            "id_trip":self.id_trip
        }

class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_traveler = db.Column(db.Integer, db.ForeignKey('traveler.id'))
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    post_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    needs_trip = db.Column(db.String(60), unique=False, nullable=False)
    destination = db.Column(db.String(200), unique=False, nullable=False)
    first_day = db.Column(db.Date(), unique=False, nullable=False)
    last_day = db.Column(db.Date(), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)
    receiving_offers = db.Column(db.Boolean(), unique=False, nullable=False)
    offers = relationship("Offers")
    counter = db.Column(db.Integer,nullable=False)

    def __init__(self,is_active,needs_trip,destination,first_day,last_day,description):
        self.is_active = True
        self.needs_trip = needs_trip
        self.destination = destination
        self.first_day = first_day
        self.last_day = last_day
        self.description = description
        self.is_active = is_active
        self.counter = 0

    def __repr__(self):
        return '<Trip %r>' % self.id

    def serialize (self):
        return {
            "id": self.id,
            "id_traveler": self.id_traveler,
            "post_date": self.post_date,
            "needs_trip": self.needs_trip,
            "destination": self.destination,
            "first_day": self.first_day,
            "last_day": self.last_day,
            "description": self.description,
            "counter":self.counter,
            "receiving_offers":self.receiving_offers
        }