"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import PropertyForm
from werkzeug.utils import secure_filename
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/property')
def property():
    form = PropertyForm()
    if request.method == "POST" and form.validate_on_submit():
        title = request.form['title']
        bedrooms = request.form['bedrooms']
        bathrooms = request.form['bathrooms']
        location = request.form['location']
        price = request.form['price']
        types = request.form['types']
        description = request.form['description']

        photo = request.form['photo']
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File Saved', 'success')
        return redirect(url_for('home'))
    return render_template('property.html', form=form)

@app.route('/properties')
def properties():
    return render_template('properties.html')

@app.route('/property/<propertyid>')
def show_property(propertyid):
    if userid != '':
        user=UserProfile.query.filter_by(id=userid).first()
    else:
        flash("No such user exists")
        return redirect(url_for("properties"))

    return render_template('property.html')
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
