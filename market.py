# from flask import  Flask,render_template
# from flask_sqlalchemy import  SQLAlchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
#
# db =  SQLAlchemy(app)
#
# class Item(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(length=30),nullable=False,unique=True)
#     price = db.Column(db.Integer(),nullable=False)
#     barcode = db.Column(db.String(length=12),nullable=False,unique=True)
#     description = db.Column(db.String(length=1024),nullable=False,unique=True)
#
#     def __repr__(self):
#         return f'Item : {self.name}'
#
#
#
# print ("File2 __name__ = %s" %__name__)
#
# @app.route("/")
# @app.route("/home")
# def home_page():
#     return render_template('home.html')
#
# @app.route("/about")
# def about_page():
#     return "<h1>Hello about !</h1>"
#
#
# @app.route("/about/<username>")
# def about_page2(username):
#     return f"<h1>Hello about ! {username}</h1>"
#
#
# @app.route("/market")
# def market_page():
#     items = Item.query.all()
#     return render_template('market.html',item_name="Phone",items=items)
#
#
#
# if __name__ == "__main__":
#     app.run()