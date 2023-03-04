from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/')
def Home():
    return render_template("Home.html")

@auth.route('/about')
def about():
   return render_template('about.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.user'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, name=name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.user'))

    return render_template("register.html", user=current_user)

@auth.route('/report',methods=['GET', 'POST'])
@login_required
def report():
    if request.method == 'POST':
        hemoglobiny = request.form.get('hb')
        tlc = request.form.get('tlc')
        platelets = request.form.get('platelets')
        ers = request.form.get('ers')
        bt = request.form.get('bt')
        ct = request.form.get('ct')
        bloodgroup = request.form.get('bloodgroup')
        bloodshugar = request.form.get('bloodshugar')
        bloodurea = request.form.get('bloodurea')


        id=current_user.id
        user= User.query.filter_by(id=id).first()
        if hemoglobiny== "":
            user.hemoglobiny=user.hemoglobiny
            
        else:
            user.hemoglobiny=hemoglobiny
            db.session.commit()

        if tlc== "":
            user.tlc=user.tlc
            
        else:
            user.tlc=tlc
            db.session.commit()

        if platelets== "":
            user.platelets=user.platelets
            
        else:
            user.platelets=platelets
            db.session.commit()

        if ers== "":
            user.ers=user.ers
            
        else:
            user.ers=ers
            db.session.commit()

        if ers== "":
            user.ers=user.ers
            
        else:
            user.ers=ers
            db.session.commit()
        
        if bt== "":
            user.bt=user.bt
            
        else:
            user.bt=bt
            db.session.commit()

        if ct== "":
            user.ct=user.ct
            
        else:
            user.ct=ct
            db.session.commit()

        if bloodgroup== "":
            user.bloodgroup=user.bloodgroup
            
        else:
            user.bloodgroup=bloodgroup
            db.session.commit()

        if bloodshugar== "":
            user.bloodshugar=user.bloodshugar
            
        else:
            user.bloodshugar=bloodshugar
            db.session.commit()

        if bloodurea== "":
            user.bloodurea=user.bloodurea
            
        else:
            user.bloodurea=bloodurea
            db.session.commit()

        return redirect(url_for('views.user'))
        
    return render_template("report.html")