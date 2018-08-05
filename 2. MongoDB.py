'''USED mLab FOR HOSTING MongoDB'''
from flask import Flask,jsonify
from pymongo import MongoClient

app=Flask(__name__)

client=MongoClient('mongodb://vinay:frais1995@ds213612.mlab.com:13612/flaskoperations')
db=client.flaskoperations

@app.route('/add')
def multiple_add():
    post=[{'name':'Anthony','language':'Python'},
          {'name':'Kelly','language':'C'},
          {'name':'John','language':'Java'},
          {'name':'Cedric','language':'Haskell'}]
    posts=db.posts
    result=posts.insert_many(post)
    return 'Added User'

@app.route('/find')
def find():
    posts=db.posts
    cedric=posts.find_one({'name':'Cedric'})
    return 'You found '+cedric['name']+'. His favourite language is '+cedric['language']

@app.route('/update')
def update():
    posts=db.posts
    john=posts.find_one({'name':'Cedric'})
    john['language']='Haskell'
    posts.save(john)
    return 'Updated John'

@app.route('/delete')
def delete():
    posts=db.posts
    kelly=posts.find_one({'name':'Kelly'})
    posts.remove(kelly)
    return 'Removed Kelly'
    
if __name__=='__main__':
    app.run(debug=True)


