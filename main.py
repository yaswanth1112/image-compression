import cv2
import tkinter as tk
from tkinter import filedialog
import os

def open_file_dialog():
    """Open a file dialog to select an image file and return the file path."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff")]
    )
    return file_path

# Open file dialog to select image
file_path = open_file_dialog()

if not file_path:
    print("No file selected.")
else:
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
    else:
        # Read the image
        img = cv2.imread(file_path)

        # Check if the image was loaded correctly
        if img is None:
            print(f"Error: Unable to load image '{file_path}'.")
        else:
            print(f"Image loaded successfully with shape: {img.shape}")

            # Calculate new dimensions
            k = 5
            width = int(img.shape[1] / k)
            height = int(img.shape[0] / k)

            # Resize the image
            scaled = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
            print(f"Resized image shape: {scaled.shape}")

            # Display the resized image
            cv2.imshow("Output", scaled)
            cv2.waitKey(500)
            cv2.destroyAllWindows()

            # Save the resized image
            cv2.imwrite('resized_image.jpg', scaled)
            print("Resized image saved as 'resized_image.jpg'.")
