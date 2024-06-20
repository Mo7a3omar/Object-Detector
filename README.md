# Object Detector

A Streamlit web application for object detection using a pre-trained YOLOv5 model. Upload an image, and the app will detect and annotate objects in the image, displaying the results both visually and textually.

## Features

- Upload an image file (JPG, JPEG, PNG).
- Detect and annotate objects in the uploaded image using YOLOv5.
- Display the annotated image and a list of detected objects with confidence scores.
- Dark theme for a modern and user-friendly interface.



## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/object-detector.git
    cd object-detector
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Streamlit app:**
    ```sh
    streamlit run app.py
    ```

2. **Open your browser and go to:**
    ```
    http://localhost:8501
    ```

3. **Upload an image and click on 'Analyze Image'.**

4. **View the annotated image and the list of detected objects.**

## Project Structure
```
object-detector/
├── app.py # Main Streamlit application
├── requirements.txt # List of dependencies
└── .gitignore # Git ignore file
```
## Requirements

- streamlit
- torch
- Pillow
- numpy

## Install the requirements using:
```sh
pip install -r requirements.txt
```
## Example
Upload an image, and the application will display the following:

1-Annotated image with bounding boxes and labels for detected objects.
2-List of detected objects with their confidence scores.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
Streamlit
YOLOv5
PyTorch
