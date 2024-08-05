from flask import Flask, render_template, request
import requests
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

def load_image(image_file):
    """Load an image from uploaded file."""
    return Image.open(image_file)

def image_to_base64(image):
    """Convert an image to a base64 string."""
    # Convert image to RGB if it has an alpha channel
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    
    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

def generate_caption(image_base64):
    """Send the image to the Llava model and get the caption."""
    payload = {
        "model": "llava",
        "prompt": "Describe the contents of this image.",
        "images": [image_base64],
        "stream": False
    }
    
    response = requests.post('http://localhost:11434/api/generate', json=payload)
    
    if response.status_code == 200:
        return response.json().get("response", "No caption generated.")
    else:
        return f"Error: {response.status_code}, {response.text}"

@app.route('/')
def upload_form():
    """Render the upload form template."""
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
    """Handle image upload, generate caption, and render result."""
    uploaded_file = request.files['image']
    
    if uploaded_file.filename != '':
        try:
            image = load_image(uploaded_file)
            image_base64 = image_to_base64(image)
            caption = generate_caption(image_base64)
            return render_template('result.html', caption=caption, image_data=image_base64)
        except Exception as e:
            return render_template('upload.html', error=f"Error processing image: {str(e)}")
    else:
        return render_template('upload.html', error="Please select an image to upload.")

if __name__ == '__main__':
    app.run(debug=True)
