from flask import Blueprint, render_template, request, redirect, url_for, flash
from database.empregado_dao import EmpregadoDAO
from database.local_dao import LocalDAO
from database.setor_dao import SetorDAO

empregado_bp = Blueprint('empregado', __name__, url_prefix='/adm/empregado')


@empregado_bp.route('/incluir')
def incluir():
    local_dao = LocalDAO()
    lst_locais = local_dao.read_all()
    return render_template('adm/empregado/incluir.html', msg='', css_msg='', lst_locais=lst_locais)


@empregado_bp.route('/salvar_incluir', methods=["POST"])
def salvar_incluir():
    dao = EmpregadoDAO()
    empregado = dao.new_object()
    local_dao = LocalDAO()
    lst_locais = local_dao.read_all()

    empregado.eml_empregado = request.form['eml_empregado']
    empregado.mat_empregado = request.form['mat_empregado']
    empregado.nme_empregado = request.form['nme_empregado']
    empregado.sts_empregado = request.form['sts_empregado']
    empregado.tel_empregado = request.form.get('tel_empregado', '')
    empregado.rml_empregado = request.form.get('rml_empregado', '')
    empregado.pwd_empregado = request.form.get('pwd_empregado', '')
    empregado.cod_local = request.form['cod_local']
    if dao.insert(empregado):
        msg = f"Empregado {empregado.nme_empregado} inserido com sucesso!"
        css_msg = 'sucesso'
    else:
        msg = "Erro ao tentar incluir empregado!"
        css_msg = "erro"

    return render_template('adm/empregado/incluir.html', msg=msg, css_msg=css_msg, lst_locais=lst_locais)


@empregado_bp.route('/consultar')
def consultar():
    return render_template('adm/empregado/consultar.html', empregados=[], filtro_usado='')


@empregado_bp.route('/roda_consultar', methods=['POST'])
def roda_consultar():
    # TRY
    nme_empregado = request.form["nme_empregado"]
    filtro_usado = f"Nome do Empregado: {nme_empregado}"
    dao = EmpregadoDAO()
    empregado = dao.read_by_like("nme_empregado", nme_empregado)

    return render_template('adm/empregado/consultar.html', empregado=empregado, filtro_usado=filtro_usado)


@empregado_bp.route('/alterar/<int:idt>')
def alterar(idt):
    dao = EmpregadoDAO()
    empregado = dao.read_by_idt(idt)

    # Busca setores para o dropdown
    local_dao = LocalDAO()
    lst_locais = local_dao.read_all()

    return render_template('adm/empregado/alterar.html', empregado=empregado, lst_locais=lst_locais)

@empregado_bp.route('/salva_alterar', methods=['POST'])
def salva_alterar():
    dao = EmpregadoDAO()
    empregado = dao.read_by_idt(int(request.form['idt_empregado']))
    local_dao = LocalDAO()
    lst_locais = local_dao.read_all()

    empregado.idt_empregado = request.form['idt_empregado']
    empregado.eml_empregado = request.form['eml_empregado']
    empregado.mat_empregado = request.form['mat_empregado']
    empregado.nme_empregado = request.form['nme_empregado']
    empregado.sts_empregado = request.form['sts_empregado']
    empregado.tel_empregado = request.form.get('tel_empregado', '')
    empregado.rml_empregado = request.form.get('rml_empregado', '')
    empregado.pwd_empregado = request.form.get('pwd_empregado', '')
    empregado.cod_local = request.form['cod_local']

    if dao.update(empregado):
        msg = f"Empregado {empregado.nme_empregado} alterado com sucesso"
        css_msg = f"sucesso"
    else:
        msg = f"Falha ao tentar alterar prestador!"
        css_msg = f"erro"

    return render_template('adm/empregado/alterar.html', msg=msg, css_msg=css_msg, empregado=empregado, lst_locais=lst_locais)


@empregado_bp.route('/atualizar')  # /adm/empregado/atualizar
def atualizar():
    return render_template('adm/empregado/atualizar.html', empregado=[], filtro_usado='')


@empregado_bp.route('/roda_atualizar', methods=['POST'])  # /adm/empregado/rodar_atualizar
def roda_atualizar():
    nme_empregado = request.form['nme_empregado']
    filtro_usado = f'Nome do Empregado: {nme_empregado}'
    dao = EmpregadoDAO()
    empregado = dao.read_by_like('nme_empregado', nme_empregado)
    return render_template('adm/empregado/atualizar.html', empregado=empregado, filtro_usado=filtro_usado)




@empregado_bp.route('/excluir/<int:idt>')
def excluir(idt):
    dao = EmpregadoDAO()

    if dao.delete(idt):
        msg = 'Empregado excluído com sucesso!'
        css_msg = "sucesso"
    else:
        msg = 'Falha ao tentar excluir empregado! Verifique se existe alguma dependência!'
        css_msg = "erro"

    return redirect('/adm/empregado/atualizar')
    #return render_template('adm/empregado/alterar.html', msg=msg, css_msg=css_msg, empregado=[], filtro_usado='')
