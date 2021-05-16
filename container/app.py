from flask import Flask, render_template, request
from simulator import risk_simulator

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/table')
def table():
    return render_template('risk_table.html')


@app.route('/attack', methods=['GET', 'POST'])
def attack():
    if request.method == 'POST':
        defender = request.form['defender']
        probability = request.form['probability']
        result = simulate_attack(defender, probability)
        return render_template('attack_status.html', result=result, defender=defender, probability=probability)

    return render_template('form_attack.html')


@app.route('/defense', methods=['GET', 'POST'])
def defense():
    if request.method == 'POST':
        attacker = request.form['attacker']
        probability = request.form['probability']
        result = simulate_defense(attacker, probability)
        return render_template('defense_status.html', result=result, attacker=attacker, probability=probability)

    return render_template('form_defense.html')


def simulate_attack(defender, percentage):
    try:
        result = str(risk_simulator.BattleSimulator.required_attack_army(int(defender), float(percentage)))
        return result
    except Exception as e:
        return f"Input error, check data format {str(e)}"


def simulate_defense(attacker, percentage):
    try:
        result = str(risk_simulator.BattleSimulator.required_defense_army(int(attacker), float(percentage)))
        return result
    except Exception as e:
        return f"Input error, check data format {str(e)}"