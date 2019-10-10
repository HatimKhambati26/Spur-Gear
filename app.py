from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def spear_input():
    if request.method == 'POST':
        p = int(request.form['P'])
        n1 = int(request.form['N1'])
        choice = int(request.form['choice'])
        if choice == 1:
            return redirect(url_for('choice_1'))
        else:
            return redirect(url_for('choice_2', n1=n1))
    else:
        return render_template('SpurGear.html')


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
        return "Value of i: " + str(i)
    return render_template('Choice2.html')


if __name__ == '__main__':
    app.run(debug=True)
