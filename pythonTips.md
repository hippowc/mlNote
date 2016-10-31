1 加载自定义python模块，模块本身无要求，正常写方法，类都ok，不需要export之类的。在引用时：
--在shell中引用。python会在sys.path列表保存的位置进行遍历，若要添加自定义模块，需要在sys.path中添加新路径.
import sys
sys.path.append('xx/xx')
--在文件中引用。
如果要引用的模块当前文件在同一目录，可以直接引用文件名。
若不在同一目录，要先将路径添加到sys.path，在引用文件
import sys
sys.path.append('xx/xx')
import Hello

2 import xx as xx 将引入的模块重命名

3 打开文件open()，即可返回文件对象，或者 with open() as f

4 命令行输入 raw_input("prompt"),返回输入值

5 numpy包用于科学计算