# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


# def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    # print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助


filename = "1.txt"
# 重新保存的txt文件
new_filename = "2.txt"
# 打开需要修改的和重新保存的txt文件
with open(filename,encoding="utf-8") as f1, open(new_filename,"w",encoding="utf-8") as f2:
    for line in f1:
        new_line = line[81:]     # [:-3] 表示后三个
        f2.write(new_line)
f1.close()
f2.close()