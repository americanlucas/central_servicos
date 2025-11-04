from flask import Blueprint, render_template, request, redirect, url_for, flash
from database.local_dao import LocalDAO
from database.setor_dao import SetorDAO

local_bp = Blueprint('local', __name__, url_prefix='/adm/local')


@local_bp.route('/incluir', methods=['GET', 'POST'])
def incluir():
    dao = SetorDAO()
    lst_setores = dao.read_by_filters([('sts_setor', '=', 'A')])
    return render_template('adm/local/incluir.html', msg="", css_msg="", lst_setores=lst_setores)

@local_bp.route('/salvar_incluir', methods=['POST'])  # /adm/local/salvar_incluir
def salvar_incluir():
    dao = LocalDAO()
    local = dao.new_object()
    dao = SetorDAO()
    lst_setores = dao.read_by_filters([('sts_setor', '=', 'A')])

    local.nme_local = request.form['nme_local']
    local.lat_local = request.form['lat_local']
    local.lgt_local = request.form['lgt_local']
    local.sts_local = request.form['sts_local']
    local.cod_setor = request.form['cod_setor']
    if dao.insert(local):
        msg = f"Local {local.nme_local} inserido com sucesso!"
        css_msg = "sucesso"
    else:
        msg = "Erro ao tentar incluir local!"
        css_msg = "erro"

    return render_template('adm/local/incluir.html', msg=msg, css_msg=css_msg, lst_setores=lst_setores)

@local_bp.route('/consultar', methods=['GET'])
def consultar():
    return render_template('adm/local/consultar.html', locais=[], filtro_usado='')


@local_bp.route('/roda_consultar', methods=['POST'])
def roda_consultar():
    nme_local = request.form['nme_local']
    filtro_usado = f'Nome do Local: {nme_local or "Não informado"}'
    dao = LocalDAO()
    locais = dao.read_by_like('nme_local', nme_local)
    return render_template('adm/local/consultar.html', locais=locais, filtro_usado=filtro_usado)

@local_bp.route('/atualizar')  # /adm/local/atualizar
def atualizar():
    return render_template('adm/local/atualizar.html', locais=[], filtro_usado='')


@local_bp.route('/roda_atualizar', methods=['POST'])  # /adm/local/rodar_atualizar
def roda_atualizar():
    nme_local = request.form['nme_local']
    filtro_usado = f'Nome do Local: {nme_local or "Não informado"}'
    dao = LocalDAO()
    locais = dao.read_by_like('nme_local', nme_local)
    return render_template('adm/local/atualizar.html', locais=locais, filtro_usado=filtro_usado)



@local_bp.route('/alterar/<int:idt>')  # /adm/local/alterar/número
def alterar(idt):
   dao = LocalDAO()
   local = dao.read_by_idt(idt)
   setor_dao = SetorDAO()
   lst_setores = setor_dao.read_all()
   return render_template('adm/local/alterar.html', msg="", css_msg="", local=local, lst_setores=lst_setores)

@local_bp.route('/salva_alterar', methods=['POST'])  # /adm/local/alterar/número
def salva_alterar():
   dao = LocalDAO()
   idt_local = int(request.form.get('idt_local'))
   local = dao.read_by_idt(idt_local)

   local.nme_local = request.form['nme_local']
   local.lat_local = request.form['lat_local']
   local.lgt_local = request.form['lgt_local']
   local.sts_local = request.form['sts_local']
   local.cod_setor = request.form['cod_setor']
   if dao.update(local):
       msg = f'Local {local.nme_local} alterado com sucesso!'
       css_msg = "sucesso"
   else:
       msg = 'Falha ao tentar alterar local!'
       css_msg = "erro"


   return render_template('adm/local/alterar.html', msg=msg, css_msg=css_msg, local=local)


@local_bp.route('/excluir/<int:idt>')
def excluir(idt):
    dao = LocalDAO()
    if dao.delete(idt):
        msg = 'Local excluído com sucesso!'
        css_msg = "sucesso"
    else:
        msg = 'Falha ao tentar excluir local! Verifique se existe alguma dependência!'
        css_msg = "erro"

    return redirect('/adm/local/atualizar')
    # return render_template('adm/local/atualizar.html', msg=msg, css_msg=css_msg, locais=[], filtro_usado='')