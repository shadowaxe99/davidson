```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Constituent Class/Model
class Constituent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    demographics = db.Column(db.String(200))
    concerns = db.Column(db.String(200))

    def __init__(self, name, demographics, concerns):
        self.name = name
        self.demographics = demographics
        self.concerns = concerns

# Constituent Schema
class ConstituentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'demographics', 'concerns')

# Init schema
constituent_schema = ConstituentSchema()
constituents_schema = ConstituentSchema(many=True)

# Create a Constituent
@app.route('/constituent', methods=['POST'])
def add_constituent():
    name = request.json['name']
    demographics = request.json['demographics']
    concerns = request.json['concerns']

    new_constituent = Constituent(name, demographics, concerns)

    db.session.add(new_constituent)
    db.session.commit()

    return constituent_schema.jsonify(new_constituent)

# Get All Constituents
@app.route('/constituent', methods=['GET'])
def get_constituents():
    all_constituents = Constituent.query.all()
    result = constituents_schema.dump(all_constituents)
    return jsonify(result)

# Get Single Constituents
@app.route('/constituent/<id>', methods=['GET'])
def get_constituent(id):
    constituent = Constituent.query.get(id)
    return constituent_schema.jsonify(constituent)

# Update a Constituent
@app.route('/constituent/<id>', methods=['PUT'])
def update_constituent(id):
    constituent = Constituent.query.get(id)

    name = request.json['name']
    demographics = request.json['demographics']
    concerns = request.json['concerns']

    constituent.name = name
    constituent.demographics = demographics
    constituent.concerns = concerns

    db.session.commit()

    return constituent_schema.jsonify(constituent)

# Delete Constituent
@app.route('/constituent/<id>', methods=['DELETE'])
def delete_constituent(id):
    constituent = Constituent.query.get(id)
    db.session.delete(constituent)
    db.session.commit()

    return constituent_schema.jsonify(constituent)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
```