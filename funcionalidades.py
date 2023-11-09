from modulos import *

class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.tel_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    
    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor()
        print("Conectando ao banco de dados")

    def desconeta_bd(self):
        self.conn.close()
        print("Desconectado ao banco de dados")

    def montaTabelas(self):
        self.conecta_bd()
        #criar tabelas 
        self.cursor.execute("CREATE TABLE IF NOT EXISTS clientes (cod INTEGER PRIMARY KEY, nome_cliente CHAR(40) NOT NULL, telefone INTEGER(20), cidade CHAR(40))")
        self.conn.commit()
        print("Banco de dados criado")
        self.desconeta_bd()

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.fone = self.tel_entry.get()
        self.cidade = self.cidade_entry.get()

    def add_Clientes(self):
        self.variaveis()
        if self.nome_entry.get() == "":
            msg = "Para casdastrar um novo cliente é necessario que seja degitado pelo menos um nome"
            messagebox.showinfo("Cadastro de clientes - Aviso!!!", msg)
        else:
            self.conecta_bd()
            self.cursor.execute("INSERT INTO clientes (nome_cliente, telefone, cidade) VALUES (?, ?, ?)", (self.nome, self.fone, self.cidade))
            self.conn.commit()
            self.desconeta_bd()
            self.select_lista()
            self.limpa_tela()

    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("SELECT * FROM clientes ORDER BY nome_cliente ASC")

        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconeta_bd()

    def onDoubleClik(self, event):
        self.limpa_tela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.tel_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)
            
    def deleta_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("DELETE FROM clientes WHERE cod= ?", (self.codigo))
        self.conn.commit()
        self.desconeta_bd()
        self.limpa_tela()
        self.select_lista()

    def alterar_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("UPDATE clientes set nome_cliente = ?, telefone = ?, cidade = ? WHERE cod = ?", (self.nome, self.fone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconeta_bd()
        self.limpa_tela()
        self.select_lista()

    def busca_cliente(self):
        self.conecta_bd()
        self.listaCli.delete(*self.listaCli.get_children())
        
        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute("SELECT cod, nome_cliente, telefone, cidade FROM clientes WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC" % nome)

        buscaNomeCli = self.cursor.fetchall()
        for i in buscaNomeCli:
            self.listaCli.insert("", END, values=i)
        self.limpa_tela()
        self.desconeta_bd()


    def images_base64(self):
        self.btNovo_base64 = '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'

    def calendario(self): 
        self.calendario1 = Calendar(self.aba2, fg="gray75", bg="blue", font=("Times", '9', 'bold'),
                                    locale='pt_br')
        self.calendario1.place(relx=0.5, rely=0.2)
        self.calDate = Button(self.aba2, text="Inserir data", command=self.print_cal)
        self.calDate.place(relx=0.84, rely=0.1, height=25, width=100)
    
    def print_cal(self):
        dataIni = self.calendario1.get_date()
        self.calendario1.destroy()
        self.entry_data.delete(0, END)
        self.entry_data.insert(END, dataIni)
        self.calDate.destroy()