print("hello mange")

from PIL import Image
from reportlab.pdfgen import canvas

# 图片文件名列表
image_files = ["1.jpg", "2.jpg", "3.jpg"]

# PDF文件名
pdf_filename = "output.pdf"

# 打开一个PDF文件，并设置页面大小（可以根据需要调整）
c = canvas.Canvas(pdf_filename)

for image_file in image_files:
    # 打开图片文件
    img = Image.open(image_file)

    # 获取图片的宽度和高度（以点为单位，1英寸=72点）
    width, height = img.size

    # 根据图片尺寸创建一个PDF页面
    c.setPageSize((width, height))
    
    # 将图片绘制到PDF页面上
    c.drawImage(image_file, 0, 0, width, height)

    # 添加新的页面，准备绘制下一张图片
    c.showPage()

# 保存PDF文件
c.save()
