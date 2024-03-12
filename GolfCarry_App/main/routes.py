from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from flask_login import login_required, current_user
from GolfCarry_App.models import Affiliation, Character, User, CharacterWithDevilFruit, CharacterWithHaki
from GolfCarry_App.main.forms import AffiliationForm, CharactersForm
from GolfCarry_App import db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    all_affiliations = Affiliation.query.all()
    all_haki_characters = Character.query.filter(Character.haki != 'No').all()
    all_devilfruit_characters = Character.query.filter(Character.devil_fruit != 'No').all()
    print(current_user)
    return render_template('home.html', all_affiliations=all_affiliations,
                            all_haki_characters=all_haki_characters, 
                            all_devilfruit_characters=all_devilfruit_characters)

@main.route('/new_affiliation', methods=['GET', 'POST'])
@login_required
def new_affiliation():
    form = AffiliationForm()
    if form.validate_on_submit():
        new_affiliation = Affiliation(
            title=form.title.data,
            created_by_id=current_user.id
        )
        db.session.add(new_affiliation)
        db.session.commit()

        flash('New affiliation was created successfully.')
        # Pass the new_affiliation variable to the template context
        return redirect(url_for('main.affiliation_detail', affiliation_id=new_affiliation.id))
    return render_template('new_affiliation.html', form=form)


@main.route('/affiliation/<affiliation_id>', methods=['GET', 'POST'])
@login_required
def affiliation_detail(affiliation_id):
    affiliation = Affiliation.query.get(affiliation_id)
    form = AffiliationForm(obj=affiliation)
    
    # Check if new_affiliation is passed in the request args
    new_affiliation = None
    if 'new_affiliation' in request.args:
        new_affiliation_id = request.args.get('new_affiliation')
        new_affiliation = Affiliation.query.get(new_affiliation_id)
    
    if form.validate_on_submit():
        affiliation.affiliation_name = form.title.data
        db.session.commit()

        flash('Affiliation was updated successfully.')
        return redirect(url_for('main.affiliation_detail', affiliation_id=affiliation.id))
    
    # Pass new_affiliation to the template context
    return render_template('affiliation_detail.html', affiliation=affiliation, form=form, new_affiliation=new_affiliation)

@main.route('/favorite_characters_list')
@login_required
def favorite_characters_list():
    user_characters_list = current_user.favorite_characters_list_items
    return render_template('favorite_characters_list.html', character_list=user_characters_list)