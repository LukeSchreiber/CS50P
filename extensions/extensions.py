# Prompt user for file name
file_name = input("File name: ").strip().lower()

# Extract extension after last '.' (or empty if none)
extension = file_name.rsplit('.', 1)[-1] if '.' in file_name else ''

# Match extension to media type
if extension == 'gif':
    print("image/gif")
elif extension in ('jpg', 'jpeg'):
    print("image/jpeg")
elif extension == 'png':
    print("image/png")
elif extension == 'pdf':
    print("application/pdf")
elif extension == 'txt':
    print("text/plain")
elif extension == 'zip':
    print("application/zip")
else:
    print("application/octet-stream")
