# cities_one = ['Blore','Hubli','Dharwad','Udupi','Berlin','Stuttgart','Hamburg','Frankfurt','Newyork','LA','Nevada','Dallas']
# cities_two = ['sydney','melbourne','perth','brisbane','adelaide','canberaa','hobart','darwin','goldcoast','albany','mackay']


from flask import Flask, jsonify,Response
import requests
import random

app = Flask(__name__)
@app.route('/')
def datasearch():
  db = [
            {'Name': 'Sam', 'Age': 27,'Job':'Engineer','Hometown':'bangalore', 'Loc': 'btm'},
            {'Name':'ram','Age':25,'Job':'Engineer','Hometown':'bangalore', 'Loc':'blore'},
            {'Name':'ramesh','Age':24,'Job':'Engineer','Hometown':'bangalore', 'Loc':'blore'},
            {'Name':'suresh','Age':23,'Job':'Engineer','Hometown':'bangalore', 'Loc':'blore'},
        ]

  d = (random.choice(db))
  print(d)
  return jsonify(d)







if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0')
