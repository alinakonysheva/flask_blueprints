from flask import render_template, abort, redirect, flash, url_for, current_app, Blueprint
from myapp import db

bp_general_app = Blueprint('bp_general', __name__,  cli_group="db")

@bp_general_app.route('/')
def do_home():
    return render_template('general/home.html', name='Kristof')


def do_not_found(error):
    return render_template('general/errors.html', code=404, error=error)


def do_not_authorized(error):
    return render_template('general/errors.html', code=403, error=error)


def do_server_error(error):
    return render_template('general/errors.html', code=500, error=error)