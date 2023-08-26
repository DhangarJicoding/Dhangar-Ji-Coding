from flask import Flask,render_template,jsonify
app=Flask(__name__)

jobs1=[{
            'id':1,
            'title':"SoftWare Enginner",
           'Location':"Banlore",
            'salary':'150000'
            },
        {
            'id': 2,
            'title': "BackEnd Developer",
            'Location': "Lukhnow",
            'salary': '800000'
        },
        {
            'id': 3,
            'title': "Data Analytics",
            'Location': "Noida",
            'salary': '180000'
        },
        {
            'id': 4,
            'title': "Data Scientist",
            'Location': "Gujrat",
            'salary': '170000'
        }
          ]



@app.route('/')
def home():
    return render_template("home.html",jobs=jobs1,com="DhangarJi Codig ")
@app.route('/api/jobs')
def list_jobs():
    return jsonify(jobs1)



app.run(debug="True")