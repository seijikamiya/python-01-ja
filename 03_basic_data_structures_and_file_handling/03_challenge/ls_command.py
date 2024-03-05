import os


def ls_command(directory):
    # ユーザー入力が「sample」の場合、ディレクトリは「sample」になります
    # 無効なディレクトリパスについて考える必要はありません

    # 「pass」を削除して、ここにコードを書いてください
    extension_dict = {}
    file_list = os.listdir(directory)
    for file in file_list:
        extension = file.split(".")[-1]
        if extension in extension_dict:
            extension_dict[extension] += 1
        else:
            extension_dict[extension] = 1

    print("Summary in alphabetical order:")
    for key, value in sorted(extension_dict.items()):
        if value > 1:
            print(f".{key}:{value} files")
        else:
            print(f".{key}:{value} file")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)
    directory_path = input("Enter directory path to organize files: ")

    if not os.path.isdir(directory_path):
        print("Invalid directory path.")
    else:
        ls_command(directory_path)
