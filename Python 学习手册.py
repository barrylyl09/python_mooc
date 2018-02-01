#encoding:utf-8


'''

# 学习手册_第四版 (课后习题)

'''

'''
第一章：

1. 人们选择 Python 的六个主要原因是什么？

答：软件质量、开发者效率、程序的可移植性、标准库的支持、组件集成和享受简便其中，质量和效率这两条是人们选择 Python 的主要原因。


2. 请列举如今正在使用 Python 的四个著名的公司和组织的名称。

答：Industrial Light & Magic、 EVE Online、 Jet Propulsion Labs、 Maya 和 ESRI 等。
做软件开发的所有组织几乎都流行使用 Python，无论是长期战略产品开发还是测试或系统管理这一的短期策略任务都广泛采用了 Python。


3. 出于什么样的原因会让你在应用中不使用 Python？

答：Python 的缺点是它的性能：它不像 C 和 C++ 这类常规的编译语言运行得那么快。另一方面，它对于绝大多数应用已经足够快了，并且典型的
Python 代码运行起来速度接近 C，因为在 Python 解释器中调用链接了 C 代码。如果速度要求很苛刻的话，应用的数值处理部分可以采用编译好
的扩展以满足应用要求。


4. 你可以用 Python 做什么？

答：你几乎可以在计算机上的任何方面使用 Python：从网站和游戏开发到机器人和航天飞机控制。


5. 在 Python 中 import this 有什么意义？

答：import this 会出发 Python 内部的一个彩蛋，它将显示 Python 语言层面之下的设计哲学。


'''



'''
第二章：

1. 什么是 Python 解释器？

答：Python 解释器是运行 Python 程序的程序。

2. 什么是源代码？

答：源代码是为程序所写的语句：它包括了文本文件（通常以.py 为后缀名）的文本。

3. 什么是字节码？

答：字节码是 Python 将程序编译后所得到的底层形式。Python 自动将字节码保存到后缀名为.pyc 的文件中。

4. 什么是 PVM？

答：PVM 是 Python 虚拟机，它是 Python 的运行时引擎解释编译得到的代码。

5. 请列出两个 Python 标准执行模块的变体的名字。

答：Psyco、Shedskin 以及 forzen binaries 是执行模块的所有变体。

6. CPython、Jython 以及 IronPython 有什么不同？

答: Cpython 是 Python 语言的标准实现。Jython 和 IronPython 分别是 Python 程序的 Java 和.NET 的实现；
它们都是 Python 的编译器的替代实现。

'''

'''
第四章：
1. 列举4个 python 核心数据类型的名称。

答：数字、字符串、列表、字典、元组、文件和集合一般被认为是核心对象（数据）类型。类型、None 和布尔型有时也被定义在这样的分类中。
还有多种数字类型（整数、浮点数、复数、分数和十进制数）和多种字符串类型（Python 2.X中的一般字符串和 Unicode 字符串，以及 Python 3.X 中的文本字符串和字节字符串）

2. 为什么我们把它们称作是"核心"数据类型？

答：它们被认作是"核心"类型是因为它们是 Python 语言自身的一部分，并且总是有效的；为了建立其他的对象，通常必须调用被导入模块的函数。
大多数核心类型都有特定的语法去生成其对象：例如，'spam'是一个创建字符串的表达式，而且决定了可以被应用的操作的集合。正是因为这一点，核心类型与 Python 的语法紧密地结合在一起。
与之相比较，必须调用内置的open 函数去创建一个文件对象。


3. "不可变性"代表了什么，哪三个 Python 的核心类型被认为是具有不可变性的？

答：一个具有 "不可变性" 的对象是一个在其创建以后不能够被改变的对象。Python 中的数字、字符串和元组都属于这个分类。尽管无法就地改变一个不可变的对象，但是
你总是可以通过运行一个表达式创建一个新的对象。


4. "序列" 是什么意思，哪三种 Python 的核心类型被认为是这个分类中的？

答：一个"序列"是一个对位置进行排序的对象的集合。字符串、列表和元组是 Python 中所有的序列。它们共同拥有一般的序列操作，例如：索引、合并以及分片，但又
各自有自己的类型特定的方法调用。


5. "映射"是什么意思，哪种 Python 的核心类型是映射？

答：术语 "映射"，表示将键与相关值相互关联映射的对象。Python 的字典是其核心类型集中唯一的映射类型。映射没有从左至右的位置顺序；它们支持通过键获取数据，
并包含了类型特定的方法调用。


6. 什么是"多态"，为什么我们要关心多态？

答："多态" 意味着一个操作符（如+）的意义取决于被操作的对象。这将变成使用好 Python 的关键思想之一（或许可以去掉之一吧）：不要把代码限制在特定的类型上，使代码自动
适用于多种类型。


'''

'''
第五章：
1. Python 中表达式2 * （3 + 4）的值是多少？

答：14

2. Python 中表达式2 * 3 + 4 的值是多少？

答：10

3. Python 中表达式2 + 3 * 4的值是多少？

答：14

4. 通过什么工具你可以找到一个数字的平方根以及它的平方？

答：导入 math 模块即可

5. 表示式 1 + 2.0 + 3 的结果是什么类型?

答：浮点型

6. 怎样能够截断或舍去浮点数的小数部分？

答： math.floor(N)来计算 floor

7. 怎样将一个整数转换为浮点数？

答：float(I)整数转换为浮点数

8. 如何将一个整数显示成八进制、十六进制或二进制的形式？

答：内置函数 oct(I)和hex(I)会将整数以八进制数和十六进制数字符串的形式返回。

9. 如何将一个八进制、十六进制或二进制数的字符串转成平常的整数？ 

答：int(S, base)函数能够用来让一个八进制和十六进制数的字符串转换为正常的整数（传入 8、16或2作为 base 的参数）


'''


