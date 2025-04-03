import sqlite3 
from PyQt5.QtWidgets import QTableWidget

class banco:
    def __init__(self,nome = "efeitos.db"):
        self.nome=nome

    def conectar(self):
        conexao=sqlite3.connect(self.nome)

    def fechar_conexao(self):
        try:
            self.conexao.close()
        except:
            return "Faio"
        
    def inserir_dados(self): #infomar o nome da tabela,os campos
        campos_tabela = [] #lista com o nome dos campos que serao inseridos
        qtd = ('?')
        cursor = self.conexao.cursor()

        #o nome que deve ser substituido
        try:
            cursor.execute(f'''INSERT INTO SALVOS ({campos_tabela}))        
                                VALUES({qtd})''',campos_tabela)
            
        except:
            return "Erro ao inserir"    

    def selecionar_tudo(self,SALVOS):
        try:
            cursor=self.conexao.cursor()
            cursor.execute(f"SELECT * FROM {SALVOS}")
            dados= cursor.fetchall()
            return dados
        except:
            return "Erro de cosnulta"

    def buscar_dados(self):
        resultado =self.selecionar_tudo()

        self.tabela.clearContents()
        self.tabela.setRowCount(len(resultado))

        for linha, texto in  enumerate(resultado):

            for coluna, dado in  enumerate(texto):
                self.tabela.setitem(linha,coluna,QTableWidget(str(dado)))


