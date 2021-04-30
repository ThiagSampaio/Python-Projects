import pandas as pd
import smtplib
from tkinter import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

COR_BRANCA = "#ffffff"
#file = "informações produtos padrão (1).xls"
#fp = open(file, 'rb')
#part = MIMEBase('application','vnd.ms-excel')
#part.set_payload(fp.read())
#fp.close()
#encoders.encode_base64(part)
#part.add_header('Content-Disposition', 'attachment', filename='informações produtos padrão (1).xls')

#----------------------------- Preparação de dados ----------------------------#

fp = open('imagem_pascoa.jpeg', 'rb')

msgImage = MIMEImage(fp.read())


fp.close()


data = pd.read_csv("data_final_4.csv", error_bad_lines=False, sep=";")
lista_estados = list(data["ESTADO "].unique())
dict_data = {}
for itens in lista_estados:
    dict_data[itens] = list(data[data["ESTADO "] == f"{itens}"]['E MAIL'])

for (key,values) in dict_data.items():
    print(key)
print(dict_data)


def mandar_email():

    fromaddr = fromaddr_entry.get()
    Subject_message = Subject_entry.get()
    senha = corpo_entry.get()


    for (key,values) in dict_data.items():
        if len(values) == 1:
            with open (f"Cartas_txt/CT {key}.txt",encoding="utf8") as file:
                corpo_message = file.readlines()
                corpo_message_txt = "".join(corpo_message)
            toaddr = values[0]
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = values[0]
            msg['Subject'] = Subject_message
            body = corpo_message_txt
            msg.attach(MIMEText(body, 'plain'))
            msg.attach(msgImage)
            #msg.attach(part)
            estado = str(key).upper()
            filename = f"CT {estado}.doc"
            attachment = open(f"Cartas/CT {estado}.doc", "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            #msg.attach(p)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(fromaddr, senha)
            text = msg.as_string()
            s.sendmail(fromaddr, toaddr, text)
            s.quit()
        else:
            for item in values:
                toaddr = item
                msg = MIMEMultipart()
                msg['From'] = fromaddr
                msg['To'] = item
                msg['Subject'] = Subject_message
                with open(f"Cartas_txt/CT {key}.txt", encoding="utf8") as file:
                    corpo_message = file.readlines()
                    corpo_message_txt = "".join(corpo_message)
                body = corpo_message_txt
                msg.attach(MIMEText(body, 'plain'))
                estado = str(key).upper()
                filename = f"CT {estado}.doc"
                attachment = open(f"Cartas/CT {estado}.doc", "rb")
                p = MIMEBase('application', 'octet-stream')
                p.set_payload((attachment).read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                #msg.attach(p)
                #msg.attach(part)
                msg.attach(msgImage)
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(fromaddr, senha)
                text = msg.as_string()
                s.sendmail(fromaddr, toaddr, text)
                s.quit()


# -- UI SETUP -- #

window = Tk()
window.title("Email automático _ v1.0")
window.config(padx=20, pady=20, bg=COR_BRANCA)

# # -- CANVAS SETUP -- #

canvas = Canvas(width=400, height=400, highlightthickness=0)
logo_img=PhotoImage(file='logo_empresa.png')
canvas.create_image(200, 200, image=logo_img)
canvas.config(bg=COR_BRANCA, highlightthickness=0)
canvas.grid(row=1, column=1)

# -- LABEL -- #
fromaddr_label = Label(text="EMAIL REMETENTE(gmail):", font=("Arial", 10, "bold"),bg=COR_BRANCA)
fromaddr_label.grid(column=0, row=2)

Subject_label = Label(text="ASSUNTO DO EMAIL:", font=("Arial", 10, "bold"),bg=COR_BRANCA)
Subject_label.grid(column=0, row=4)

corpo_label = Label(text="SENHA DO EMAIL:", font=("Arial", 10, "bold"),bg=COR_BRANCA)
corpo_label.grid(column=0, row=3)


# -- ENTRY -- #
fromaddr_entry = Entry(width=35, bg='#cccccc')
fromaddr_entry.grid(column=0, row=2, columnspan=2)
fromaddr_entry.focus()

Subject_entry = Entry(width=35, bg='#cccccc')
Subject_entry.grid(column=0, row=4, columnspan=2)

corpo_entry = Entry(width=35, bg='#cccccc')
corpo_entry.grid(column=0, row=3, columnspan=2)


# -- BUTTON SETUP -- #

# # -------------------- BUTTON 1 SETUP ------------------------- # #
generate_password_button = Button(text="Mandar email", highlightthickness=0, command=mandar_email)
generate_password_button.grid(column=2, row=2)



window.mainloop()