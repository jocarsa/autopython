import os
from PIL import Image
from PIL.ExifTags import TAGS

folder = "fotos"
existing_names = set()

for filename in os.listdir(folder):
    path = os.path.join(folder, filename)
    if not os.path.isfile(path):
        continue

    try:
        with Image.open(path) as image:
            exif = image._getexif()
            if not exif:
                print(f"No EXIF in {filename}")
                continue

            datetime_original = None
            for tag, value in exif.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == "DateTimeOriginal":
                    datetime_original = value
                    break

        if not datetime_original:
            print(f"No DateTimeOriginal in {filename}")
            continue

        date = datetime_original.replace(":", "").replace(" ", "_")
        ext = os.path.splitext(filename)[1].lower()
        new_name = f"{date}{ext}"

        counter = 1
        while new_name in existing_names or os.path.exists(os.path.join(folder, new_name)):
            new_name = f"{date}_{counter}{ext}"
            counter += 1

        new_path = os.path.join(folder, new_name)
        os.rename(path, new_path)
        existing_names.add(new_name)

        print(f"{filename} -> {new_name}")

    except Exception as e:
        print(f"Error processing {filename}: {e}")
