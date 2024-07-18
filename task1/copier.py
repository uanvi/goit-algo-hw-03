import os
import shutil
import argparse

def copy_files_r(source_dir, dest_dir):
    """Copy files from source dir to dest dir"""
    try:
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            if os.path.isdir(source_item):
                # use recursion for nested directories
                new_dest_dir = os.path.join(dest_dir, item)
                os.makedirs(new_dest_dir, exist_ok=True)
                copy_files_r(source_item, new_dest_dir)
            elif os.path.isfile(source_item):
                # copy file
                file_extension = os.path.splitext(item)[1].lstrip('.').lower()
                if not file_extension:
                    file_extension = 'no_extension'
                extension_dir = os.path.join(dest_dir, file_extension)
                os.makedirs(extension_dir, exist_ok=True)
                shutil.copy2(source_item, os.path.join(extension_dir, item))
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Recursively copy files and sort by extension.")
    parser.add_argument('source_dir', type=str, help='Source directory path')
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help='Destination directory path (default is dist)')
    args = parser.parse_args()


    if not os.path.exists(args.source_dir):
        print(f"Error: Source directory '{args.source_dir}' does not exist.")
        return

    os.makedirs(args.dest_dir, exist_ok=True)

    copy_files_r(args.source_dir, args.dest_dir)

if __name__ == "__main__":
    main()
