from tkinter import *
from tkinter import ttk
from tkinter import tix
import sqlite3
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.platypus import SimpleDocTemplate, Image
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from PIL import ImageTk, Image
import base64