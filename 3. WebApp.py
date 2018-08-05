'''USED POSTMAN+mLab FOR THIS WEBAPP'''
from flask import Flask,jsonify,request
from pymongo import MongoClient

app=Flask(__name__)

client=MongoClient('mongodb://vinay:frais1995@ds115758.mlab.com:15758/web_framework')
db=client.web_framework

@app.route('/add')
def multiple_add():
    post=[{'language':'Python','name':'Flask'},
          {'language':'PHP','name':'Laravel'},
          {'language':'JavaScript','name':'Express'},
          {'language':'Ruby','name':'Rails'}]
    posts=db.webframe
    result=posts.insert_many(post)
    return 'Added User'

@app.route('/framework',methods=['GET'])
def get_all_framework():
    posts=db.webframe
    output=[]
    for q in posts.find():
        output.append({'name':q['name'],'language':q['language']})
    return jsonify({'result':output})

@app.route('/framework/<name>',methods=['GET'])
def get_one_framework(name):
    posts=db.webframe
    q=posts.find_one({'name':name})
    if q:
        output={'name':q['name'],'language':q['language']}
    else:
        output='Result not found.'
    return jsonify({'result':output})

@app.route('/framework',methods=['POST'])
def add_framework():
    posts=db.webframe
    name=request.json['name']
    language=request.json['language']
    post={'language':language,'name':name}
    f_id=posts.insert_one(post).inserted_id
    new_frame=posts.find_one({'_id':f_id})
    output={'name':new_frame['name'],'language':new_frame['language']}
    return jsonify({'result':output})

if __name__=='__main__':
    app.run(debug=True)


