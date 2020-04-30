'''
author: WangQuanyi
date: 2019-11-20 22:52
name: students.py.py
contact: wang0759@algonquinlive.com

'''

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from forms import inputForm
import sqlite3
import base64
import webbrowser

# app config
app = Flask(__name__)
app.config['SECRET_KEY'] = '8888'

# render homePage
@app.route('/')
def home():
    return render_template('index.html', the_title='welcome page')

# function to open find student page
@app.route('/findStudent',methods=['post','get'])
def findStudent():

    form = inputForm()
    conn = sqlite3.connect('week10.db')
    c = conn.cursor()
    query = 'select id, student from lab10 where Student is not null order by student'
    c.execute(query)
    theseStudents = list(c.fetchall())
    nameList = theseStudents
    form.lstNames.choices=nameList


    if request.method == 'POST':
        Name = form.lstNames.data
        c1=conn.cursor()

        query = 'select id, link from lab10 where id={}'.format(int(Name))
        c1.execute(query)
        oneRecord = c1.fetchone()
        thisUrl = base64.urlsafe_b64decode(oneRecord[1]).decode('utf-8')
        # If new is 0, the url is opened in the same browser window if possible.
        # If new is 1, a new browser window is opened if possible.
        # If new is 2, a new browser page (“tab”) is opened if possible.
        webbrowser.open(thisUrl,new=1)
        c1.close()
    c.close()
    return render_template('inputForm.html', form=form, the_title='Find student')


# function to display all students in a form
@app.route('/displayAll',methods=['post','get'])
def display_all():

    conn2 = sqlite3.connect('week10.db')
    c2 = conn2.cursor()
    # list students according to their country, then name.
    query = 'select student,city,country,link from lab10 where Student is not null order by country,student'
    c2.execute(query)
    # make each student into one long list.
    theseStudents = c2.fetchall()
    nameList = []
    urlList = []
    for row in theseStudents:
        # list each student and decode their google link(row[3]) into ASCII
        nameList.append(row)
        url=base64.urlsafe_b64decode(row[3]).decode('utf-8')
        urlList.append(url)
    a = zip(nameList, urlList)
    return render_template('displayAll.html', list=a, the_title='display all student')




