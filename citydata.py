# cities_one = ['Blore','Hubli','Dharwad','Udupi','Berlin','Stuttgart','Hamburg','Frankfurt','Newyork','LA','Nevada','Dallas']
# cities_two = ['sydney','melbourne','perth','brisbane','adelaide','canberaa','hobart','darwin','goldcoast','albany','mackay']


from flask import Flask, jsonify,Response
import requests
import random

app = Flask(__name__)
@app.route('/')
def datasearch():
  db = [
            {'name': 'Sandeep', 'age': 27, 'address': 'mazha'},
            {'name':'Nishanth','age':25, 'address':'blore'},
        ]

  d = (random.choice(db))
  print(d)
  return jsonify(d)







if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0')
