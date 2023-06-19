import os
import random


main_directory = "raw_images"

digits_folders = [os.path.join(main_directory, folder) for folder in os.listdir(main_directory) if os.path.isdir(os.path.join(main_directory, folder))]

for digit_folder in digits_folders:
    file_names = os.listdir(digit_folder)
    random.shuffle(file_names)

    for i, file_name in enumerate(file_names):
        file_extension = os.path.splitext(file_name)[1]
        number = "{:03d}".format(i+1)
        new_file_name = f"{number}.png"
        old_file_path = os.path.join(digit_folder, file_name)
        new_file_path = os.path.join(digit_folder, new_file_name)
        os.rename(old_file_path, new_file_path)