from PIL import Image
import json
import os
import sys


    # 获取从批处理传递的路径参数
json_path = sys.argv[1]  # 第一个参数是 JSON 文件路径
png_path = sys.argv[2]   # 第二个参数是 PNG 文件路径
    
print(f"接收到的 JSON 文件路径: {json_path}")
print(f"接收到的 PNG 文件路径: {png_path}")
    
    # 在这里添加你的处理代码
    # 比如打开文件、处理内容等等






file=json_path

image = Image.open(png_path)
    #image = Image.open(r"C:\Users\Lenovo\Desktop\TextureAtlas\atlas0.webp")
       
# 创建一个指定大小的透明画布（例如：宽 800px，高 600px）
with open(file, 'r') as f:
    data = json.load(f)
    c=data["frames"]
    #print(data["frames"])
    for i in c.keys():
        x,y,w,h=c[i]["frame"]['x'],c[i]["frame"]['y'],c[i]["frame"]['w'],c[i]["frame"]['h']
        a,b=c[i]["sourceSize"]['w'],c[i]["sourceSize"]['h']
        d,e=c[i]["spriteSourceSize"]['x'],c[i]["spriteSourceSize"]['y']
        #print(x,y,w,h)
        canvas = Image.new('RGBA', (a, b), (255, 0, 0, 0))
        canvas.paste(image.crop((x, y, x+w, y+h)), (d, e), image.crop((x, y, x+w, y+h)))
        file=os.path.dirname(os.path.abspath(__file__))+"\\"+i
        os.makedirs(os.path.dirname(file), exist_ok=True)
        canvas.save(file, "PNG")
        print("保存为 "+file)
        #canvas.save(file, "PNG")
        #canvas = Image.new('RGBA', (800, 600), (255, 0, 0, 0))
# 指定图像放置的位置（例如：左上角放置在 (100, 100) 位置）


# 将图像粘贴到透明画布上，左上角放在 (x, y) 位置
#canvas.paste(image, (x, y), image)  # 第三个参数确保透明度被保留

# 保存结果

#canvas.save("output_image.png")

# 显示图像
#image.show()