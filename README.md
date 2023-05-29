# Command-Line Face Blur Tool

This is a command-line tool written in Python that allows you to detect faces in an image and apply a blur effect to the detected faces.
All processing is done locally on your machine, and no data is sent to any third-party service.

## Requirements

- Python 3.6 or above
- OpenCV (installed via `pip install opencv-python`)
- argparse (installed via `pip install argparse`)

You can install the required packages by running the following command:

```python
pip install -r requirements.txt
```

It is highly recommended to use a virtual environment to install the required packages.

## Usage

```python
python face_blur_cli.py image_path [--save-path SAVE_PATH] [--blur-level BLUR_LEVEL]
```

- `image_path`: Path to the input image file.
- `--save-path SAVE_PATH` (optional): Path to save the blurred image. If not provided, the blurred image will be displayed but not saved.
- `--blur-level BLUR_LEVEL` (optional): Blur level to adjust the intensity of the blur effect (default: 10). Higher values result in more blur.

## Examples

- Save the blurred image with a custom save path:

```python
python face_blur_cli.py image.jpg --save-path blurred_image.jpg
```

- Adjust the blur level to 5 (default: 10):

```python
python face_blur_cli.py image.jpg --blur-level 5
```

## License

This project is licensed under the MIT License.
