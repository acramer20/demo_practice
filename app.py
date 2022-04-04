"""Demo app using SQLAlchemy."""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# db = SQLAlchemy()
# db.app = app
# db.init_app(app)

app.config['SECRET_KEY'] = "chickenzarecool1234"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']= False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_pets():
    """shows list of all pets in db"""
    pets = Pet.query.all()
    return render_template('list.html', pets = pets)

@app.route('/<int:pet_id>')
def show_pet(pet_id):
    """show details about a single pet"""
    pet = Pet.query.get_or_404(pet_id) 
    # This allows for you to respond with a 404 if it is not found. 
    return f"<h1>{pet.name}</h1>"




















# from models import db, connect_db, Pet

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sqla_intro'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True

# connect_db(app)

# from flask_debugtoolbar import DebugToolbarExtension
# app.config['SECRET_KEY'] = "SECRET!"
# debug = DebugToolbarExtension(app)


# @app.route("/")
# def list_pets():
#     """List pets and show add form."""

#     pets = Pet.query.all()
#     return render_template("list.html", pets=pets)


# @app.route("/", methods=["POST"])
# def add_pet():
#     """Add pet and redirect to list."""

#     name = request.form['name']
#     species = request.form['species']
#     hunger = request.form['hunger']
#     hunger = int(hunger) if hunger else None

#     pet = Pet(name=name, species=species, hunger=hunger)
#     db.session.add(pet)
#     db.session.commit()

#     return redirect(f"/{pet.id}")


# @app.route("/<int:pet_id>")
# def show_pet(pet_id):
#     """Show info on a single pet."""

#     pet = Pet.query.get_or_404(pet_id)
#     return render_template("detail.html", pet=pet)
