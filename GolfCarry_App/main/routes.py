from flask import Blueprint, request, render_template, redirect, url_for, flash
import random
from datetime import date, datetime
from flask_login import login_required, current_user
from GolfCarry_App.models import User, CarryYardages, ProAverageCarryYardages
from GolfCarry_App.main.forms import CarryYardageForm
from GolfCarry_App import db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    all_yardages = CarryYardages.query.all()
    return render_template('home.html', all_yardages=all_yardages)

@main.route('/new_carryyardages', methods=['GET', 'POST'])
@login_required
def new_carryyardages():
    # print("**********************")
    # print('New Carry Yardages')
    # print("IIIIIIIIIIIIIIIIIII CURENT USER BELOW IIIIIIIIIIIIIII")
    print(current_user)
    form = CarryYardageForm()
    if form.validate_on_submit():
        # print("_____________________Form AUTO SUBMIT_______________________")
        new_yardages = CarryYardages(
            PWedge=form.PWedge.data,
            Nine_Iron=form.Nine_Iron.data,
            Eight_Iron=form.Eight_Iron.data,
            Seven_Iron=form.Seven_Iron.data,
            Six_Iron=form.Six_Iron.data,
            Five_Iron=form.Five_Iron.data,
            Four_Iron=form.Four_Iron.data,
            Three_Iron=form.Three_Iron.data,
            Hybrid=form.Hybrid.data,
            Five_Wood=form.Five_Wood.data,
            Three_Wood=form.Three_Wood.data,
            Driver=form.Driver.data,
            created_by_id=current_user.id
        )
        db.session.add(new_yardages)
        db.session.commit()

        flash('New yardages were created successfully.')
        return redirect(url_for('main.yardage_detail', carryyardages_id=new_yardages.id))
    # print('&&&&&&&&&&&&&&&&&&&&&&&& GOT PAST THE FORM &&&&&&&&&&&&&&&&&&&&')
    return render_template('new_carryyardages.html', form=form)


@main.route('/yardages/<carryyardages_id>', methods=['GET', 'POST'])
@login_required
def yardage_detail(carryyardages_id):
    # print("*************")
    print(carryyardages_id)
    yardages = CarryYardages.query.get(carryyardages_id)
    form = CarryYardageForm(obj=yardages)
    
    # Check if new_affiliation is passed in the request args
    new_affiliation = None
    if 'new_affiliation' in request.args:
        new_affiliation_id = request.args.get('new_affiliation')
        new_affiliation = CarryYardages.query.get(new_affiliation_id)
    
    if form.validate_on_submit():
        yardages.PWedge = form.PWedge.data,
        yardages.Nine_Iron=form.Nine_Iron.data,
        yardages.Eight_Iron=form.Eight_Iron.data,
        yardages.Seven_Iron=form.Seven_Iron.data,
        yardages.Six_Iron=form.Six_Iron.data,
        yardages.Five_Iron=form.Five_Iron.data,
        yardages.Four_Iron=form.Four_Iron.data,
        yardages.Three_Iron=form.Three_Iron.data,
        yardages.Hybrid=form.Hybrid.data,
        yardages.Five_Wood=form.Five_Wood.data,
        yardages.Three_Wood=form.Three_Wood.data,
        yardages.Driver=form.Driver.data
        db.session.commit()

        flash('Affiliation was updated successfully.')
        return redirect(url_for('main.yardage_detail', carryyardages_id=yardages.id))
    
    # Pass new_affiliation to the template context
    return render_template('yardage_detail.html', affiliation=yardages, form=form, new_affiliation=new_affiliation)


@main.route('/profile')
@login_required
def user_profile():
    user_yardages = CarryYardages.query.filter_by(created_by_id=current_user.id).all()
    pro = ProAverageCarryYardages()
    return render_template('userhome.html', user_yardages=user_yardages, Pro_yardages=pro)


@main.route('/compare')
@login_required
def compare_users():
    total_users = User.query.count()
    random_user_id = random.randint(1, total_users)
    user_yardages = CarryYardages.query.filter_by(created_by_id=current_user.id).all()
    random_user = CarryYardages.query.filter_by(created_by_id=User.query.filter_by(id=random_user_id).first().id).all()
    return render_template('compare.html', user_yardages=user_yardages, Pro_yardages=random_user)