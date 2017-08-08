from flask import Flask,request,render_template
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


  return render_template("sample.html")

if __name__=='__main__':
    app.run(debug=True)