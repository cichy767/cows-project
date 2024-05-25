from flask import request, jsonify
import uuid
from datetime import datetime
from app import app
from models import db, Cow


# Create a new cow
@app.route('/cows', methods=['POST'])
def add_cow():
    data = request.get_json()
    new_cow = Cow(
        id=str(uuid.uuid4()),
        name=data['name'],
        sex=data['sex'],
        birthdate=datetime.strptime(data['birthdate'], '%Y-%m-%dT%H:%M:%S'),
        condition=data['condition'],
        weight_mass_kg=data['weight']['mass_kg'],
        weight_last_measured=datetime.strptime(data['weight']['last_measured'], '%Y-%m-%dT%H:%M:%S'),
        feeding_amount_kg=data['feeding']['amount_kg'],
        feeding_cron_schedule=data['feeding']['cron_schedule'],
        feeding_last_measured=datetime.strptime(data['feeding']['last_measured'], '%Y-%m-%dT%H:%M:%S'),
        milk_last_milk=datetime.strptime(data['milk_production']['last_milk'], '%Y-%m-%dT%H:%M:%S'),
        milk_cron_schedule=data['milk_production']['cron_schedule'],
        milk_amount_l=data['milk_production']['amount_l'],
        has_calves=data['has_calves']
    )
    db.session.add(new_cow)
    db.session.commit()
    return jsonify({"message": "Cow added"}), 201


# Get all cows
@app.route('/cows', methods=['GET'])
def get_cows():
    cows = Cow.query.all()
    result = []
    for cow in cows:
        result.append({
            'id': cow.id,
            'name': cow.name,
            'sex': cow.sex,
            'birthdate': cow.birthdate.isoformat(),
            'condition': cow.condition,
            'weight': {
                'mass_kg': cow.weight_mass_kg,
                'last_measured': cow.weight_last_measured.isoformat()
            },
            'feeding': {
                'amount_kg': cow.feeding_amount_kg,
                'cron_schedule': cow.feeding_cron_schedule,
                'last_measured': cow.feeding_last_measured.isoformat()
            },
            'milk_production': {
                'last_milk': cow.milk_last_milk.isoformat(),
                'cron_schedule': cow.milk_cron_schedule,
                'amount_l': cow.milk_amount_l
            },
            'has_calves': cow.has_calves
        })
    return jsonify(result), 200


# Update a cow
@app.route('/cows/<id>', methods=['PUT'])
def update_cow(id):
    data = request.get_json()
    cow = Cow.query.get(id)
    if not cow:
        return jsonify({"message": "Cow not found"}), 404

    cow.name = data['name']
    cow.sex = data['sex']
    cow.birthdate = datetime.strptime(data['birthdate'], '%Y-%m-%dT%H:%M:%S')
    cow.condition = data['condition']
    cow.weight_mass_kg = data['weight']['mass_kg']
    cow.weight_last_measured = datetime.strptime(data['weight']['last_measured'], '%Y-%m-%dT%H:%M:%S')
    cow.feeding_amount_kg = data['feeding']['amount_kg']
    cow.feeding_cron_schedule = data['feeding']['cron_schedule']
    cow.feeding_last_measured = datetime.strptime(data['feeding']['last_measured'], '%Y-%m-%dT%H:%M:%S')
    cow.milk_last_milk = datetime.strptime(data['milk_production']['last_milk'], '%Y-%m-%dT%H:%M:%S')
    cow.milk_cron_schedule = data['milk_production']['cron_schedule']
    cow.milk_amount_l = data['milk_production']['amount_l']
    cow.has_calves = data['has_calves']

    db.session.commit()
    return jsonify({"message": "Cow updated"}), 200


# Delete a cow
@app.route('/cows/<id>', methods=['DELETE'])
def delete_cow(id):
    cow = Cow.query.get(id)
    if not cow:
        return jsonify({"message": "Cow not found"}), 404

    db.session.delete(cow)
    db.session.commit()
    return jsonify({"message": "Cow deleted"}), 200


# Filter cows
@app.route('/cows/filter', methods=['GET'])
def filter_cows():
    sex = request.args.get('sex')
    cows = Cow.query.filter_by(sex=sex).all()
    result = []
    for cow in cows:
        result.append({
            'id': cow.id,
            'name': cow.name,
            'sex': cow.sex,
            'birthdate': cow.birthdate.isoformat(),
            'condition': cow.condition,
            'weight': {
                'mass_kg': cow.weight_mass_kg,
                'last_measured': cow.weight_last_measured.isoformat()
            },
            'feeding': {
                'amount_kg': cow.feeding_amount_kg,
                'cron_schedule': cow.feeding_cron_schedule,
                'last_measured': cow.feeding_last_measured.isoformat()
            },
            'milk_production': {
                'last_milk': cow.milk_last_milk.isoformat(),
                'cron_schedule': cow.milk_cron_schedule,
                'amount_l': cow.milk_amount_l
            },
            'has_calves': cow.has_calves
        })
    return jsonify(result), 200
