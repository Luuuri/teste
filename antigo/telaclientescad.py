# importa a biblioteca tkinter e dá o apelido de tk
import tkinter as tk

# importa o ttk, usado aqui para criar a tabela de pedidos
from tkinter import ttk


# cria a classe da janela de clientes
class JanelaClientes:

    # método construtor da classe
    # ele é executado automaticamente quando a classe é criada
    def __init__(self, root):

        # guarda a janela principal dentro da classe
        self.root = root

        # define o título da janela
        self.root.title("Clientes")

        # define o tamanho inicial da janela
        self.root.geometry("900x700")

        # define a cor de fundo da janela principal
        self.root.configure(bg="#f5f5f5")

        # define o tamanho mínimo que a janela pode ter
        self.root.minsize(1100, 650)

        # variável de controle
        # False significa que a área de endereço começa escondida
        self.endereco_visivel = False

        # chama os métodos que montam cada parte da interface
        self.criar_topo()
        self.criar_menu_lateral()
        self.criar_titulo()
        self.criar_formulario_cliente()
        self.criar_area_pedidos()

    # =========================================================
    # MÉTODO: CRIAR TOPO
    # =========================================================
    # cria a barra superior da tela
    def criar_topo(self):

        # frame da barra superior
        self.barra_topo = tk.Frame(self.root, bg="#d9d9d9")

        # posiciona a barra no topo da janela
        # relwidth=1 significa ocupar toda a largura
        # relheight=0.08 significa ocupar 8% da altura
        self.barra_topo.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        # cria o ícone da casa no topo
        self.lbl_icone_casa = tk.Label(self.barra_topo,text="⌂",bg="#d9d9d9",fg="#444444",font=("Arial", 16, "bold"))

        # posiciona o ícone da casa
        self.lbl_icone_casa.place(relx=0.015, rely=0.25)

        # cria o texto "Clientes" no topo
        self.lbl_titulo_topo = tk.Label(self.barra_topo,text="Clientes",bg="#d9d9d9",fg="#222222",font=("Arial", 14, "bold"))

        # posiciona o texto "Clientes"
        self.lbl_titulo_topo.place(relx=0.09, rely=0.28)

        # cria o ícone de configuração no canto direito
        self.lbl_icone_config = tk.Label(self.barra_topo,text="⚙",bg="#d9d9d9",fg="#444444",font=("Arial", 16))

        # posiciona o ícone de configuração
        self.lbl_icone_config.place(relx=0.965, rely=0.25)

    # =========================================================
    # MÉTODO: CRIAR MENU LATERAL
    # =========================================================
    # cria a barra lateral esquerda
    def criar_menu_lateral(self):

        # frame da lateral
        self.menu_lateral = tk.Frame(self.root, bg="#f0f0f0")

        # posiciona a barra lateral
        # ela começa logo abaixo do topo
        self.menu_lateral.place(relx=0, rely=0.08, relwidth=0.06, relheight=0.92)

        # cria o ícone de menu
        self.lbl_menu = tk.Label(
            self.menu_lateral,text="☰",bg="#f0f0f0",fg="#555555",font=("Arial", 18))

        # posiciona o ícone de menu
        self.lbl_menu.place(relx=0.30, rely=0.02)

        # cria o ícone de sair na parte inferior da lateral
        self.lbl_sair = tk.Label(self.menu_lateral,text="⏻",bg="#f0f0f0",fg="#555555",font=("Arial", 18))

        # posiciona o ícone de sair
        self.lbl_sair.place(relx=0.30, rely=0.94)

    # =========================================================
    # MÉTODO: CRIAR TÍTULO DA PÁGINA
    # =========================================================
    # cria a seta de voltar e o título principal
    def criar_titulo(self):

        # cria a seta de voltar
        self.lbl_voltar = tk.Label(self.root,text="←",bg="#f5f5f5",fg="#333333",font=("Arial", 18, "bold"))

        # posiciona a seta
        self.lbl_voltar.place(relx=0.085, rely=0.12)

        # cria o título principal da tela
        self.lbl_titulo = tk.Label(self.root,text="Novo Cliente",bg="#f5f5f5",fg="#111111",font=("Arial", 22, "bold"))

        # posiciona o título
        self.lbl_titulo.place(relx=0.115, rely=0.118)

    # =========================================================
    # MÉTODO: CRIAR FORMULÁRIO DO CLIENTE
    # =========================================================
    # cria a área esquerda com os campos do cliente
    def criar_formulario_cliente(self):

        # frame principal dos campos
        self.area_formulario = tk.Frame(self.root, bg="#f5f5f5")

        # posiciona essa área na parte esquerda da tela
        self.area_formulario.place(relx=0.08, rely=0.18, relwidth=0.30, relheight=0.70)

        # cria os campos principais do cliente
        # esse método reaproveita o mesmo modelo para vários campos
        self.criar_campo(self.area_formulario, "Nome *", 0.00, "ent_nome")
        self.criar_campo(self.area_formulario, "Telefone *", 0.14, "ent_telefone")
        self.criar_campo(self.area_formulario, "CPF", 0.28, "ent_cpf")
        self.criar_campo(self.area_formulario, "Email", 0.42, "ent_email")

        # cria o botão de endereço
        # ao clicar, ele chama o método alternar_endereco
        self.btn_endereco = tk.Button(self.area_formulario,text="✚  Endereço",bg="#e9e9e9",fg="#0b1f2a",font=("Arial", 12, "bold"),bd=0,activebackground="#dcdcdc",cursor="hand2",command=self.alternar_endereco)

        # posiciona o botão de endereço
        self.btn_endereco.place(relx=0.00, rely=0.58, relwidth=0.35, relheight=0.07)

        # cria o botão salvar
        self.btn_salvar = tk.Button(self.area_formulario,text="Salvar",bg="#000000",fg="#ffffff",font=("Arial", 12, "bold"),bd=0,activebackground="#222222",activeforeground="#ffffff",cursor="hand2")

        # posiciona o botão salvar
        self.btn_salvar.place(relx=0.00, rely=0.71, relwidth=0.20, relheight=0.07)

        # cria o botão cancelar
        self.btn_cancelar = tk.Button(self.area_formulario,text="Cancelar",bg="#f48c8c", fg="#ffffff",font=("Arial", 12, "bold"),bd=0,activebackground="#ea7777",activeforeground="#ffffff",cursor="hand2")

        # posiciona o botão cancelar
        self.btn_cancelar.place(relx=0.25, rely=0.71, relwidth=0.25, relheight=0.07)

        # cria a área de endereço
        # ela fica pronta, mas só aparece quando o botão endereço é clicado
        self.area_endereco = tk.Frame(self.root, bg="#f5f5f5")

    # =========================================================
    # MÉTODO: CRIAR UM CAMPO PADRÃO
    # =========================================================
    # esse método cria um label + uma entry
    # ele serve para evitar repetição de código
    def criar_campo(self, janela, texto, pos_y, nome_atributo):

        # cria o texto do campo
        lbl = tk.Label(janela,text=texto,bg="#f5f5f5",fg="#333333",font=("Arial", 11, "bold"))

        # posiciona o texto
        lbl.place(relx=0.00, rely=pos_y)

        # cria a caixa de entrada do campo
        ent = tk.Entry(janela,font=("Arial", 12),bg="#cfcfcf",fg="#222222",relief="flat")

        # posiciona a caixa de entrada logo abaixo do texto
        ent.place(relx=0.00, rely=pos_y + 0.05, relwidth=0.62, relheight=0.07)

        # salva a entry dentro da classe com o nome recebido
        # por exemplo:
        # se nome_atributo for "ent_nome", então isso vira self.ent_nome
        setattr(self, nome_atributo, ent)

    # =========================================================
    # MÉTODO: CRIAR ÁREA DE PEDIDOS
    # =========================================================
    # cria o quadro da direita com busca e tabela
    def criar_area_pedidos(self):

        # frame principal da área de pedidos
        self.area_pedidos = tk.Frame(self.root, bg="#dcdcdc")

        # posiciona essa área do lado direito
        self.area_pedidos.place(relx=0.40, rely=0.23, relwidth=0.49, relheight=0.32)

        # cria a caixa de busca
        self.ent_busca = tk.Entry(self.area_pedidos,font=("Arial", 11),relief="flat",bg="#ffffff",fg="#333333")

        # insere um texto inicial dentro do campo de busca
        self.ent_busca.insert(0, " Buscar Pedido...")

        # posiciona a caixa de busca
        self.ent_busca.place(relx=0.03, rely=0.05, relwidth=0.30, relheight=0.08)

        # cria o texto de filtro ao lado da busca
        self.lbl_filtrar = tk.Label(self.area_pedidos,text="⌕ Filtrar",bg="#dcdcdc",fg="#777777",font=("Arial", 10, "bold"))

        # posiciona o texto filtrar
        self.lbl_filtrar.place(relx=0.36, rely=0.06)

        # frame branco que vai conter a tabela
        self.tabela_frame = tk.Frame(self.area_pedidos, bg="#ffffff")

        # posiciona o frame da tabela
        self.tabela_frame.place(relx=0.02, rely=0.15, relwidth=0.96, relheight=0.78)

        # define os nomes internos das colunas da tabela
        colunas = ("id", "origem", "data", "status", "pagamento")

        # cria a tabela usando ttk.Treeview
        self.tabela = ttk.Treeview(self.tabela_frame,columns=colunas,show="headings")

        # define o texto que aparece no cabeçalho de cada coluna
        self.tabela.heading("id", text="ID")
        self.tabela.heading("origem", text="Origem")
        self.tabela.heading("data", text="Data")
        self.tabela.heading("status", text="Status")
        self.tabela.heading("pagamento", text="Pagamento")

        # define largura e alinhamento de cada coluna
        self.tabela.column("id", width=70, anchor="center")
        self.tabela.column("origem", width=120, anchor="center")
        self.tabela.column("data", width=100, anchor="center")
        self.tabela.column("status", width=120, anchor="center")
        self.tabela.column("pagamento", width=120, anchor="center")

        # faz a tabela ocupar todo o frame branco
        self.tabela.place(relx=0, rely=0, relwidth=1, relheight=1)

        # cria um objeto de estilo para personalizar a tabela
        estilo = ttk.Style()

        # define o tema padrão
        estilo.theme_use("default")

        # configura o estilo das linhas da tabela
        estilo.configure("Treeview", background="#ffffff", foreground="#333333", rowheight=32,fieldbackground="#ffffff",borderwidth=0,font=("Arial", 10))

        # configura o estilo do cabeçalho da tabela
        estilo.configure( "Treeview.Heading", background="#ffffff",foreground="#444444", font=("Arial", 10, "bold"), relief="flat")

        # configura a cor da linha quando ela for selecionada
        estilo.map( "Treeview",background=[("selected", "#d9edf7")],foreground=[("selected", "#222222")])

    # =========================================================
    # MÉTODO: MOSTRAR OU ESCONDER ENDEREÇO
    # =========================================================
    # esse método alterna entre a área de pedidos e a área de endereço
    def alternar_endereco(self):

        # se o endereço já estiver visível
        if self.endereco_visivel:

            # esconde a área de endereço
            self.area_endereco.place_forget()

            # mostra novamente a área de pedidos
            self.area_pedidos.place(relx=0.40, rely=0.23, relwidth=0.49, relheight=0.32)

            # volta a janela para a altura menor
            self.root.geometry("900x700")

            # atualiza a variável de controle
            self.endereco_visivel = False

        # se o endereço ainda não estiver visível
        else:

            # chama o método que monta os campos do endereço
            self.mostrar_endereco()

            # esconde a área de pedidos
            self.area_pedidos.place_forget()

            # aumenta a altura da janela para caber os campos do endereço
            self.root.geometry("1366x860")

            # atualiza a variável de controle
            self.endereco_visivel = True

    # =========================================================
    # MÉTODO: MOSTRAR ENDEREÇO
    # =========================================================
    # desenha os campos de endereço na parte direita da tela
    def mostrar_endereco(self):

        # posiciona a área de endereço
        self.area_endereco.place(relx=0.40, rely=0.18, relwidth=0.53, relheight=0.52)

        # limpa todos os componentes antigos do frame
        # isso evita duplicar os campos ao clicar mais de uma vez
        for widget in self.area_endereco.winfo_children():
            widget.destroy()

        # cria os campos do endereço
        self.criar_campo_endereco("Nome", 0.00, 0.00, 0.86)
        self.criar_campo_endereco("CEP", 0.00, 0.18, 0.38)
        self.criar_campo_endereco("Número", 0.50, 0.18, 0.36)
        self.criar_campo_endereco("Logradouro", 0.00, 0.36, 0.86)
        self.criar_campo_endereco("Complemento/Referência", 0.00, 0.54, 0.86)
        self.criar_campo_endereco("Bairro", 0.00, 0.72, 0.38)
        self.criar_campo_endereco("Cidade", 0.52, 0.72, 0.34)

    # =========================================================
    # MÉTODO: CRIAR CAMPO DE ENDEREÇO
    # =========================================================
    # cria um label e uma entry dentro da área de endereço
    def criar_campo_endereco(self, texto, pos_x, pos_y, largura):

        # cria o texto do campo
        lbl = tk.Label( self.area_endereco,text=texto, bg="#f5f5f5", fg="#333333", font=("Arial", 11, "bold"))

        # posiciona o texto no frame de endereço
        lbl.place(relx=pos_x, rely=pos_y)

        # cria a caixa de entrada
        ent = tk.Entry( self.area_endereco,font=("Arial", 12), bg="#cfcfcf",fg="#222222", relief="flat")

        # posiciona a caixa de entrada logo abaixo do texto
        ent.place(relx=pos_x, rely=pos_y + 0.06, relwidth=largura, relheight=0.08)

    # =========================================================
    # MÉTODO: PREENCHER EXEMPLO DE EDIÇÃO
    # =========================================================
    # esse método serve para abrir a tela no modo "Editar Cliente"
    # preenchendo alguns dados de exemplo
    def preencher_exemplo_edicao(self):

        # troca o título da tela
        self.lbl_titulo.config(text="Editar Cliente")

        # limpa o campo nome
        self.ent_nome.delete(0, tk.END)

        # insere um nome de exemplo
        self.ent_nome.insert(0, "Débora Diniz")

        # limpa o campo telefone
        self.ent_telefone.delete(0, tk.END)

        # insere um telefone de exemplo
        self.ent_telefone.insert(0, "(93) 9 9152-9220")

        # adiciona uma linha de exemplo na tabela de pedidos
        self.tabela.insert("", "end", values=("#004", "Mesa 2", "04/04/26", "Entregue", "Pago"))


# =========================================================
# PARTE PRINCIPAL DO PROGRAMA
# =========================================================
# esse bloco só será executado se esse arquivo for aberto diretamente
if __name__ == "__main__":

    # cria a janela principal do tkinter
    root = tk.Tk()

    # cria a tela de clientes usando a janela principal
    app = JanelaClientes(root)

    # se quiser abrir a tela já no modo editar, basta tirar o comentário da linha abaixo
    # app.preencher_exemplo_edicao()

    # mantém a janela aberta e funcionando
    root.mainloop()
