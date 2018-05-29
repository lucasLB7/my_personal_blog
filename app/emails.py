from flask_mail import Message
from . import mail
from flask import render_template
import os

def send_mail(subject, sender, recipients, text_body, html_body):
    message = Message(subject, sender = sender, recipients = recipients)
    message.body = text_body
    message.html = html_body

    mail.send(message)

def send_sub(user):
    send_mail("Succesfully subscribed", sender="blenderfendermail@gmail.com", recipients=[user.email], text_body="Successfully subscibed to Blender Fender", html_body="<h1>Subscibed</h1>")
