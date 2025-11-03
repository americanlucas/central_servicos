from flask import Blueprint, render_template, request, redirect, url_for, flash
from database.prestador_dao import PrestadorDAO
from database.setor_dao import SetorDAO

prestador_bp = Blueprint('prestador', __name__, url_prefix='/adm/prestador')


@prestador_bp.route('/incluir')
def incluir():
    setor_dao = SetorDAO()
    lst_setores = setor_dao.read_by_filters([('sts_setor', '=', 'A')])
    return render_template('adm/prestador/incluir.html', msg='', css_msg='', lst_setores=lst_setores)

@prestador_bp.route('/salvar_incluir', methods=['POST'])
def salvar_incluir():
    dao = PrestadorDAO()
    prestador = dao.new_object()
    setor_dao = SetorDAO()
    lst_setores = setor_dao.read_by_filters([('sts_setor', '=', 'A')])

    prestador.mat_prestador = request.form.get('mat_prestador', '')
    prestador.nme_prestador = request.form['nme_prestador']
    prestador.eml_prestador = request.form['eml_prestador']
    prestador.sts_prestador = request.form['sts_prestador']
    prestador.tel_prestador = request.form.get('tel_prestador', '')
    prestador.rml_prestador = request.form.get('rml_prestador', '')
    prestador.pwd_prestador = request.form.get('pwd_prestador', '')
    prestador.cod_setor = request.form['cod_setor']

    if dao.insert(prestador):
        msg = f"Prestador {prestador.nme_prestador} inserido com sucesso"
        css_msg = "sucesso"
    else:
        msg = f"Erro ao tentar incluir prestador!"
        css_msg = "erro"

    return render_template('adm/prestador/incluir.html', msg=msg, css_msg=css_msg, lst_setores=lst_setores)


@prestador_bp.route('/consultar', methods=['GET'])
def consultar():
    return render_template('adm/prestador/consultar.html', prestadores=[], filtro_usado='')


@prestador_bp.route('/roda_consultar', methods=['POST'])
def roda_consultar():
    nme_prestador = request.form["nme_prestador"]
    filtro_usado = f"Nome do Empregado: {nme_prestador}"
    dao = PrestadorDAO()
    prestador = dao.read_by_like("nme_prestador", nme_prestador)

    return render_template('adm/prestador/consultar.html', prestador=prestador, filtro_usado=filtro_usado)

@prestador_bp.route('/atualizar')  # /adm/prestador/atualizar
def atualizar():
    return render_template('adm/prestador/atualizar.html', prestadores=[], filtro_usado='')


@prestador_bp.route('/roda_atualizar', methods=['POST'])  # /adm/prestador/rodar_atualizar
def roda_atualizar():
    nme_prestador = request.form['nme_prestador']
    filtro_usado = f'Nome do Prestador: {nme_prestador}'
    dao = PrestadorDAO()
    prestadores = dao.read_by_like('nme_prestador', nme_prestador)
    return render_template('adm/prestador/atualizar.html', prestadores=prestadores, filtro_usado=filtro_usado)



@prestador_bp.route('/alterar/<int:idt>')
def alterar(idt):
    dao = PrestadorDAO()
    prestador = dao.read_by_idt(idt)
    setor_dao = SetorDAO()
    lst_setores = setor_dao.read_by_filters([('sts_setor', '=', 'A')])

    return render_template('adm/prestador/alterar.html', prestador=prestador, msg='', css_msg='', lst_setores=lst_setores)

@prestador_bp.route('/salva_alterar', methods=['POST'])
def salva_alterar():
    dao = PrestadorDAO()
    prestador = dao.new_object()
    setor_dao = SetorDAO()
    lst_setores = setor_dao.read_by_filters([('sts_setor', '=', 'A')])

    prestador.mat_prestador = request.form.get('mat_prestador', '')
    prestador.nme_prestador = request.form['nme_prestador']
    prestador.eml_prestador = request.form['eml_prestador']
    prestador.sts_prestador = request.form['sts_prestador']
    prestador.tel_prestador = request.form.get('tel_prestador', '')
    prestador.rml_prestador = request.form.get('rml_prestador', '')
    prestador.pwd_prestador = request.form.get('pwd_prestador', '')
    prestador.cod_setor = request.form['cod_setor']

    if dao.update(prestador):
        msg = f'Prestador {prestador.nme_prestador} alterado com sucesso'
        css_msg = 'sucesso'
    else:
        msg = "Falha ao tentar alterar prestador!"
        css_msg = "erro"

    return render_template('adm/prestador/alterar.html', msg=msg, css_msg=css_msg, prestador=prestador, lst_setores=lst_setores)

@prestador_bp.route('/excluir/<int:idt>')
def excluir(idt):
    dao = PrestadorDAO()
    if dao.delete(idt):
        msg = 'Prestador excluído com sucesso!'
        css_msg = "sucesso"
    else:
        msg = 'Falha ao tentar excluir prestador! Verifique se existe alguma dependência!'
        css_msg = "erro"

    return redirect('/adm/prestador/atualizar')
    # return render_template('adm/prestador/atualizar.html', msg=msg, css_msg=css_msg, prestadores=[], filtro_usado='')

