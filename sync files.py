# no extra header are required
import os
import shutil

def copy_files()-> None:
    # specify the source and destination folder paths and file extension
    src_folder = "\\Path\\to\\source\\directory"        # path to the source directory
    dest_folder = "\\Path\\to\\destination\\directory"  # path to the destination directory
    file_extension = ".txt" # file extension

    # get a list of files in the source folder
    file_list_source = os.listdir(src_folder)
    file_list_destination=os.listdir(dest_folder)

    for source_file in file_list_source:
        file_path = os.path.join(src_folder, source_file)
        if source_file not in file_list_destination and source_file.endswith(file_extension):
            try:
                shutil.copy2(file_path, dest_folder)
                print(f"Copied {source_file} to {dest_folder}")
            except:
                print(f" {source_file} cannot be copied")
                continue


if __name__ == '__main__':
    copy_files()
  