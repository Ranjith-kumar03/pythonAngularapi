# from flask import Flask, request
# from flask_restful import Api, Resource, reqparse
# from models import db, ProductModel

# app = Flask(__name__)
# # https://www.youtube.com/watch?v=IdhtcdCbTVk&list=PLGt1lxwGVOI58H_ClPv1D909ranaK-9NS&index=2
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# api = Api(app)
# db.init_app(app)

# @app.before_first_request
# def create_table():
#     db.create_all()

# class ProductsView(Resource):
#     '''
#     parser = reqparse.RequestParser()
#     parser,add_argument('name', type=str, required=True,
#     help = "cant leave name Blank)
#     parser,add_argument('price', type=float, required=True,
#     help = "cant leave price Blank)
#     parser,add_argument('brand', type=str, required=True,
#     help = "cant leave brand Blank)
#     '''
#     def get(self):
#         products = ProductModel.query.all()
#         return{"products":[x.json() for x in products]}

#     def post(self):
#         data = request.get_json()
#         new_product = ProductModel(
#             data['name'],
#             data['description'],
#             data['price'],
#             data['brand']
#         )
#         db.session.add(new_product)
#         db.session.commit()
#         db.session.flush()
#         return new_product.json(), 201


# class SingleProduct(Resource):
    
#     def get(self,id):
#         product = ProductModel.query.filter_by(id =id).first()
#         if product:
#             return{"product":product.json()}
#         return {"message":f'Product ID not found'}, 404

#     def delete(self,id):
#             product = ProductModel.query.filter_by(id =id).first()
#             if product:
#                 db.session.delete(product)
#                 db.session.commit()
#                 return {"message" :"deleted the product"}
#             else : return {"message":f'Product ID not found'}, 404

#     def put(self,id):
#             data = request.get_json()
#             product = ProductModel.query.filter_by(id =id).first()
#             if product:
#                 product.name = data['name']
#                 product.description = data['description']
#                 product.price = data['price']
#                 product.brand = data['brand']
#             else:
#                 product = ProductModel(id=id ,**data)
            
#             db.session.add(product)
#             db.session.commit()

#             return product.json()
            
    


# api.add_resource(ProductsView, '/products')
# api.add_resource(SingleProduct, '/product/<int:id>')


# app.debug = True

# if __name__ == "__main__":
#     app.run("localhost",port = 5000)

