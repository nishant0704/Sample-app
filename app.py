from flask import Flask,render_template,request,jsonify, Response
from flask_mysqldb import MySQL
from citydata import cities_one,cities_two
import yaml
from json import dumps
import re




app = Flask(__name__)
db=yaml.load(open('db.yaml'))
app.config['MYSQL_HOST']= db['mysql_host']
app.config['MYSQL_USER']= db['mysql_user']
app.config['MYSQL_PASSWORD']= db['mysql_password']
app.config['MYSQL_DB']= db['mysql_db','mysql_db1']
mysql = MySQL(app)


@app.route('/',methods = ['GET'])
def samplefunction():
    #access your DB get your results here
   r = requests.get(url ="http://localhost:5000/")
   data = r.json()
   name = data['name']
   age = data['age']
   address = data['address']
   print(data['name'])
    #if request.method == 'POST':
   cur = mysql.connection.cursor()
   cur.execute("INSERT INTO person_data(name,age,address) VALUES(%s,%s,%s)",(name,age,address))
   mysql.connection.commit()
   cur.close()
   val= Response(dumps(data))
   val.headers['Access-Control-Allow-Origin'] = '*'
   return (val)

@app.route('/upload')
def inserting():
    city_a = random.choice(cities_one)
    city_b = random.choice(cities_two)
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO city(cityname,citynew) VALUES(%s,%s)",(city_a,city_b))
    mysql.connection.commit()
    cur.close()
    cur.execute("SELECT * FROM city")
    city_data = cur.fetchall()
    if len(city_data) > 0:
        value = Response(dumps(city_data))
        return value


@app.route('/search',methods=['GET'])
def retrieve():
    name = str(request.args.get('q'))
    result = []
    rsp = Response("not found",status=404)
    rsp.headers['Access-Control-Allow-Origin'] = '*'

    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM person_information")
    user = cur.fetchall()
    for x in user:
        if re.match(str(name),x[0],flags=re.IGNORECASE):
            result.append({'Name':x[0],'Age':x[1],'Job':x[2],'Hometown':x[3],'Loc':x[4]})

    if len(result) > 0:
        resp = Response(dumps(result))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    return rsp

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port ='5001')









# resp = requests.get('main.html')
# if resp.status_code != 200:
#     raise ApiError


# from flask import Flask,render_template,request,redirect
# from flask_mysqldb import MySQL
# import yaml
#
# app = Flask(__name__)
# db=yaml.load(open('db.yaml'))
# app.config['MYSQL_HOST']= db['mysql_host']
# app.config['MYSQL_USER']= db['mysql_user']
# app.config['MYSQL_PASSWORD']= db['mysql_password']
# app.config['MYSQL_DB']= db['mysql_db']
#
# mysql = MySQL(app)
#
# @app.route('/',methods=['GET','POST'])
# def index():
#     if request.method == 'POST':
#         userDetails = request.form;
#         name = userDetails['name']
#         email = userDetails['email']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO users(name,email) VALUES(%s,%s)",(name,email))
#         mysql.connection.commit()
#         cur.close()
#         return redirect('/users')
#     return render_template('index.html')
#
# @app.route('/users')
# def users():
#     cur = mysql.connection.cursor()
#     resultValue = cur.execute("SELECT * FROM users")
#     if resultValue > 0:
#         userDetails = cur.fetchall()
#         return render_template('users.html',userDetails=userDetails)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


#
#
#
#
#
#
#
# # persons = [
# #     {
# #         'Name':'Karthik',
# #         'Age':'27',
# #         'Job':'Founder',
# #         'Hometown':'Udupi',
# #         'Loc':'blore',
# #
# #     },
# #     {
# #         'Name':'Sandeep',
# #         'Age':'27',
# #         'Job':'Engineer',
# #         'Hometown':'Udupi',
# #         'Loc':'blore',
# #     },
# #     {
# #         'Name':'Manu',
# #         'Age':'27',
# #         'Job':'Operations',
# #         'Hometown':'Tumkur',
# #         'Loc':'blore',
# #     },
# #     {
# #         'Name':'Prashant',
# #         'Age':'27',
# #         'Job':'Engineer',
# #         'Hometown':'Nepal',
# #         'Loc':'blore',
# #     },
# #     {
# #         'Name':'Joice',
# #         'Age':'24',
# #         'Job':'Engineer',
# #         'Hometown':'Kerala',
# #         'Loc':'blore',
# #     },
# #     {
# #         'Name':'Steev',
# #         'Age':'25',
# #         'Job':'Engineer',
# #         'Hometown':'Kerala',
# #         'Loc':'blore',
# #     },
# #     {
# #         'Name':'Akhil',
# #         'Age':'23',
# #         'Job':'Engineer',
# #         'Hometown':'Kerala',
# #         'Loc':'blore',
# #     },
# #     {
# #         'Name':'Nisha',
# #         'Age':'25',
# #         'Job':'Engineer',
# #         'Hometown':'Udupi',
# #         'Loc':'blore',
# #     },
# #     {
# #         'Name':'Nishant',
# #         'Age':'25',
# #         'Job':'Engineer',
# #         'Hometown':'Udupi',
# #         'Loc':'blore',
# #     },
# #   ]
#
#
# # @app.route('/search' ,methods=['GET'])
# # def get_contact():
# #     name = str(request.args.get('q'))
# #     result = []
# #     for x in persons:
# #         # if x['Name'].lower() == name.lower():
# #         if re.match(str(name),x['Name'],flags=re.IGNORECASE):
# #             result.append({'Name':x['Name'],'Age':x['Age'],'Loc':x['Loc'],'Job':x['Job'],'Hoemtwon':x['Hometown']})
# #             # print str(x)
# #             resp = Response(dumps(x), status=200)
# #             resp.headers['Access-Control-Allow-Origin'] = '*'
# #             return resp
# #             # return Response(jsonify(x), status=200, mimetype='application/json')
# #     resp = Response(status=404)
# #     resp.headers['Access-Control-Allow-Origin'] = '*'
# #     return resp
