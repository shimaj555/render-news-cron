# daily_news_chapter.py -- Render上での動作テスト用（5秒の簡易動画を作る）
from moviepy.editor import ImageClip, AudioFileClip
from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

# 1) 画像を作る（PIL）
img_path = "test_img.png"
w, h = 1280, 720
img = Image.new("RGB", (w, h), color=(30, 60, 120))
draw = ImageDraw.Draw(img)
text = "Render Test\ndaily_news_chapter"
# フォント指定がなければデフォルトで描画
draw.text((50, 300), text, fill=(255,255,255))
img.save(img_path)
print("Created image:", img_path)

# 2) 画像を動画化（5秒）
clip = ImageClip(img_path).set_duration(5)
outname = f"render_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
clip.write_videofile(outname, fps=24)
print("Written video:", outname)

# 3) 簡単に環境変数が渡っているか確認（安全のためマスク）
for k in ["OPENAI_API_KEY","NEWSAPI_KEY","ELEVENLABS_KEY"]:
    v = os.getenv(k)
    print(f"{k} set? ->", "YES" if v else "NO")
