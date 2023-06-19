import os
import random
import shutil

main_directory = "dataset"
destination = "test_set"
digits_folders = [os.path.join(main_directory, folder) for folder in os.listdir(main_directory) if os.path.isdir(os.path.join(main_directory, folder))]
num = 1
for folder in digits_folders:
    # all_files = os.listdir(folder)
    for i in range(2):
        random_number = random.randint(1, len(os.listdir(folder)))
        random_number = "{:03d}".format(random_number)
        file_name = f"{random_number}.png"
        file_path = os.path.join(folder, file_name)
        formatted_num = "{:03d}".format(num)
        new_name = f"{formatted_num}.png"
        shutil.move(file_path, os.path.join(destination, new_name))
        num += 1