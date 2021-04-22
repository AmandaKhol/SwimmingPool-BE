
from flask import Flask, jsonify
from flask_restful import Resource


centers = [
        {
          "id": "al",
          "name": "Aluche",
          "hours": ["10:30", "12:00", "'13:30'","11:00", "12:30", "14:00"],
          "streets": [
            {
              "id": "'1'",
              "hours": ["'10:30'", "'12:00'", "'13:30'"]
            },
            {
              "id": "2",
              "hours": ["'11:00'", "'12:30'", "'14:00'"]
            }
          ]
        },
        {
          "id": "ch",
          "name": "Carabanchel",
          "hours": ["15:00", "16:30", "18:00", "15:30","17:00", "18:30"],
          "streets": [
            { "id": "3", "hours": ["'15:00'", "16:30", "18:00"] },
            { "id": "4", "hours": ["'15:30'","17:00", "18:30"] }
          ]
        },
        {
          "id": "'vk'",
          "name": "Vallecas",
          "hours": ["18:30", "20:00", "21:30", "18:00", "19:30", "21:00"],
          "streets": [
            { "id": "'5'", "hours": ["'18:30'", "'20:00'", "21:30"] },
            { "id": "'6'", "hours": ["18:00", "'19:30'", "'21:00'"] }
          ]
        }
]


class HourList(Resource):
    def get(self):
        hoursInfo = []
        for center in centers:
            pool_info = {
                'name': center['name'],
             'hours': center['hours']
            }
            hoursInfo.append(pool_info)
        return jsonify({'hours': hoursInfo})