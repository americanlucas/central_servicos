# Classe DAO para a entidade "tb_local"
from database.model_dao import DAO


class LocalDAO(DAO):
    def __init__(self):
        super().__init__("tb_local", "id_local")