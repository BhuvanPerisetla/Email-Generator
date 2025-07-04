import os

for root, dirs, files in os.walk("C:/Users/bhuva/Desktop/Email generator"):
    for file in files:
        if file.endswith(".pyc") or "__pycache__" in root:
            try:
                os.remove(os.path.join(root, file))
            except:
                pass
