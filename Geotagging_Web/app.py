# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:39:40 2024

@author: shivajay
"""

# backend.py

import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from embedding_module import embed_text
from extraction_module import extract_data

app = Flask(__name__)

static_dir = 'F:\\Geotagging_final\\static\\'
os.makedirs(static_dir, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/embed')
def embed():
    return render_template('embed.html')

@app.route('/extract')
def extract():
    return render_template('extract.html')

@app.route('/process_embed', methods=['POST'])
def process_embed():
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file part'}), 400
    file = request.files['file']
    data = request.form['data']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        embed_text(file, data, os.path.join(static_dir, 'embedded_image.png'))
        return jsonify({'status': 'success', 'message': 'Data embedded successfully!'}), 200
    return jsonify({'status': 'error', 'message': 'File not allowed'}), 400

@app.route('/process_extract', methods=['POST'])
def process_extract():
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        extracted_data = extract_data(file)
        return jsonify({'status': 'success', 'data': extracted_data}), 200
    return jsonify({'status': 'error', 'message': 'File not allowed'}), 400

@app.route('/result/<action>')
def result(action):
    if action == 'embed':
        return render_template('result.html', result_message='Data embedded successfully!', action='embed')
    elif action == 'extract':
        return render_template('result.html', result_message='Data extracted successfully!', action='extract')

@app.route('/download_embedded_image')
def download_embedded_image():
    return send_from_directory(static_dir, 'embedded_image.png', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)










