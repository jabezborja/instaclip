from dotenv import load_dotenv
from moviepy.config import change_settings

from app import create_app

load_dotenv()
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)