# 🖼️ Image Steganography Web App  

A sleek and easy-to-use web app built with **Streamlit** that lets you **hide and extract secret messages** within images using **steganography**! 🔐✨  

## 🚀 Features  

✅ **Hide Messages** – Securely embed text into images 📝➡️🖼️  
✅ **Extract Messages** – Retrieve hidden messages from processed images 🔍🔡  
✅ **Integrity Check** – Uses **SHA-256 hashing** to verify message integrity 🔒  
✅ **User-friendly** – Simple web interface for effortless interaction 💻  

## 📦 Requirements  

You'll need **Python 3.x** and the following packages:  

- 🏗️ `streamlit` – For the web UI  
- 🖼️ `Pillow` – Image processing  
- 🤖 `torch` & `transformers` – (If needed for additional AI tasks)  
- 🔢 `numpy` – Numerical operations  
- 📷 `opencv-python` – Image manipulation  

## ⚡ Installation  

1. Clone this repo:  
```bash
   git clone <repo-link>
   cd <repo-folder>
  ```

2. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## 🎯 How to Use

1. Run the app:
  ```bash
  streamlit run app.py
  ```

2. Open your browser and interact with the interface! 🌐

3. Choose an operation:

  🖊️ Embed Data: Upload an image & enter the secret text to hide 🔏
  
  🔓 Extract Data: Upload a processed image to retrieve the hidden message

  
## 🛠️ How It Works

🔸 Uses pixel manipulation for encoding messages 🖼️🔡

🔸 Ensures message integrity with SHA-256 hashing 🔐

🔸 Supports popular image formats: JPG, JPEG, PNG 🏞️

🔸 Maintains image quality while embedding data 🎨

## ⚠️ Limitations

⚡ The amount of data you can hide depends on the image size

⚡ Only supports text-based secret messages 🔡

⚡ Works best with lossless formats like PNG (JPG may lose data)

## Hosted Link: https://shiv1803-geotagging.hf.space
