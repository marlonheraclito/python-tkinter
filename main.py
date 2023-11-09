from modulos import *
from validyEntry import Validadores
from frameGrad import GradientFrame
from relatorios import Relatorios
from funcionalidades import Funcs
from placeHoder import EntPlaceHolder

root = tix.Tk()

class Aplication(Funcs, Relatorios, Validadores):
    def __init__(self):
        self.root = root
        self.images_base64()
        self.validaEntradas()
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.menus()
        self.montaTabelas()
        self.select_lista()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background="#107db2")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)

    def frames_da_tela(self):
        self.frame1 = Frame(self.root, bd=4, bg="#dfe3ee", highlightbackground="#759fe6", highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame2 = Frame(self.root, bd=4, bg="#dfe3ee", highlightbackground="#759fe6", highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def menus(self):
            menuBar = Menu(self.root)
            self.root.config(menu=menuBar)
            fileMenu = Menu(menuBar)
            fileMenu2 = Menu(menuBar)

            def Quit(): self.root.destroy()

            menuBar.add_cascade(label="Opçoes", menu = fileMenu)
            menuBar.add_cascade(label="Sobre", menu = fileMenu2)

            fileMenu2.add_command(label="Sair", command=Quit)
            fileMenu.add_command(label="Limpa Cliente", command= self.limpa_tela)
          
            fileMenu.add_command(label="Ficha do Cliente", command= self.geraRelatCliente)
            fileMenu.add_command(label="Janela", command= self.janela2)

    def widgets_frame1(self):
        #Criando Abas
        self.abas = ttk.Notebook(self.frame1)
        self.aba1 = GradientFrame(self.abas)
        self.aba2 = Frame(self.abas)

        self.aba1.configure(background="#dfe3ee")
        self.aba2.configure(background="lightgray")
        self.abas.add(self.aba1, text="Aba 1")
        self.abas.add(self.aba2, text="Aba 2")
        self.abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)

        #Criando Canvas 
        self.canvas_bt = Canvas(self.aba1, bd=0, bg='#1e3743', highlightbackground='gray', highlightthickness=5)
        self.canvas_bt.place(relx=0.19, rely=0.08, relwidth=0.23, relheight=0.19)

        #criando do botao limpar 
        self.bt_limpar = Button(self.aba1, text="Limpar", bd=2, bg="#107db2", fg="white", activebackground='#108ecb', 
                                activeforeground='white', font=('verdana', 8, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        

        #criando do botao buscar
        self.bt_buscar = Button(self.aba1, text="Buscar", bd=2, bg="#107db2", fg="white", 
                                activebackground='#108ecb', activeforeground='white', font=('verdana', 8, 'bold'), command=self.busca_cliente)
        self.bt_buscar.place(relx=0.31, rely=0.1, relwidth=0.1, relheight=0.15)

        texto_balaoBuscar = "Digite no campo nome o cliente que deseja pesquisar"
        self.balao_buscar = tix.Balloon(self.aba1)
        self.balao_buscar.bind_widget(self.bt_buscar, balloonmsg=texto_balaoBuscar)

         #Criando botao novo
        self.btnovo =  PhotoImage(data=base64.b64decode(self.btNovo_base64))
        self.btnovo = self.btnovo.subsample(6, 14)

        self.bt_novo = ttk.Button(self.aba1, image=self.btnovo, command=self.add_Clientes)
        self.bt_novo.place(relx=0.6, rely=0.1, width=60, height=30)
       

        #criando do botao Alterar
        self.bt_alterar = Button(self.aba1, text="Alterar", bd=2, bg="#107db2", fg="white", font=('verdana', 8, 'bold'), command=self.alterar_cliente)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        #criando do botao Apagar
        self.bt_apagar = Button(self.aba1, text="Apagar", bd=2, bg="#107db2", fg="white", font=('verdana', 8, 'bold'), command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)


        #criando label e entrada de codigo
        self.lb_codigo = Label(self.aba1, text="Codigo", bg="#dfe3ee", fg="#107db2")
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.aba1, validate="key", validatecommand=self.vcmd2)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.07)

         #criando label e entrada de nome
        self.lb_nome = Label(self.aba1, text="Nome:", bg="#dfe3ee", fg="#107db2")
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = EntPlaceHolder(self.aba1, 'Digite o nome do Cliente')
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.85)

         #criando label e entrada de telefone
        self.lb_tel = Label(self.aba1, text="Telefone:", bg="#dfe3ee", fg="#107db2")
        self.lb_tel.place(relx=0.05, rely=0.6)

        self.tel_entry = Entry(self.aba1)
        self.tel_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

         #criando label e entrada de cidade
        self.lb_cidade = Label(self.aba1, text="Cidade:", bg="#dfe3ee", fg="#107db2")
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.aba1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

        #Criando menu DropDown
        self.tipVar = StringVar()
        self.tipV = ("Solteiro(a)", "Casado(a)", "Divorsiado(a)", "Viuvo(a)")
        self.tipVar.set("Solteiro(a)")
        self.popupMenu = OptionMenu(self.aba2, self.tipVar, *self.tipV)
        self.popupMenu.place(relx=0.05, rely=0.1, relwidth=0.2, relheight=0.2)
        #self.estado_civil = self.tipVar.get()

        #Criando um Calendario 
        self.bt_Calendario = Button(self.aba2, text="Date", command=self.calendario)
        self.bt_Calendario.place(relx=0.5, rely=0.02)
        self.entry_data = Entry(self.aba2, width=10)
        self.entry_data.place(relx=0.5, rely=0.2)
        
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame2, height=3, column=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)


        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        self.scrollLista = Scrollbar(self.frame2, orient="vertical")
        self.listaCli.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.onDoubleClik)

    def janela2(self):
        self.root2 = Toplevel()
        self.root2.title("Janela 2")
        self.root2.configure(background='lightblue')
        self.root2.geometry("600x400")
        self.root2.resizable(False, False)
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.grab_set()

    def validaEntradas(self):
        self.vcmd2 = (self.root.register(self.validate_entry2), "%P")

Aplication()