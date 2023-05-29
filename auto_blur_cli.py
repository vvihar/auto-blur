import argparse

import cv2


def blur_faces(image_path, save_path=None, blur_level=10):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale for face detection
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform face detection using the haarcascade classifier
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    faces = face_cascade.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    # Apply blur to each detected face
    blurred_image = image.copy()
    for x, y, w, h in faces:
        face_roi = blurred_image[y : y + h, x : x + w]
        blurred_face = cv2.GaussianBlur(face_roi, (99, 99), blur_level)
        blurred_image[y : y + h, x : x + w] = blurred_face

    # Save the blurred image
    if save_path is not None:
        cv2.imwrite(save_path, blurred_image)
    else:
        image_dir = "/".join(image_path.split("/")[:-1])
        image_name = image_path.split("/")[-1].split(".")[0]
        save_path = f"{image_dir}/{image_name}_blurred.jpg"
        cv2.imwrite(save_path, blurred_image)
    print(f"Blurred image saved to: {save_path}")

    # Display the blurred image
    cv2.imshow("Blurred Image", blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Face Blur CLI Tool")
    parser.add_argument("image_path", help="Path to the image file")
    parser.add_argument("--save-path", help="Optional path to save the blurred image")
    parser.add_argument(
        "--blur-level", type=int, default=10, help="Blur level (default: 10)"
    )

    # Parse the arguments
    args = parser.parse_args()

    # Call the blur_faces function with the provided arguments
    blur_faces(args.image_path, args.save_path, args.blur_level)
