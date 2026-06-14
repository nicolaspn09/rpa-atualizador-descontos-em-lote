import mysql.connector
import locale
import smtplib
import time
import requests
import os
import cx_Oracle
import openpyxl
import pandas as pd
from datetime import timedelta
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from logExecucaoCodigos import grava_log_execucao_sql


#Grava a informação no log
def grava_log(mensagemLog):
    pass # Logica de negocio removida por seguranca corporativa

def conecta_my_sql_insert(sql):
    pass # Logica de negocio removida por seguranca corporativa

def envia_email_execucao():
    pass # Logica de negocio removida por seguranca corporativa

def envia_email(mensagemEmail, destinatarios_email, assunto_email): 
    """
    Envia e-mail para os usuários

    Parameters:
    pass # Logica de negocio removida por seguranca corporativa

def conecta_oracle(query):
    pass # Logica de negocio removida por seguranca corporativa

def converte_data():
    pass # Logica de negocio removida por seguranca corporativa

def le_arquivo_excel(caminho_arquivo):
    pass # Logica de negocio removida por seguranca corporativa

def le_arquivo_excel_monta_update(caminho_arquivo):
    pass # Logica de negocio removida por seguranca corporativa

def preenche_excel_pendencias(totalizador, item, caminho_arquivo):
    pass # Logica de negocio removida por seguranca corporativa

def verifica_criacao_diretorios():
    pass # Logica de negocio removida por seguranca corporativa

def verifica_arquivos_recebidos():
    pass # Logica de negocio removida por seguranca corporativa

def verifica_calculos_recebimentos():
    pass # Logica de negocio removida por seguranca corporativa

def verifica_arquivos_ressarcimento():
    pass # Logica de negocio removida por seguranca corporativa

def verifica_arquivos_descontos_alterar():
    pass # Logica de negocio removida por seguranca corporativa

def gera_pendencias():
    pass # Logica de negocio removida por seguranca corporativa
