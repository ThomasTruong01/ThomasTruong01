from config import db
from flask import Flask, render_template, redirect, request
from models import Dojo, Ninja


def root():
    # dojoList = Dojo.query.all()
    return render_template('index.html')


def addDojo():
    newDojo = Dojo(name=request.form['name'],
                   city=request.form['city'],
                   state=request.form['state'])
    db.session.add(newDojo)
    db.session.commit()
    return redirect('/')


def addNinja():
    newNinja = Ninja(
        first_name=request.form['fName'], last_name=request.form['lName'], dojo_id=request.form['dojoLocation'])
    db.session.add(newNinja)
    db.session.commit()
    return redirect('/')
