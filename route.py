from flask import *
from calorie import *
from flaskext.mysql import MySQL
mysql=MySQL()
app=Flask(__name__)
app.config['MYSQL_DATABASE_USER']='root'
#app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_DB']='dietician'
app.config['MYSQL_DATABASE_host']='127.0.0.1:5000'
mysql.init_app(app)

@app.route('/',methods=['GET','POST'])
def get_data():

  if request.method=='POST':

    Name=request.form['field1']
    email_id=request.form['field2']
    i_age=request.form['field3']
    i_weight=request.form['field4']
    i_height=request.form['field5']
    i_gender=request.form['field6']
    i_preference=request.form['field8']
    i_activity=request.form['field7']
    connection = mysql.get_db()
    cursor = connection.cursor()
    query="INSERT INTO userinput(username,email,weight,height,age,gender,activity,preference) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(Name,email_id,i_weight,i_height,i_age,i_gender,i_activity,i_preference))
    connection.commit()

    return redirect('/dietmenu')
  return render_template("sample.html")

@app.route('/dietmenu' )
def dietmenu():

    food=[breakfast,lunch,snacks,dinner]
    return render_template("diet.html",food=food)


@app.route('/aboutus')#methods=['GET'])
def about():
    return render_template("about.html")

@app.route('/recipe')
def recipee():
    return render_template("recipe.html")

@app.route('/news')#methods=['GET'])
def newss():
    return render_template("news.html")

@app.route('/contactus',methods=['GET','POST'])
def get_message():

  if request.method=='POST':

    First=request.form['first']
    Last=request.form['last']
    Email=request.form['email']
    Phone=request.form['phone']
    Message=request.form['message']

    connection = mysql.get_db()
    cursor = connection.cursor()
    query="INSERT INTO suggestionbox(First_name,Last_name,Email,Phone,Message) VALUES(%s,%s,%s,%s,%s)"
    cursor.execute(query,(First,Last,Email,Phone,Message))
    connection.commit()


  return render_template("contact.html")



if __name__ == '__main__':
    app.run(port=7000, debug=True)