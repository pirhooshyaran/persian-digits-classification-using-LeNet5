import cv2
import os
import shutil

# ====== SET DIRECTORIES =====
raw_images_directory = "raw_images"
processed_images_directory = "dataset" # desired path to the being created and processed image data
if not os.path.exists(processed_images_directory):
    os.mkdir(processed_images_directory)
else:
    shutil.rmtree(processed_images_directory)
    os.mkdir(processed_images_directory)

# ===== DEFINE A FUNCTION TO CREATE AN IMAGE DATASET =====
def create_dataset(raw_images_directory, processed_images_directory, classes):
    """
    This function takes raw images path, desired path for process images and classes as arguments.
    Using OpenCV library this function preprocesses each images in the raw directory by resizing
    and applying some filters and thresholds so that raw images become binary images, i.e, pixel values
    are only of two values: 0 for black background and 255 for white digits.
    Finally, it saves images to the selected directory. 
    """
    for clas in classes:
        rawclass_path = os.path.join(raw_images_directory, clas)
        dataclass_path = os.path.join(processed_images_directory, clas)
        if not os.path.exists(dataclass_path):
            os.mkdir(dataclass_path)
        i = 1
        for rawimage in os.listdir(rawclass_path):
            rawimage_path = os.path.join(rawclass_path, rawimage)
            image = cv2.imread(rawimage_path, cv2.IMREAD_GRAYSCALE)
            gray_resized = cv2.resize(image, (32,32), interpolation=cv2.INTER_AREA)
            blur = cv2.GaussianBlur(gray_resized,(5,5),0)
            _, final_image = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
            number = i
            number = "{:03d}".format(number)
            file_path = f"{dataclass_path}\\{number}.png"
            cv2.imwrite(file_path, final_image)
            i += 1

classes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
create_dataset(raw_images_directory, processed_images_directory, classes)