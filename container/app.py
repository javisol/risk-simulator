from flask import Flask, render_template, request
from simulator import risk_simulator

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/simulate')
def simulate():
    return "Required: " + str(risk_simulator.BattleSimulator.required_army(5, 0.75))


@app.route('/risk', methods=['GET', 'POST'])
def risk_form():
    if request.method == 'POST':
        defender = request.form['defender']
        percentage = request.form['percentage']
        result = simulate(defender, percentage)
        return render_template('risk_form.html', result=result)

    return render_template('risk_form.html')


def simulate(defender, percentage):
    try:
        result = str(risk_simulator.BattleSimulator.required_army(int(defender), float(percentage)))
        return result
    except Exception as e:
        return f"Input error, check data format {str(e)}"
