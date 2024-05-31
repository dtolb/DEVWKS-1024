from connexion import FlaskApp
from connexion.resolver import RelativeResolver
from flask import jsonify, request

app = FlaskApp(__name__)

# Mock data
power_configurations = [
    {"id": "config123", "name": "Main Data Center Power Configuration", "status": "active",
        "settings": {"voltage": 240, "frequency": 50.0, "max_power_draw": 1000, "min_power_draw": 300},
        "ai_power_plan_id": "aiPlan456"}
]

ai_power_plans = [
    {"id": "aiPlan456", "name": "Energy Saver AI Plan", "optimized_for": "energy-efficiency",
        "parameters": {"max_voltage": 230, "min_frequency": 49.5, "target_power_saving": 15}}
]

def list_power_configurations():
    return jsonify(power_configurations)

def get_power_configuration(id):
    config = next((item for item in power_configurations if item["id"] == id), None)
    return jsonify(config) if config else ('', 404)

def update_power_configuration(id):
    config = next((item for item in power_configurations if item["id"] == id), None)
    if not config:
        return ('', 404)
    data = request.get_json()
    config.update(data)
    return jsonify(config)

def list_ai_power_plans():
    return jsonify(ai_power_plans)

def get_ai_power_plan(id):
    plan = next((item for item in ai_power_plans if item["id"] == id), None)
    return jsonify(plan) if plan else ('', 404)

def create_ai_power_plan():
    data = request.get_json()
    ai_power_plans.append(data)
    return jsonify(data), 201

app.add_api('openapi.yaml', resolver=RelativeResolver('main'))

if __name__ == '__main__':
    app.run(port=8080)
