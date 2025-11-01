from flask import Flask, render_template

from urls.adm.empregado import empregado_bp
from urls.adm.local import local_bp
from urls.adm.prestador import prestador_bp
from urls.adm.setor import bp_setor
from urls.adm.servico import bp_serv
from urls.adm.tipo_ocorrencia import tipo_ocorrencia_bp

app = Flask(__name__)

app.register_blueprint(bp_setor)
app.register_blueprint(bp_serv)
app.register_blueprint(tipo_ocorrencia_bp)
app.register_blueprint(empregado_bp)
app.register_blueprint(prestador_bp)
app.register_blueprint(local_bp)


@app.route('/')
def cs():
    return render_template('index.html')


@app.route('/menu_adm')
def menu_adm():
    return render_template('menu_adm.html')


@app.route('/menu_pre')
def menu_pre():
    return render_template('menu_pre.html')


@app.route('/menu_sol')
def menu_sol():
    return render_template('menu_sol.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
