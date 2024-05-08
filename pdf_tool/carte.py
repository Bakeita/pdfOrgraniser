import cv2
import pandas as pd

# Load the image using OpenCV
image_path = 'path/to/your/image.jpg'
image = cv2.imread(image_path)

# Get image dimensions
height, width, channels = image.shape

# Flatten the 2D array to a 1D array of pixel values
pixels = image.reshape((height * width, channels))

# Create a DataFrame with pixel values
df = pd.DataFrame(pixels, columns=[f'Channel_{i+1}' for i in range(channels)])

# Export DataFrame to Excel
excel_file_path = 'output.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"Data has been exported to {excel_file_path}")
