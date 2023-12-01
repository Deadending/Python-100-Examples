class bcolors:
    HEADER = '\033[95m'     #淡紫色
    OKBLUE = '\033[94m'     #深蓝色
    OKGREEN = '\033[92m'    #深绿色
    WARNING = '\033[93m'    #黄色
    FAIL = '\033[91m'       #红色
    ENDC = '\033[0m'        #重置文本的颜色和样式到默认设置
    BOLD = '\033[1m'        #将文本设置为粗体
    UNDERLINE = '\033[4m'   #将文本设置为下划线

print(bcolors.WARNING + '文本颜色字体？' + bcolors.ENDC)
print(bcolors.OKGREEN + bcolors.UNDERLINE +'文本颜色字体？' + bcolors.ENDC)