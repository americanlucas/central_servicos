# Classe DAO para a entidade "tb_prestador"
from database.model_dao import DAO


class PrestadorDAO(DAO):
    def __init__(self):
        super().__init__("tb_prestador", "id_prestador")