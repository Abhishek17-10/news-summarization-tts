import os

def ensure_static_folder():
    """Creates 'static' folder if not exists for storing TTS files."""
    if not os.path.exists("static"):
        os.makedirs("static")
