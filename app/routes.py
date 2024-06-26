from flask import render_template, redirect

from app import db
from app import app
from app.forms import MessageForm
from app.models import User, Messages

# add route '/' and also add the two methods to handle request: 'GET' and 'POST'
@app.route('/', methods = ['GET', 'POST'])
def home():
    form = MessageForm()
    if form.validate_on_submit():
        # check if user exits in database
        user = User.query.filter_by(author = form.author.data).first()
        # if not create user and add to database
        if user is None:
            new_user = User(author = form.author.data)
            db.session.add(new_user)
        # create row in Message table with user (created/found) add to ta database
        new_message = Messages(message = form.message.data, user_id = User.query.filter_by(author = form.author.data).first().id)
        db.session.add(new_message)
        db.session.commit()
    
    # A starter conversation that is not in the data tables
    posts = [
        {   'author':'Carlos', 
            'message':'Yo! Where you at?!'
        },
        {   'author':'Jerry', 
            'message':'Home. You?'}
    ]

    # output all messages
    # create a list of dictionaries with the following structure
    # [{'author':'carlos', 'message':'Yo! Where you at?!'},
    #  {'author':'Jerry', 'message':'Home. You?'}]
    allmessages = Messages.query.all()
    if allmessages is not None:
        for onemessage in allmessages:
            posts = posts + [
            {   'author':f'{User.query.filter_by(id = onemessage.user_id).first().author}', 
                'message':f'{onemessage.message}'}
            ]
   

    return render_template('home.html', posts=posts, form=form)

