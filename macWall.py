from os import system, listdir
from PIL import Image

num = int(input('请输入你想生成的缩略图的长: ') )
for pic in listdir('.'):
    if pic[-4:] == '.jpg':
        tmp_pic = pic[:-4] + '.png'
        temp_pic = pic[:-4] + '.bmp'
        system('ffmpeg -i ' + pic + ' -vf scale=' + str(num) + ':-1 ' + tmp_pic)
        system('ffmpeg -i ' + tmp_pic + ' -vf crop=' + str(num) + ':' + str(num * 0.5625) + ' ' + temp_pic)

img = Image.new('RGB', (num, int(num * 0.5625) ), (0, 0, 0) )
zd = eval(input('请输入图片按顺序对应的字典 (参考theme.json文件) : ') )
name = input('请输入图片的前缀名称: ')
for i in range(len(zd)):
    i += 1
    box = (int(num / len(zd) ) * (i - 1), 0, num, int(num * 0.5625) )
    i = zd[i]
    pic = Image.open(name + str(i) + '.bmp')
    tmp = pic.crop(box)
    img.paste(tmp, box)
    pic.close()
system('del *.bmp *.png')
img.save('thumbnail.png')
img.close()
