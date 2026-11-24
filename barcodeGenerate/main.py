import barcode
from barcode.writer import ImageWriter
from PIL import Image


def make_barcode(text, out_name="my_barcode"):
    """Generate a Code128 barcode image and return the saved file path."""
    barcode_obj = barcode.get("code128", text, writer=ImageWriter())
    return barcode_obj.save(out_name)


def main():
    text = input("What should the barcode contain? ").strip()

    if not text:
        print("Nothing entered, so no barcode was made.")
        return

    path = make_barcode(text)
    print(f"Barcode saved as: {path}")

    Image.open(path).show()


if __name__ == "__main__":
    main()