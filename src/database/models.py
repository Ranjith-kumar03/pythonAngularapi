from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ProductModel(db.Model):
    __tablename__ = "products"

    def __init__(self, name, description, price, brand):
        self.name = name
        self.description = description
        self.price = price
        self.brand = brand
        

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(250))
    price = db.Column(db.Integer())
    brand = db.Column(db.String(50))

    def json(self):
        return {"id":self.id, "name": self.name,"description":self.description,
                  "price":self.price ,"brand":self.brand}