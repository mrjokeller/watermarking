import subprocess
from PIL import Image, ImageDraw, ImageFont


class ImageProcessor:
    
    def __init__(self, image_path: str):
        self.image_path = image_path
        self.watermark = "Watermark"
        
    def has_image(self):
        return self.image_path is not None
    
    def set_image(self, image_path: str):
        self.image_path = image_path
        
    def set_watermark_text(self, text: str):
        self.watermark = text
        
    def set_watermark(self):
        with Image.open(self.image_path) as img:
            size = img.height * img.width
            draw = ImageDraw.Draw(img)
            # font = ImageFont.truetype(<font-file>, <font-size>)
            font = ImageFont.truetype("arial.ttf", 64)
            # draw.text((x, y),"Sample Text",(r,g,b))
            draw.text((50, 50), self.watermark, (255, 255, 255), font=font)
            new_path = self.image_path.split(".")[0] + "_wm.jpg"
            
            img.save(fp=f"{new_path}", format='JPEG')
            
            file_to_show = new_path
            subprocess.call(["open", "-R", file_to_show])
            