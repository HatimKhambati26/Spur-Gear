from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def sp_input():
    if request.method == 'POST':
        p = int(request.form['P'])
        n1 = int(request.form['N1'])
        choice = int(request.form['choice'])
        if choice == 1:
            return redirect(url_for('choice_1'))
        else:
            return redirect(url_for('choice_2', n1=n1))
    else:
        return render_template('input.html')


# @app.route('/', methods=['POST'])
# def my_form_post():
#     p = int(request.form['P'])
#     n1 = int(request.form['N1'])
#     choice = int(request.form['choice'])
#     if choice == 1:
#         return redirect(url_for('choice_1'))
#     else:
#         return redirect(url_for('choice_2', n1=n1))


@app.route('/choice1', methods=['GET', 'POST'])
def choice_1():
    if request.method == 'POST':
        i = int(request.form['i'])
        return "Value of i: " + str(i)
    return render_template('Choice1.html')


@app.route('/choice2', methods=['GET', 'POST'])
def choice_2():
    if request.method == 'POST':
        n1 = int(request.values.get('n1'))
        n2 = int(request.form['N2'])
        i = round(n1 / n2, 2)
        if i > 5:
            i = round(pow(i, 1 / 2), 2)
        return redirect(url_for('spur_input'))
    return render_template('Choice2.html')


@app.route('/input', methods=['GET', 'POST'])
def spur_input():
    if request.method == 'POST':
        sf = int(request.form['sf'])
        press_ang = int(request.form['press_ang'])
        gear_qua = int(request.form['gear_qua'])
        pinion = int(request.form['pinion'])
        FoS1 = int(request.form['FoS1'])
        BHN1 = int(request.form['BHN1'])
        gear = int(request.form['gear'])
        FoS2 = int(request.form['FoS2'])
        BHN2 = int(request.form['BHN2'])
        # = int(request.form[''])
        return str(sf) + str(press_ang)+str(gear_qua)+str(pinion)+str(FoS1)+str(BHN1)+str(gear)+str(FoS2)+str(BHN2)
    return render_template('SpurGear.html')


if __name__ == '__main__':
    app.run(debug=True)
