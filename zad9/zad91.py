from PIL import Image, ImageFilter
from pathlib import Path

current_dir = ''
filenames = ["1.png", "2.png", "3.png", "4.png", "5.png"]
filenames = Path(current_dir).glob('*')
Path('new91').mkdir(parents=True, exist_ok=True)

for file in filenames:
    with Image.open(file) as img:
        img.load()
        img = img.resize((img.width // 2, img.height // 2))
        img = img.convert("L")
        img = img.filter(ImageFilter.FIND_EDGES)
         img.save(Path("new91", file))
