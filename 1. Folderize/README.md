# Folderize

**Folderize** is a simple Python tool designed to help you clean up and organize your folder names by capitalizing the first letter of each word, making them more readable and professional. If you have folders with names like `MY FAVORITE SONGS` or `TUPAC SHAKUR (10-20)`, Folderize will rename them to `My Favorite Songs` and `Tupac Shakur (10-20)` respectively.

## Features

- Recursively renames folder names in any directory.
- Capitalizes the first letter of each word, while preserving other characters like parentheses or numbers.
- Lightweight and easy to use.

## Example

- Given a directory structure like this:

```
/Songs 
  ├── TUPAC SHAKUR (10-20)
  └── MY FAVORITE SONGS
```

- After running **Folderize**, the structure will be transformed into:

```
/Songs
  ├── Tupac Shakur (10-20)
  └── My Favorite Songs
```

## Installation

1. Clone the repository:

   ```bash
   $ git clone https://github.com/roshanware/scripts.git
   $ cd scripts/
   $ cd 1.\ Folderize/
   ```

2. Ensure you have Python installed (version 3.6+).

3. No additional dependencies are needed, as this script only uses Python's built-in libraries.

## Usage

1. Run the script and provide the path to the directory you want to process:

```bash
$ python3 main.py
```

2. You will be prompted to enter the directory path:

```bash
[*] Enter the folder path: /path/to/your/folder
```

3.The script will rename all the folders in the specified directory, capitalizing the first letter of each word.

```bash
$ python3 main.py
[*] Enter the folder path: /Users/John/Songs
[*] Renamed: /Users/John/Songs/TUPAC SHAKUR (10-20) -> /Users/John/Songs/Tupac Shakur (10-20)
[*] Renamed: /Users/John/Songs/MY FAVORITE SONGS -> /Users/John/Songs/My Favorite Songs
```

## Contributing

- Feel free to open issues or submit pull requests if you would like to contribute to the project.

## License

- This project is licensed under the MIT License.
