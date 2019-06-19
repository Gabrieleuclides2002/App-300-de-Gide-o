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

        canvas2.create_rectangle(2,2,52,32, fill='white')
        canvas2.create_text(27,17, text='Menu', font=('Verdana',13), fill='black')

        
    if e.x >=350 and e.x <=550 and e.y >=110 and e.y <= 140:
        def buttons2(e):
            if e.x >= 2 and e.x <= 52 and e.y >=2 and e.y <= 32:
                canvas2.destroy()
            return
        
        canvas2 = Canvas(canvas, width=600, height=500, bg='green')
        canvas2.place(x=0,y=0)
        canvas2.bind('<Button-1>',buttons2)

        canvas2.create_rectangle(2,2,52,32, fill='white')
        canvas2.create_text(27,17, text='Menu', font=('Verdana',13), fill='black')

        canvas2.create_text(100,100, text='Nome:', font=('Verdana',14,'bold'), fill='white')
        canvas2.create_text(110,200, text='Unidade:', font=('Verdana',14,'bold'), fill='white')
        canvas2.create_text(117,300, text='Endereço:', font=('Verdana',14,'bold'), fill='white')
        canvas2.create_text(86,400, text='RG:', font=('Verdana',14,'bold'), fill='white')

        ed_nome = Entry(canvas2, width=35, border=0, bg='green', font=('Verdana',12))
        ed_nome.place( x=150, y=92 )
        canvas2.create_line(150,112,500,112, fill='white')
        
    if e.x >=350 and e.x <=550 and e.y >=170 and e.y <= 200:
        def buttons2(e):
            if e.x >= 2 and e.x <= 52 and e.y >=2 and e.y <= 32:
                canvas2.destroy()
            return
        
        canvas2 = Canvas(canvas, width=600, height=500, bg='green')
        canvas2.place(x=0,y=0)
        canvas2.bind('<Button-1>',buttons2)

        canvas2.create_rectangle(2,2,52,32, fill='white')
        canvas2.create_text(27,17, text='Menu', font=('Verdana',13), fill='black')
        
    if e.x >=350 and e.x <=550 and e.y >=230 and e.y <= 260:
        def buttons2(e):
            if e.x >= 2 and e.x <= 52 and e.y >=2 and e.y <= 32:
                canvas2.destroy()
            return
        
        canvas2 = Canvas(canvas, width=600, height=500, bg='green')
        canvas2.place(x=0,y=0)
        canvas2.bind('<Button-1>',buttons2)

        canvas2.create_rectangle(2,2,52,32, fill='white')
        canvas2.create_text(27,17, text='Menu', font=('Verdana',13), fill='black')
        
    if e.x >=350 and e.x <=550 and e.y >=290 and e.y <= 320:
        def buttons2(e):
            if e.x >= 2 and e.x <= 52 and e.y >=2 and e.y <= 32:
                canvas2.destroy()
            return
        
        canvas2 = Canvas(canvas, width=600, height=500, bg='green')
        canvas2.place(x=0,y=0)
        canvas2.bind('<Button-1>',buttons2)

        canvas2.create_rectangle(2,2,52,32, fill='white')
        canvas2.create_text(27,17, text='Menu', font=('Verdana',13), fill='green')
        
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
# olá
janela.mainloop()
