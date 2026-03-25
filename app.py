from flask import Flask ,redirect, render_template , request 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__ , template_folder='templates')

#database config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///forms.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

#data class 
class myresp(db.Model):
    id = db.Column(db.Integer , primary_key =True)
    email = db.Column(db.String(100) , nullable =False)
    name = db.Column(db.String(100) , nullable =False)
    age = db.Column(db.String(20), nullable=False)
    do_you = db.Column(db.String(100) , nullable =False)
    gender = db.Column(db.String(100) , nullable =False)
    msg = db.Column(db.String(100) , nullable =False)
    # created = db.Column(db.DateTime , default =datetime.utcnow)

    def __repr__(self):
        return f"name{self.id}"

with app.app_context():
        db.create_all()




@app.route('/', methods = ['GET' , 'POST'])
def index():
    # if request.method == 'GET':
    #     return render_template('forms.html')
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        age = request.form.get('age')
        do_you = request.form.get('do_you')
        gender = request.form.get('gender')
        msg = request.form.get('msg')

        data = myresp(
            email=email,
            name=name,
            age=age,
            do_you=do_you,
            gender=gender,
            msg=msg)
        try:
            db.session.add(data)
            db.session.commit()
            return render_template('end.html')
        except Exception as e:
            print(f"ERROR{e}")
            return f"ERROR:{e}"

    else:
        return render_template('forms.html')

@app.route('/responses')
def responses():
    all_data = myresp.query.all()
    return str([(r.name, r.email, r.age, r.gender, r.msg) for r in all_data])

    
    
   






if __name__ == '__main__':
   


    app.run(host = '0.0.0.0' , debug= True)
