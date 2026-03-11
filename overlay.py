from PIL import Image, ImageDraw


def draw_levels(image_path, entry, sl, tp1, tp2, tp3):

    img = Image.open(image_path)

    draw = ImageDraw.Draw(img)

    draw.text((50,50), f"Entry: {entry}", fill="white")
    draw.text((50,80), f"SL: {sl}", fill="red")
    draw.text((50,110), f"TP1: {tp1}", fill="green")
    draw.text((50,140), f"TP2: {tp2}", fill="green")
    draw.text((50,170), f"TP3: {tp3}", fill="green")

    img.save(image_path)

    return image_path
