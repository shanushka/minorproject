from flask import *
from flaskext.mysql import MySQL
mysql=MySQL()
app=Flask(__name__)
app.config['MYSQL_DATABASE_USER']='root'
#app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_DB']='dietician'
app.config['MYSQL_DATABASE_host']='127.0.0.1:5000'
mysql.init_app(app)

@app.route('/',methods=['GET','POST'])
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
    app.run(port=5000, debug=True)