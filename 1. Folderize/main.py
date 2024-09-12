import os
from typing import List

def main(path: str) -> None:
    for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            old_path: str = os.path.join(root, name)
            new_name: str = rename_folder_name(name)
            new_path: str = os.path.join(root, new_name)
            if old_path != new_path:
                try:
                    os.rename(old_path, new_path)
                    print(f"[*] Renamed: {old_path} -> {new_path}")
                except OSError as e:
                    print(f"[*] Error renaming {old_path}: {e}")

def rename_folder_name(name: str) -> str:
    components: List[str] = name.split(" ")
    renamed_components: List[str] = []
    for comp in components:
        if comp.isalpha():
            renamed_components.append(comp.capitalize())
        else:
            renamed_components.append(comp)
    return " ".join(renamed_components)

if __name__ == '__main__':
    directory_path: str = input('[*] Enter the folder path: ').strip()
    main(directory_path)