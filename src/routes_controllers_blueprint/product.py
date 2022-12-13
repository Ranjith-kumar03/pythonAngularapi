from flask import Flask , Blueprint, request , jsonify
from src.database.models import ProductModel, db
Product = Blueprint("Product", __name__,url_prefix="/api/v1/custom")

@Product.post("/product")
def addProduct():
    _product = request.get_json()
    add_product = ProductModel(
        name=_product['name'],
        description=_product['description'],
        price=_product['price'],
        brand=_product['brand']
    )
    db.session.add(add_product)
    db.session.commit()
    db.session.flush()
    return jsonify({
        "added product":{
            "product": add_product.json()
        }
    })

@Product.get("/products")
def allProducts():
    products = ProductModel.query.all()
    if products:
        return{"products":[x.json() for x in products]}
    else:
        return{"products":"No Products added"}

@Product.get("/product/<int:id>")
def getProduct(id):
    product = ProductModel.query.filter_by(id=id).first()
    if product:
        return{"product":product.json()}
    else:
        return{"products":f"No Products on the given - {id}"}

@Product.put("/product/<int:id>")
def updateProduct(id):
    _product = request.get_json()
    product = ProductModel.query.filter_by(id=id).first()
    if product:
        product.name = _product["name"]
        product.description=_product['description']
        product.price=_product['price']
        product.brand=_product['brand']
        db.session.commit()
        __product = ProductModel.query.filter_by(id=id).first()
        if __product:
            return {"product":__product.json()}
        
    else:
        return{"products":f"No Products on the given - {id}"}

@Product.delete("/product/<int:id>")
def deleteProduct(id):
    product = ProductModel.query.filter_by(id=id).first()
    if product:
        db.session.delete(product)
        db.session.commit()
        delet_product = ProductModel.query.filter_by(id=id).first()
        if not delet_product:
            return{"product":f"successfully deleted product {id}"}
    else:
        return{"products":f"No Products on the given - {id}"}
