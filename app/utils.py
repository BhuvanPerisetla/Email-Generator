def clean_text(text):
    import re
    text = re.sub(r'<[^>]*?>', '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    return ' '.join(text.split())
