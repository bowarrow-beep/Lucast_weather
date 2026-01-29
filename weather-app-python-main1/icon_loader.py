from PIL import Image, ImageTk

def load_icon(file_path):
    img = Image.open(file_path).resize((50, 50), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)
