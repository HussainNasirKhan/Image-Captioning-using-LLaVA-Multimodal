# Image Captioning using LLaVA Multimodal

A Flask web application that allows users to upload images and generates descriptive captions using the LLaVA Multimodal model. Features include real-time image upload display, responsive design, and clipboard functionality for easy caption copying.

https://github.com/user-attachments/assets/63f46777-fac6-465a-b0e5-0f65ee415fec

## Features
- Upload images and get descriptive captions using the LLaVA model.
- Real-time display of uploaded images.
- Responsive design for a seamless user experience.
- Copy captions to clipboard with a single click.

## Requirements
- Flask
- Requests
- Pillow

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/HussainNasirKhan/Image-Captioning-using-LLaVA-Multimodal.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Image-Captioning-using-LLaVA-Multimodal
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask app:
    ```sh
    python app.py
    ```
2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Upload an image to generate a caption.

## File Structure

- `app.py`: The main Flask application file.
- `templates/`: Contains the HTML templates (`upload.html` and `result.html`).
- `static/`: Contains the CSS file (`styles.css`).

## Contributing
Feel free to submit issues and pull requests for improvements or bug fixes.
