from pdf2image import convert_from_path

# PDF 文件路径
pdf_path = "input.pdf"
print("開始轉換")
# 转换 PDF 为图像
images = convert_from_path(pdf_path, dpi=300)  # dpi可调整分辨率
print("轉換中...")
# 保存每一页为 JPG 文件
for i, image in enumerate(images):
    image.save(f"output_page_{i+1}.jpg", "JPEG")

print("轉換完成！")
