from flask import Flask, request, redirect, render_template

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import PetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'   
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'itsasecret'

app.debug = True

debug = DebugToolbarExtension(app)

connect_db(app)

with app.app_context():
    db.create_all()  # Create tables if they don't exist
    print('Tables created')

@app.route('/')
def pets_list():
    # Displays a page with the list of pets
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/add', methods = ["GET","POST"])
def add_pet():
    #Display page with the form to create a new pet
    form = PetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != 'csrf_token'}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('form.html', form=form)
    
@app.route('/<int:pet_id>', methods = ["GET","POST"])
def edit_pet(pet_id):
    #Display page with the form to edit a pet
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit.html', form=form, pet=pet)
    



