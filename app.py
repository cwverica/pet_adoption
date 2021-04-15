from flask import Flask, flash, request, redirect, render_template
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True

connect_db(app)

app.config['SECRET_KEY'] = "SECRET!AGENT-MAN!"
debug = DebugToolbarExtension(app)


@app.route('/')
def show_all_pets():

    pets = Pet.query.all()
    return render_template('home.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet_form():

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        pet = Pet(name=name,
                species=species,
                photo_url=form.photo_url.data if form.photo_url.data else None,
                age=form.age.data if form.age.data else None,
                notes=form.notes.data if form.notes.data else None,
                available=True)

        db.session.add(pet)
        db.session.commit()

        flash(f'{name} the {species} has been added!')
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet_form(pet_id):

    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data if form.photo_url.data else None
        pet.age = form.age.data if form.age.data else None
        pet.notesnotes = form.notes.data if form.notes.data else None
        pet.available = form.available.data

        db.session.commit()

        flash(f'{pet.name} the {pet.species} has been updated!')
        return redirect(f'/')
    else:
        return render_template('edit_pet.html', form=form, pet=pet)
