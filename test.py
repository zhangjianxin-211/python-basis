class Dog:
    def animal(self):
        """在函数内部，三引号是文档说明的意思,跨文件时遇到函数如果有三引号注释可以按ctrl+鼠标左键查看"""
        print('狮子')
        print('猴子')
        print('老虎')

x = Dog()
x.animal()