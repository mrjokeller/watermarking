from ui import UI
from image_processor import ImageProcessor


def main():
    ip = ImageProcessor(None)
    ui = UI(image_processor=ip)
    
    
if __name__ == "__main__":
    main()