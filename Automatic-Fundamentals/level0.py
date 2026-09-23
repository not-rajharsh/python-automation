'''
Learn:
- `os`
- `pathlib`
- `shutil`
- `glob`
- `subprocess`
- `datetime`
- `time`
- `json`
- `csv`
'''





#os 
#helps to work with computer os & automate system work

import os 
if(not os.path.exists("data")):
    os.mkdir("data.txt")

for i in range(0,9):
    os.mkdir(f"Level-{i+1}")

for i in range(0,9):
    os.rename(f"Level-0/test", f"Level-0/test-renamed")

folders=os.listdir("")







#pathlib 

#create and join path 

from pathlib import Path
# Create path
p = Path('/home/user') / 'projects' / 'demo.txt'
# Join parts
q = Path('/etc').joinpath('init.d', 'reboot')   

#Extract parts of the path without string manipulation.
p = Path('/home/user/docs/report.pdf')
print(p.name)      # 'report.pdf'
print(p.stem)      # 'report' (name without suffix)
print(p.suffix)    # '.pdf'
print(p.parent)    # PosixPath('/home/user/docs')
print(p.root)      # '/' (for absolute paths)   

#Resolve relative paths to absolute ones or access user directories.
# Current working directory
cwd = Path.cwd()
# User's home directory
home = Path.home()
# Resolve symlinks and get absolute path
absolute_path = Path('relative/path').resolve()
# Expand user shorthand (~)
config = Path('~/.config/app.json').expanduser()   

#Verify existence and type before performing operations.
p = Path('/some/path')
print(p.exists())   # True if path exists
print(p.is_file())  # True if regular file
print(p.is_dir())   # True if directory
print(p.is_symlink()) # True if symbolic link   

#Use built-in methods for simple text I/O, avoiding explicit open() calls for small files.
p = Path('data.txt')
# Write text (creates file if it doesn't exist)
p.write_text('Hello, World!', encoding='utf-8')
# Read text
content = p.read_text(encoding='utf-8')   

#Create, list, and walk directories efficiently.
d = Path('/tmp/mydir')
# Create directory (parents=True creates intermediate dirs)
d.mkdir(parents=True, exist_ok=True)
# List immediate children
for entry in d.iterdir():
    print(entry)
# List files only
files = [i for i in d.iterdir() if i.is_file()]
# Recursively find files by pattern
csvs = list(d.rglob('*.csv'))   


#Rename, remove, and change permissions.
p = Path('old.txt')
target = Path('new.txt')

# Rename or move
p.rename(target)

# Remove file
p.unlink()

# Remove empty directory
d.rmdir()

# Change permissions
p.chmod(0o755)   








#shutil
#Copying Files: Use shutil.copy(src, dst) to copy file contents and permissions, or shutil.copy2(src, dst) to also preserve metadata like timestamps. shutil.copyfile(src, dst) copies only the contents without metadata. 

import shutil

# Basic copy (permissions only)
shutil.copy("source.txt", "destination.txt")

# Copy with metadata (timestamps, permissions)
shutil.copy2("source.txt", "destination.txt")

# Copy only contents
shutil.copyfile("source.txt", "destination.txt")



#Moving and Renaming: shutil.move(src, dst) moves or renames files and directories. If the destination is a directory, the source is moved inside it. 

import shutil

# Move file to new location
shutil.move("file.txt", "/new/location/file.txt")

# Rename file (move within same directory)
shutil.move("old_name.txt", "new_name.txt")


#Directory Operations: Use shutil.copytree(src, dst) to recursively copy an entire directory tree, and shutil.rmtree(path) to permanently delete a directory and all its contents. 

import shutil

# Copy entire directory recursively
shutil.copytree("source_dir", "dest_dir")

# Delete directory and all contents
shutil.rmtree("directory_to_delete")


#Archiving and Utilities: shutil.make_archive() creates ZIP/TAR archives, shutil.unpack_archive() extracts them, and shutil.disk_usage() checks available disk space. 

import shutil

# Create ZIP archive
shutil.make_archive("backup", "zip", root_dir="source_dir")

# Check disk usage
usage = shutil.disk_usage(".")
print(f"Free: {usage.free / (1024**3):.2f} GB")

# Find executable in PATH
python_path = shutil.which("python3")






