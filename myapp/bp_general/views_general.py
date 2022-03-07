from flask import render_template, abort, redirect, flash, url_for, current_app, Blueprint

from bp_general.form_books import EbookForm
from myapp import db
from bp_general.controller_general import ControllerBook, ControllerEBook

bp_general_app = Blueprint('bp_general', __name__, cli_group="db")


@bp_general_app.route('/')
def do_home():
    controller = ControllerBook(db.session)
    return render_template('general/home.html', name='some name', ids=controller.get_all_ids())


@bp_general_app.route('/books')
def do_books():
    controller = ControllerEBook(db.session)
    return render_template('general/books.html', books=controller.get_all_ebook())


@bp_general_app.route('/books/addebook')
def add_ebook():
    return render_template('general/addebook.html', form=EbookForm())

@bp_general_app.route('/books/ebook/delete/<int:ebook_id>')
def delete_ebook(ebook_id):
    ControllerEBook(db.session).remove_ebook(ebook_id)
    return redirect(url_for('bp_general.do_books'))

@bp_general_app.route('/books/addebook', methods=['POST'])
def add_ebook_post():
    form = EbookForm()
    if form.validate_on_submit():
        controller = ControllerEBook(db.session)
        ebook = controller.add_ebook(form.title.data, 14.0, 'author_first_name', 'author_middle_name',
                                     form.author_last_name.data, 1987,
                                     1, 'ru', 'annotation', 'publisher', 9.0, 'pic')

        return redirect(url_for('bp_general.do_books'))
    else:
        abort(500)


def do_not_found(error):
    return render_template('general/errors.html', code=404, error=error)


def do_not_authorized(error):
    return render_template('general/errors.html', code=403, error=error)


def do_server_error(error):
    return render_template('general/errors.html', code=500, error=error)
