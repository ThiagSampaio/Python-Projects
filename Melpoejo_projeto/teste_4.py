import pandas as pd
import smtplib
from tkinter import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

data =pd.read_csv("data_final_teste2.csv", error_bad_lines=False, sep=";")
print(data["ESTADO"])