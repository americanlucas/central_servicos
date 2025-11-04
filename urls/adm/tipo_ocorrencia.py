from flask import Blueprint, render_template, request, redirect, url_for, flash
from database.tipo_ocorrencia_dao import TipoOcorrenciaDAO

tipo_ocorrencia_bp = Blueprint('tipo_ocorrencia', __name__, url_prefix='/adm/tipo_ocorrencia')


@tipo_ocorrencia_bp.route('/incluir')  # /adm/tipo_ocorrencia/incluir
def incluir():
    return render_template('adm/tipo_ocorrencia/incluir.html', msg="", css_msg="")


@tipo_ocorrencia_bp.route('/salvar_incluir', methods=['POST'])  # /adm/tipo_ocorrencia/salvar_incluir
def salvar_incluir():
    dao = TipoOcorrenciaDAO()
    tipo_ocorrencia = dao.new_object()
    tipo_ocorrencia.nme_tipo_ocorrencia = request.form['nme_tipo_ocorrencia']
    tipo_ocorrencia.tpo_tipo_ocorrencia = request.form['tpo_tipo_ocorrencia']
    tipo_ocorrencia.sts_tipo_ocorrencia = request.form['sts_tipo_ocorrencia']
    tipo_ocorrencia.txt_modelo_ocorrencia = request.form['txt_modelo_ocorrencia']

    if dao.insert(tipo_ocorrencia):
        msg = f"Ocorrência número {tipo_ocorrencia.idt_tipo_ocorrencia} inserido com sucesso!"
        css_msg = "sucesso"
    else:
        msg = "Erro ao tentar incluir tipo de ocorrência!"
        css_msg = "erro"

    return render_template('adm/tipo_ocorrencia/incluir.html', msg=msg, css_msg=css_msg)


@tipo_ocorrencia_bp.route('/consultar')  # /adm/tipo_ocorrencia/consultar
def consultar():
    return render_template('adm/tipo_ocorrencia/consultar.html', tipos=[], filtro_usado='')


@tipo_ocorrencia_bp.route('/roda_consultar', methods=['POST'])  # /adm/tipo_ocorrencia/roda_consultar
def roda_consultar():
    nme_tipo_ocorrencia = request.form['nme_tipo_ocorrencia']
    filtro_usado = f'Nome do Tipo de Ocorrência: {nme_tipo_ocorrencia or "Não informado"}'
    dao = TipoOcorrenciaDAO()
    tipos = dao.read_by_like('nme_tipo_ocorrencia', nme_tipo_ocorrencia)
    return render_template('adm/tipo_ocorrencia/consultar.html', tipos=tipos, filtro_usado=filtro_usado)


@tipo_ocorrencia_bp.route('/atualizar')  # /adm/tipo_ocorrencia/atualizar
def atualizar():
    return render_template('adm/tipo_ocorrencia/atualizar.html', tipos=[], filtro_usado='')


@tipo_ocorrencia_bp.route('/roda_atualizar', methods=['POST'])  # /adm/tipo_ocorrencia/rodar_atualizar
def roda_atualizar():
    nme_tipo_ocorrencia = request.form['nme_tipo_ocorrencia']
    filtro_usado = f'Nome do Tipo de Ocorrência: {nme_tipo_ocorrencia or "Não informado"}'
    dao = TipoOcorrenciaDAO()
    tipos = dao.read_by_like('nme_tipo_ocorrencia', nme_tipo_ocorrencia)
    return render_template('adm/tipo_ocorrencia/atualizar.html', tipos=tipos, filtro_usado=filtro_usado)


@tipo_ocorrencia_bp.route('/excluir/<int:idt>')
def excluir(idt):
    dao = TipoOcorrenciaDAO()
    if dao.delete(idt):
        msg = 'Tipo de Ocorrência excluído com sucesso!'
        css_msg = "sucesso"
    else:
        msg = 'Falha ao tentar excluir tipo de ocorrência! Verifique se existe alguma dependência!'
        css_msg = "erro"

    return redirect('/adm/tipo_ocorrencia/atualizar')
    # return render_template('adm/tipo_ocorrencia/atualizar.html', msg=msg, css_msg=css_msg, tipos=[], filtro_usado='')


@tipo_ocorrencia_bp.route('/alterar/<int:idt>')  # /adm/tipo_ocorrencia/alterar/número
def alterar(idt):
    dao = TipoOcorrenciaDAO()
    tipo_ocorrencia = dao.read_by_idt(idt)
    return render_template('adm/tipo_ocorrencia/alterar.html', msg="", css_msg="", tipo_ocorrencia=tipo_ocorrencia)


@tipo_ocorrencia_bp.route('/salva_alterar', methods=['POST'])  # /adm/tipo_ocorrencia/salva_alterar
def salva_alterar():
    dao = TipoOcorrenciaDAO()
    tipo_ocorrencia = dao.read_by_idt(int(request.form['idt_tipo_ocorrencia']))
    tipo_ocorrencia.nme_tipo_ocorrencia = request.form['nme_tipo_ocorrencia']
    tipo_ocorrencia.tpo_tipo_ocorrencia = request.form['tpo_tipo_ocorrencia']
    tipo_ocorrencia.sts_tipo_ocorrencia = request.form['sts_tipo_ocorrencia']
    tipo_ocorrencia.txt_modelo_ocorrencia = request.form['txt_modelo_ocorrencia']

    if dao.update(tipo_ocorrencia):
        msg = 'Tipo de Ocorrência alterado com sucesso!'
        css_msg = "sucesso"
    else:
        msg = 'Falha ao tentar alterar tipo de ocorrência!'
        css_msg = "erro"

    return render_template('adm/tipo_ocorrencia/alterar.html', msg=msg, css_msg=css_msg,
                           tipo_ocorrencia=tipo_ocorrencia)