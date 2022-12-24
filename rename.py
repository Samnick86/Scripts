import os

# Set the path to the folder containing the files to be renamed
path = r"C:\Users\UserName\desktop\folderwithfiles"

# Get a list of the `.psd` files in the folder, sorted by name
files = sorted([f for f in os.listdir(path) if f.endswith(".psd")])

# Set the counter to 1
counter = 1

# Loop through each file in the list
for file in files:
  # Build the new file name using the counter and the file extension
  new_name = f"{counter}.psd"

  # Rename the file
  os.rename(os.path.join(path, file), os.path.join(path, new_name))

  # Increment the counter
  counter += 1
