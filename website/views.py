from contextlib import _RedirectStream, redirect_stderr
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/user', methods=['GET', 'POST'])
@login_required
def user():
    id=current_user.id
    user= User.query.filter_by(id=id).first()
    return render_template("user.html", username=user.name,hemoglobiny=user.hemoglobiny,tlc=user.tlc,platelets=user.platelets,ers=user.ers,bt=user.bt,ct=user.ct,bloodgroup=user.bloodgroup,bloodshugar=user.bloodshugar,bloodurea=user.bloodurea)






