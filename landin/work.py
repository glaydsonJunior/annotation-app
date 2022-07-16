from flask import Flask, render_template, url_for, request, redirect
from flask_session import Session
app = Flask(__name__)

storage = []


@app.route('/', methods=['POST','GET'])
def notes():

    if request.method == 'POST':
        note = request.form['content']

        if note is None or note == ' ':
            return 404
        storage.append(note)
        return render_template('PaginaInicial.html', storage=storage)

    else:
        return render_template('PaginaInicial.html', storage=storage)


@app.route('/back/<delete>', methods=['POST','GET'])
def back(delete):

    if request.method == 'POST':
        storage.remove(delete)
        return redirect(url_for('notes'))

    else:
        return render_template("stop.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
