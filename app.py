from flask import Flask, render_template, request, url_for, redirect
from SpurGear import calculate

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def sp_input():
    if request.method == 'POST':
        p = int(request.form['P'])
        n1 = int(request.form['N1'])
        choice = int(request.form['choice'])
        if choice == 1:
            return redirect(url_for('choice_1', p=p, n1=n1))
        else:
            return redirect(url_for('choice_2', p=p, n1=n1))
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
        p = int(request.values.get('p'))
        n1 = int(request.values.get('n1'))
        i = float(request.form['i'])
        return redirect(url_for('spur_input', p=p, n1=n1, i=i))
    return render_template('Choice1.html')


@app.route('/choice2', methods=['GET', 'POST'])
def choice_2():
    if request.method == 'POST':
        p = int(request.values.get('p'))
        n1 = int(request.values.get('n1'))
        n2 = int(request.form['N2'])
        i = round(n1 / n2, 2)
        if i > 5:
            i = round(pow(i, 1 / 2), 2)
        return redirect(url_for('spur_input', p=p, n1=n1, i=i))
    return render_template('Choice2.html')


@app.route('/input', methods=['GET', 'POST'])
def spur_input():
    if request.method == 'POST':
        p = float(request.values.get('p'))
        n1 = float(request.values.get('n1'))
        i = float(request.values.get('i'))
        sf = float(request.form['sf'])
        pres_ang = int(request.form['pres_ang'])
        gear_qua = int(request.form['gear_qua'])
        pinion = int(request.form['pinion'])
        FoS1 = float(request.form['FoS1'])
        BHN1 = float(request.form['BHN1'])
        gear = int(request.form['gear'])
        FoS2 = float(request.form['FoS2'])
        BHN2 = float(request.form['BHN2'])
        m = int(request.form['m'])
        psi = int(request.form['psi'])
        u = int(request.form['u'])
        e1 = float(request.form['E1'])
        e2 = float(request.form['E2'])
        # = int(request.form[''])
        # = int(request.form[''])
        # = int(request.form[''])

        pd, z1, z2, y1, y2, benstr1, benstr2, BHN, weak1, weak2, m1, b, fs, fd, fw, n12, n22, round2 = calculate(p, n1,
                                                                                                                 i, sf,
                                                                                                                 pinion,
                                                                                                                 FoS1,
                                                                                                                 BHN1,
                                                                                                                 gear,
                                                                                                                 FoS2,
                                                                                                                 BHN2,
                                                                                                                 m, psi,
                                                                                                                 u,
                                                                                                                 gear_qua,
                                                                                                                 pres_ang,
                                                                                                                 e1,
                                                                                                                 e2)
        # return str(sf) + str(press_ang)+str(gear_qua)+str(pinion)+str(FoS1)+str(BHN1)+str(gear)+str(FoS2)+str(BHN2)
        return render_template('Output.html', i=i, p=p, n1=n1, pd=pd, z1=z1, z2=z2, y1=y1, y2=y2, benstr1=benstr1,
                               benstr2=benstr2, BHN=BHN, weak1=weak1, weak2=weak2, m1=m1, b=b, fs=fs, fd=fd, fw=fw,
                               n12=n12, n22=n22, round2=round2)
    return render_template('SpurGear.html')


if __name__ == '__main__':
    app.run(debug=True)
