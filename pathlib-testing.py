import pathlib

# /Users/mattrosinski/Documents/Repos/Demos/Python-and-R/numpy-practice.py

print(pathlib.Path(__file__))

this_path = pathlib.Path('.')

print(this_path)

this_path.exists()

another_path = pathlib.Path(__file__)

filename = another_path.parts[-1]

folder = another_path.parent

upperfolder = another_path.parent.parent
upperfolder

# Index the number of levels above you want to reference
folder_items = another_path.parents[2]
folder_items

# Create a folder from the script
data_folder = pathlib.Path(__file__).parents[0].joinpath('test-data')
data_folder

if not data_folder.exists():
    data_folder.mkdir()

data_folder.joinpath('myfile.txt').touch(exist_ok=True)
data_folder.joinpath('myfile.csv').touch(exist_ok=True)
data_folder.joinpath('myfile.py').touch(exist_ok=True)
data_folder.joinpath('myfile.json').touch(exist_ok=True)
data_folder.joinpath('myfolder').mkdir(exist_ok=True)

# Use resolve() to convert between Windows and Linux path syntax