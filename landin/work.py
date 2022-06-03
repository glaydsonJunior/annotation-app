from flask import Flask, render_template, url_for, request, session, redirect
from flask_session import Session
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/', methods=['POST','GET'])
def notes():
    if session.get('notas') is None:
        session["notas"] = []
    if request.method == 'POST':
        anotacao = request.form['conteudo']
        if anotacao is None or anotacao == ' ':
            return 404
        session["notas"].append(anotacao)
        return render_template('PaginaInicial.html', note=session["notas"],notinha=anotacao)
    else:
        return render_template('PaginaInicial.html', note=session["notas"])

@app.route('/back/<delete>', methods=['POST','GET'])
def back(delete):
    if request.method == 'POST':
        session["notas"].remove(delete)
        return redirect(url_for('notes'))
    else:
        return render_template("stop.html")
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
