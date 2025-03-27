import os

file_path = r'C:\Users\DELL\Desktop\Computer Science\Sohaib\Selenium\whatsapp.py'

# Check if the file exists
if os.path.exists(file_path):
    try:
        with open(file_path, 'a') as file:
            file.write("\nprint('Hello world')\n")
        print(f"Successfully added to {file_path}")
    except Exception as e:
        print(f"Error: {e}")
else:
    print(f"The file {file_path} does not exist.")



