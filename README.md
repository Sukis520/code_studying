# Fall Detection Web Application

这个项目用于检测人是否摔倒，有两个标签，0-摔倒，1-没摔倒，搭建了本地web服务器,在web上面上传图片即可识别是否摔倒

## Project Structure

```
fall-detection-web
├── src
│   ├── app.py              # Entry point of the application, handles image uploads and model inference.
│   ├── model
│   │   └── model.pkl       # Trained model file for fall detection.
│   ├── static
│   │   └── style.css       # Stylesheet for the web application.
│   └── templates
│       └── index.html      # Main page with upload form and result display.
├── requirements.txt        # List of required Python libraries and dependencies.
└── README.md               # Documentation for the project.
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Sukis520/fall-detection
   cd fall-detection-web
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Use the upload form to submit an image for fall detection.

4. The application will display the result indicating whether a fall has been detected.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.