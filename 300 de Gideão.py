from tkinter import *

def cor(e):
    if e.x >= 350 and e.x <=550 and e.y >=50 and e.y <= 80:
        # Membros
        canvas.create_rectangle(350,50,550,80, fill='light blue')
        canvas.create_text(450,65, text='Membros', font=('Verdana',13))

        # Adicionar Desbravador
        rec_add = canvas.create_rectangle(350,110,550,140, fill='light yellow')
        text_add = canvas.create_text(450,125, text='Adicionar alguém', font=('Verdana',13))

        # Anotações
        canvas.create_rectangle(350,170,550,200, fill='light yellow')
        canvas.create_text(450,185, text='Anotações', font=('Verdana',13))

        # Cartão Virtual
        canvas.create_rectangle(350,230,550,260, fill='light yellow')
        canvas.create_text(450,245, text='Cartão virtual', font=('Verdana',13))

        # Patrimônio
        canvas.create_rectangle(350,290,550,320, fill='light yellow')
        canvas.create_text(450,305, text='Patrimônio do clube', font=('Verdana',13))
        
    if e.x >=350 and e.x <=550 and e.y >=110 and e.y <= 140:
        # Membros
        canvas.create_rectangle(350,50,550,80, fill='light yellow')
        canvas.create_text(450,65, text='Membros', font=('Verdana',13))

        # Adicionar Desbravador
        rec_add = canvas.create_rectangle(350,110,550,140, fill='light blue')
        text_add = canvas.create_text(450,125, text='Adicionar alguém', font=('Verdana',13))

        # Anotações
        canvas.create_rectangle(350,170,550,200, fill='light yellow')
        canvas.create_text(450,185, text='Anotações', font=('Verdana',13))

        # Cartão Virtual
        canvas.create_rectangle(350,230,550,260, fill='light yellow')
        canvas.create_text(450,245, text='Cartão virtual', font=('Verdana',13))

        # Patrimônio
        canvas.create_rectangle(350,290,550,320, fill='light yellow')
        canvas.create_text(450,305, text='Patrimônio do clube', font=('Verdana',13))
        
    if e.x >=350 and e.x <=550 and e.y >=170 and e.y <= 200:
        # Membros
        canvas.create_rectangle(350,50,550,80, fill='light yellow')
        canvas.create_text(450,65, text='Membros', font=('Verdana',13))

        # Adicionar Desbravador
        rec_add = canvas.create_rectangle(350,110,550,140, fill='light yellow')
        text_add = canvas.create_text(450,125, text='Adicionar alguém', font=('Verdana',13))

        # Anotações
        canvas.create_rectangle(350,170,550,200, fill='light blue')
        canvas.create_text(450,185, text='Anotações', font=('Verdana',13))

        # Cartão Virtual
        canvas.create_rectangle(350,230,550,260, fill='light yellow')
        canvas.create_text(450,245, text='Cartão virtual', font=('Verdana',13))

        # Patrimônio
        canvas.create_rectangle(350,290,550,320, fill='light yellow')
        canvas.create_text(450,305, text='Patrimônio do clube', font=('Verdana',13))

    if e.x >=350 and e.x <=550 and e.y >=230 and e.y <= 260:
        # Membros
        canvas.create_rectangle(350,50,550,80, fill='light yellow')
        canvas.create_text(450,65, text='Membros', font=('Verdana',13))

        # Adicionar Desbravador
        rec_add = canvas.create_rectangle(350,110,550,140, fill='light yellow')
        text_add = canvas.create_text(450,125, text='Adicionar alguém', font=('Verdana',13))

        # Anotações
        canvas.create_rectangle(350,170,550,200, fill='light yellow')
        canvas.create_text(450,185, text='Anotações', font=('Verdana',13))

        # Cartão Virtual
        canvas.create_rectangle(350,230,550,260, fill='light blue')
        canvas.create_text(450,245, text='Cartão virtual', font=('Verdana',13))

        # Patrimônio
        canvas.create_rectangle(350,290,550,320, fill='light yellow')
        canvas.create_text(450,305, text='Patrimônio do clube', font=('Verdana',13))
        
    if e.x >=350 and e.x <=550 and e.y >=290 and e.y <= 320:
        # Membros
        canvas.create_rectangle(350,50,550,80, fill='light yellow')
        canvas.create_text(450,65, text='Membros', font=('Verdana',13))

        # Adicionar Desbravador
        rec_add = canvas.create_rectangle(350,110,550,140, fill='light yellow')
        text_add = canvas.create_text(450,125, text='Adicionar alguém', font=('Verdana',13))

        # Anotações
        canvas.create_rectangle(350,170,550,200, fill='light yellow')
        canvas.create_text(450,185, text='Anotações', font=('Verdana',13))

        # Cartão Virtual
        canvas.create_rectangle(350,230,550,260, fill='light yellow')
        canvas.create_text(450,245, text='Cartão virtual', font=('Verdana',13))

        # Patrimônio
        canvas.create_rectangle(350,290,550,320, fill='light blue')
        canvas.create_text(450,305, text='Patrimônio do clube', font=('Verdana',13))

def buttons(e):
    if e.x >= 350 and e.x <=550 and e.y >=50 and e.y <= 80:
        def buttons2(e):
            if e.x >= 2 and e.x <= 52 and e.y >=2 and e.y <= 32:
                canvas2.destroy()
            return

        canvas2 = Canvas(canvas, width=600, height=500, bg='green')
        canvas2.place(x=0,y=0)
        canvas2.bind('<Button-1>',buttons2)

        canvas2.create_oval(2,2,52,32, fill='white')
        canvas2.create_text(27,17, text='Menu', font=('Verdana',13), fill='black')

    ### Cadastramento ###
    if e.x >=350 and e.x <=550 and e.y >=110 and e.y <= 140:
        def buttons2(e):
            if e.x >= 2 and e.x <= 52 and e.y >=2 and e.y <= 32:
                canvas2.destroy()
            return
        
        canvas2 = Canvas(canvas, width=600, height=500, bg='green')
        canvas2.place(x=0,y=0)
        canvas2.bind('<Button-1>',buttons2)

        canvas2.create_oval(2,2,52,32, fill='white')
        canvas2.create_text(27,17, text='Menu', font=('Verdana',13), fill='black')

        canvas2.create_text(100,100, text='Nome:', font=('Verdana',14,'bold'), fill='white')
        canvas2.create_text(110,200, text='Unidade:', font=('Verdana',14,'bold'), fill='white')
        canvas2.create_text(117,300, text='Endereço:', font=('Verdana',14,'bold'), fill='white')
        canvas2.create_text(86,400, text='RG:', font=('Verdana',14,'bold'), fill='white')

        # Nome
        ed_nome = Entry(canvas2, width=35, border=0, bg='green', font=('Verdana',12), fg='white')
        ed_nome.place( x=150, y=92 )
        canvas2.create_line(150,112,500,112, fill='white')
        
        # Unidade
        ed_unidade = Entry(canvas2, width=20, border=0, bg='green', font=('Verdana',12), fg='white')
        ed_unidade.place( x=170, y=191 )
        canvas2.create_line(170,211,330,211, fill='white')

        # Endereço
        ed_end = Entry(canvas2, width=25, border=0, bg='green', font=('Verdana',12), fg='white')
        ed_end.place( x=184 , y=290 )
        canvas2.create_line(184,310,435,310, fill='white')

        # RG
        ed_rg = Entry(canvas2, width=15, border=0, bg='green', font=('Verdana',12), fg='white')
        ed_rg.place( x=120 , y=389 )
        canvas2.create_line(120,409,270,409, fill='white')

        # Botão confirmar
        bt_confirm = Button(canvas2, text='Confirmar', font=('Castellar',14), bg='yellow', overrelief=GROOVE, activebackground='black', activeforeground='yellow')
        bt_confirm.place( x=400, y=400 )
        
    if e.x >=350 and e.x <=550 and e.y >=170 and e.y <= 200:
        def buttons2(e):
            if e.x >= 2 and e.x <= 52 and e.y >=2 and e.y <= 32:
                canvas2.destroy()
            return
        
        canvas2 = Canvas(canvas, width=600, height=500, bg='green')
        canvas2.place( x=0, y=0 )
        canvas2.bind('<Button-1>',buttons2)

        canvas2.create_oval(2,2,52,32, fill='white')
        canvas2.create_text(27,17, text='Menu', font=('Verdana',13), fill='black')

        canvas2.create_line(300,0,300,500, fill='white')

        canvas3 = Canvas(canvas2, width=300, height=500, bg='#00FF00')
        canvas3.place( x=300, y=0 )

        text_anot = Text(canvas3, font=('Verdana',12), width=300, height=25)
        text_anot.place( x=0, y=46 )

        bt_salvar = Button(canvas3, text='Salvar', activebackground='black', bg='yellow', activeforeground='yellow', font=('Times New Roman',17), overrelief=GROOVE)
        bt_salvar.place( x=0, y=0 )
        
    if e.x >=350 and e.x <=550 and e.y >=230 and e.y <= 260:
        def buttons2(e):
            if e.x >= 2 and e.x <= 52 and e.y >=2 and e.y <= 32:
                canvas2.destroy()
            return
        
        canvas2 = Canvas(canvas, width=600, height=500, bg='green')
        canvas2.place(x=0,y=0)
        canvas2.bind('<Button-1>',buttons2)

        canvas2.create_oval(2,2,52,32, fill='white')
        canvas2.create_text(27,17, text='Menu', font=('Verdana',13), fill='black')

    ### Patrimônio ###
    if e.x >=350 and e.x <=550 and e.y >=290 and e.y <= 320:
        def buttons2(e):
            if e.x >= 2 and e.x <= 52 and e.y >=2 and e.y <= 32:
                canvas2.destroy()
            return
        
        def conc():
            if ed_sac.get() == '' and ed_dep.get() == '':
                lb_caixa['text'] = 0
            if ed_dep.get() == '':
                deposito = str(ed_dep.get())
                saque = int(ed_sac.get())
            if ed_sac.get() == '':
                saque = str(ed_sac.get())
                deposito = int(ed_dep.get())
            if ed_sac.get() != '' and ed_dep.get() != '':
                saque = int(ed_dep.get())
                deposito = int(ed_dep.get())
                
            if deposito == '':
                tot = int(lb_caixa['text']) - saque
                tot2 = str(tot)
                lb_caixa['text'] = tot2
                
            if saque == '':
                tot = int(lb_caixa['text']) + deposito
                tot2 = str(tot)
                lb_caixa['text'] = tot2
                
            if saque != '' and deposito != '':
                lb_caixa['text'] = str(int(ed_dep.get()) - int(ed_sac.get()))
                
            return
        
        canvas2 = Canvas(canvas, width=600, height=500, bg='green')
        canvas2.place(x=0,y=0)
        canvas2.bind('<Button-1>',buttons2)

        canvas2.create_oval(2,2,52,32, fill='white')
        canvas2.create_text(27,17, text='Menu', font=('Verdana',13), fill='black')

        canvas2.create_text(200,100, text='Caixa do Clube:', font=('Verdana',14,'bold'), fill='white')
        canvas2.create_text(170,200, text='Depositar: R$', font=('Verdana',14,'bold'), fill='white')
        canvas2.create_text(150,250, text='Sacar: R$',  font=('Verdana',14,'bold'), fill='white')

        # Valor do caixa
        lb_caixa = Label(canvas2, text='', font=('Arial',14), fg='yellow', bg='green')
        lb_caixa.place( x=316, y=89)

        # Depositar
        ed_dep = Entry(canvas2, border=0, width=10, font=('Verdana',13), bg='green', fg='white')
        ed_dep.place( x=260, y=188)
        canvas2.create_line(260,210,367,210, fill='white')

        # Sacar
        ed_sac =  Entry(canvas2, border=0, width=10, font=('Verdana',13), bg='green', fg='white')
        ed_sac.place( x=215, y=237 )
        canvas2.create_line(215,259,326,259, fill='white')

        # Botão Concluir
        bt_concluir = Button(canvas2, text='Concluir', font=('Castellar',14), bg='yellow', overrelief=GROOVE, activebackground='black', activeforeground='yellow', command=conc)
        bt_concluir.place( x=235, y=300 )

        # Alerta
        canvas2.create_rectangle(20,350,580,450, fill='white')
        canvas2.create_text(300,400, text='*A cada alteração certifique-se de utilizar apenas uma opção*\n                             ( Depositar / Sacar )', font=('Arial',13,'bold'))
        

    return


janela = Tk()
janela.geometry('600x500+250+100')
janela.title('300 de Gideão')
janela['bg'] = 'white'
janela.resizable(0,0)

canvas = Canvas(janela, width=600, height=500, bg='green')
canvas.pack()
canvas.bind('<Button-1>',buttons)
canvas.bind('<Motion>',cor)

imagem = PhotoImage(file='photo.png')
lb_fundo = Label(canvas, image=imagem, width=300, height=500, bg='#F7F7F7', cursor='heart')
lb_fundo.place( x=2, y=2 )

# Membros
canvas.create_rectangle(350,50,550,80, fill='light yellow')
canvas.create_text(450,65, text='Membros', font=('Verdana',13))

# Adicionar Desbravador
rec_add = canvas.create_rectangle(350,110,550,140, fill='light yellow')
text_add = canvas.create_text(450,125, text='Adicionar alguém', font=('Verdana',13))

# Anotações
canvas.create_rectangle(350,170,550,200, fill='light yellow')
canvas.create_text(450,185, text='Anotações', font=('Verdana',13))

# Cartão Virtual
canvas.create_rectangle(350,230,550,260, fill='light yellow')
canvas.create_text(450,245, text='Cartão virtual', font=('Verdana',13))

# Patrimônio
canvas.create_rectangle(350,290,550,320, fill='light yellow')
canvas.create_text(450,305, text='Patrimônio do clube', font=('Verdana',13))

janela.mainloop()
