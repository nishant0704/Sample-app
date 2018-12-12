from flask import Flask,render_template,request,jsonify, Response
from json import dumps
import re

persons = [
    {
        'Name':'karthik',
        'Age':'27',
        'Job':'Founder',
        'Hometown':'Udupi',
        'Loc':'blore',

    },
    {
        'Name':'Sandeep',
        'Age':'27',
        'Job':'Engineer',
        'Hometown':'Udupi',
        'Loc':'blore',
    },
    {
        'Name':'Manu',
        'Age':'27',
        'Job':'Operations',
        'Hometown':'Tumkur',
        'Loc':'blore',
    },
    {
        'Name':'prashant',
        'Age':'27',
        'Job':'Engineer',
        'Hometown':'Nepal',
        'Loc':'blore',
    },
    {
        'Name':'Joice',
        'Age':'24',
        'Job':'Engineer',
        'Hometown':'Kerala',
        'Loc':'blore',
    },
    {
        'Name':'Steev',
        'Age':'25',
        'Job':'Engineer',
        'Hometown':'Kerala',
        'Loc':'blore',
    },
    {
        'Name':'Akhil',
        'Age':'23',
        'Job':'Engineer',
        'Hometown':'Kerala',
        'Loc':'blore',
    },
    {
        'Name':'Nisha',
        'Age':'25',
        'Job':'Engineer',
        'Hometown':'Udupi',
        'Loc':'blore',
    },
    {
        'Name':'Nishant',
        'Age':'25',
        'Job':'Engineer',
        'Hometown':'Udupi',
        'Loc':'blore',
    },
  ]

 # resp = requests.get('main.html')
 # if resp.status_code != 200:
 #     raise ApiError
app = Flask(__name__)

# @app.route('/')
# def main():
#     return render_template('main.html');


@app.route('/search',methods=['GET'])
def retrieve():
    name = str(request.args.get('q'))
    result = []
    rsp = Response("not found",status=404)
    rsp.headers['Access-Control-Allow-Origin'] = '*'
    for x in persons:
        if re.match(str(name),x['Name'],flags=re.IGNORECASE):
            result.append({'Name':x['Name'],'Age':x['Age'],'Loc':x['Loc'],'Job':x['Job'],'Hometown':x['Hometown']})

    if len(result) > 0:
            resp = Response(dumps(result))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp

    return rsp
# @app.route('/search' ,methods=['GET'])
# def get_contact():
#     name = str(request.args.get('q'))
#     result = []
#     for x in persons:
#         # if x['Name'].lower() == name.lower():
#         if re.match(str(name),x['Name'],flags=re.IGNORECASE):
#             result.append({'Name':x['Name'],'Age':x['Age'],'Loc':x['Loc'],'Job':x['Job'],'Hoemtwon':x['Hometown']})
#             # print str(x)
#             resp = Response(dumps(x), status=200)
#             resp.headers['Access-Control-Allow-Origin'] = '*'
#             return resp
#             # return Response(jsonify(x), status=200, mimetype='application/json')
#     resp = Response(status=404)
#     resp.headers['Access-Control-Allow-Origin'] = '*'
#     return resp





if __name__ == "__main__":
    app.run(debug=True)
