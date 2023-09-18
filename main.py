# -*- Coding:utf-8 -*-
from flask import Flask, render_template as render, send_from_directory, url_for,redirect
from app import create_app
from config import Properties,Routes

app= create_app()

@app.route("/")

def index():
    return render('index.html')

@app.route("/images/qr/code/<path:filename>")

def get_img_qr(filename):
    return send_from_directory(Routes.base_code_qr,filename)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)