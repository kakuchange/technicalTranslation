## Python编程规范

## 翻译自: [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

## 原作者: Guido van Rossum <guido at python.org>, Barry Warsaw <barry at python.org>, Nick Coghlan <ncoghlan at gmail.com>

## 译者: kaku

---

## Python编程规范

- [介绍](#介绍)
- [A Foolish Consistency is the Hobgoblin of Little Minds](#A Foolish Consistency is the Hobgoblin of Little Minds)


### 介绍
这篇文档给出了Python主要发行版的标准库的编程约定(规范), 此外还有相应的C的编程及Python的c实现的规范推荐.[1](#参考内容)

这篇文档和[PEP 257](https://www.python.org/dev/peps/pep-0257/)(Docstring Conventions)字符串文档--改编自Guido最初的Python Style Guide, 并增加了一些Barry's style guide.

这篇文档也在与时俱进.

许多项目有其自己的编程规范, 如果冲突, 项目文档规范优先.

### A Foolish Consistency is the Hobgoblin of Little Minds

Guido的远见之一就是, 代码更经常被阅读想较写而言. 这个"指南"试图增进代码的可读性, 并能保持一致性在更大范围上的Python代码. 正如[PEP 20](https://www.python.org/dev/peps/pep-0020)所言: "Readability counts".

此风格"指南"(我翻译为编程规范)就是有关一致性的指南, 也是些编程规范最重要的. 在一个项目, 一个模块, 一个函数中, 保持一致性是极其重要的.

然而, 有时,此规范或建议并不太适用. 如果你有这样的质疑, 做出你自己的判断. 看看别的例子, 再决定怎样做好. 不要含糊不清, 也不去追问!!

特别的, 不要因为应用些编程规范而不向后兼容!

一些其它的原因忽视一些独有的规范.

1. 应用该规范导致可读性降低, 甚至自带加密时, 很使用些规范.

2. 由于某些原因(如历史遗留原因), 要保持与周围的代码风格保持一致--然而, 这也是一个从混乱状态中恢复的机会.

3. 先于此规范写的成代码, 并且没有任何要修改这段代码的必要.

4. 此规范所推荐做法, 与老版本不兼容, 而又要保持向后兼容

### 代码布局

####缩进

每一级缩进使用4个空格

续行(被圆括号, 中括号, 花括号, or using a hanging indent所包裹的元素)应该在竖直方向上排列. 当使用 hanging indent 下面的问题应该被考虑: 第一行不应该有参数, 并且续行应该用缩进分隔开(以区别出这是续行~).

正例:

**Aligned with opening delimiter.**
```
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
```

**More indentation included to distinguish this from the rest.**
```
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
```

**Hanging indents should add a level.**
```
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

反例:

**Arguments on first line forbidden when not using vertical alignment.**
```
foo = long_function_name(var_one, var_two,
    var_three, var_four)
```

**Further indentation required as indentation is not distinguishable.**
```
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

4个空格的缩进在续行中是可选

可选:

**Hanging indents *may* be indented to other than 4 spaces.**
```
foo = long_function_name(
  var_one, var_two,
  var_three, var_four)
```

When the conditional part of an if-statement is long enough to require that it be written across multiple lines, it's worth noting that the combination of a two character keyword (i.e. if), plus a single space, plus an opening parenthesis creates a natural 4-space indent for the subsequent lines of the multiline conditional. This can produce a visual conflict with the indented suite of code nested inside the if-statement, which would also naturally be indented to 4 spaces. This PEP takes no explicit position on how (or whether) to further visually distinguish such conditional lines from the nested suite inside the if-statement. Acceptable options in this situation include, but are not limited to:
(这一段说, 对于较长的if else 语句, pep8中没有规定具体的做法, 但指出并不"值得"像上面一样,用圆括号分隔并以4个空格缩进区分, 因为可能会造成潜在的冲突. 同时也有一些可供选择的做法:)

**No extra indentation.(没有额外的缩进,在圆括号下)**
```
if (this_is_one_thing and
    that_is_another_thing):
    do_something()
```

**Add a comment, which will provide some distinction in editors**
**supporting syntax highlighting.**
```
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()
```

**Add some extra indentation on the conditional continuation line.**
```
if (this_is_one_thing
        and that_is_another_thing):
    do_something()
```

(相应的可以看下面的关于是否打断(break)在binary operator之前或之前的讨论)

闭合的圆括号, 中括号, 大括号, 在multiline constructs 可以与最后一组元素相并齐, 或者在和multiline construct并齐, 具体看下两种. 

1. line up under the first non-whitespace character of the last line of the list, as in.

```
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )
```

2. or it may be lined up under the first character of the line that starts the multiline construct, as in:

```
my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```

#### Tabs or Spaces?

推荐使用空格, Space are the preferred indentation method.

Tabs 应该用在已经使用Tabs的代码里.

Python3 不允许混合使用Tabs 与 Spaces缩进.

Python2 使用混合缩进的, 应改为单一的Spaces缩进. 

当以`-t`标识调用Python2命令行解释器时, 将检查混合使用的缩进(warning level), `-tt`将使级别上升到error, 非常建议这么做.

#### Maximum Line Length

限制每一行长度最大为 **79** 字符.

对于没有结构限制的大段文字(文档字符串, 注释), 最大行长应为**72**

限制所需的窗口大小, 可以并排打开很多文件, 这会在使用code review tools时, 在相近的列中展示2个版本.

默认的折叠(wrapping)在大多数的工具, 使代码结构被破坏, 使之很难理解. 同时在不同编辑器中, 最大长度可以设置为80. (even if the tool places a marker glyph in the final column when wrapping lines. some web based tools may may not offer dynamic line wwrapping at all.)(这一段不重要, 后面如果不重要的部分,我会给出原文.)

对长度的问题, 不同偏好的可以不同, 但一般在80~100, docstrings仍然是72的字符比较适宜.(The Ptyhon standard library is conservative and requires limit lines to 79 characters and docstrings/comments to72.)

再理想的折叠长行的方式是, 使用Python 隐式的续行, 在parentheses, brackets and braces. 更应该使用反斜来进行续行. 

反斜仍在一些场合很有用, 如, 长的多重的with 语句, 不能使用隐式的续行, 像下面这样做:

```
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```

(相关的关于多个if 语句的讨论见前面, 此外类似的还有```assert```)

#### Should a line break before or after a binary operator?

2种风格, 第二种更值得推荐(对匹配操作数与操作符更方便), 但无论哪种, 保持统一.

1. **No: operators sit far away from their operands**
```
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```

2. **Yes: easy to match operators with operands**
```
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

#### Blank Lines

最顶层的函数和类定义间, 2个空行

类中方法定义间, 1个空行

额外的换行可以被用于(节俭地, 保守地,爱惜地)分开一组相关的函数, 空行也可能被省略, 在一组相关的虚拟方法(类似于基类方法,个人理解)e.g. a set of implementations.

要一个函数中, (节俭地,爱惜地)使用空行来分隔逻辑部分.

Python accepts the control-L(i.e. ^L) form feed character as whitespace; Many tools trea these characters as page separators, so you may use them to separate pages of related sections of you file. Note, some editors and webbased code viewers may not recognize control-L as a form feed and will show another glyph in its place.
(这段说一些特殊的控制字符,可以用于代码逻辑划分, 在一些编辑器中可以正常显示, 但基于web的显示可能会不正常.)

#### Source File Encoding

在Python的核心发布版中应该使用UTF-8(or ASCII in Python2)

在Python3在使用UTF-8 或 Python2中使用ASCII 不用声明.

在标准库中, 非默认的encode(编码方式)应该仅用于测试目的...(or when a comment or docstring needs to mention an author name that contains non-ASCII characters; otherwise, using \x, \u, or \N escapes is the preferred way to include non-ASCII data in string literals.)这一段说在仅在特定的情况下, 用\x等标识来包括这些非ASCII的字符.

对于Python3.0 或更高, 下面这些规定是针对标准库的: 所有的标识符都必须使用只使用ASCII, 并且应该用英语单词, 在任何可行的时候(在很多情况下, 缩写和技术词汇都不是英语). 此外, 字符串和注释也必须使用ASCII. 唯一的另外是 a.测试非ASCII的测试, b.作者的名字. (还说要提供名字的翻译= =).

受众广的开源项目被鼓励采用类似的策略.

#### imports

- Imports 应该分行写,如:

    Yes: import os
        import sys

    No:  import sys, os

    也可以这样:

    from subprocess import Popen, PIPE

- Imports 总是应该写在文件的开头, 在模块文档和注释之后, 模块全局变量和常量之前.

    import 的顺序:
    1. 标准库
    2. 相关第三方库
    3. 本地自定义库

- 绝对导入被推荐, 由于这样易读并且表现更好(或者至少给出更好的error messages). (if the import system is incorrectly configured such as when a direcotry inside a package ends up on sys.path):

```
    import mypkg.sibling
    from mypkg import sibling
    from mypkg.sibling import example
```

    然而, 显示的相对导入也是一个可选方案, 尤其是在应对一个复杂的包布局时, 使用绝对导入可能会不必要的复杂.
    
```
    from . import sibling
    from .sibling import example
```

- 当导入一个类, 从一个包含此类的模块中时, 这样做是OK的:

```
    from myclass import MyClass
    from foo.bar.youclass import YourClass
```

    如果可能导入类名冲突(如, 许多个Utils类)这样做:

```
    import myclass
    import foo.bar.youclass
```
    and use `myclass.MyClass` and `foo.bar.yourclass.YourClass`
    
- 通配符的导入(`from <module> import *`)应该避免, 由于这样使得变量名(各种名都在当前的命名空间下)(as they make it unclear which names are present in the namespace, confusing both readers and automated tools), 造成混乱. 除非,你想使另一个模块覆盖pure Python implementation. 

这样做之后, the guidelines below regarding public and internal interfaces still apply.

#### Module level dunder names

Module level "dunders" (i.e. names with two leading and two trailing underscores) such as __all__, __author__, __version__, etc. should be placed **after** the module docstring but **before** any import statements except from __future__ import. Python mandates that future-imports must appear in the module before any other code except docstrings.(这一段说, __all__等几个特殊的"dunders"应该在模块docstring之后, from __future__ import xxx 之后.)

For example:

```
from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys
```

### String Quotes

在Python中, 单引号与双引号是相同的作用. 此PEP不对此作推荐. 任选其一并遵守. 当字符串包括两者时, 可避免使用反斜转义, 这有助于提升可读性.

对三引号来说,惯例上应该使用双引号来包含docstring, 在PEP257中.

### Whitespace in Expressions and Statements

**Pet Peeves**

Avoid extraneous whitespace in the following situations(避免以下情形的额外空格)

- 避免紧挨着圆括号, 中括号, 大括号

Yes: spam(ham[1], {eggs: 2})
No:  spam( ham[ 1 ], { eggs: 2 } )

- 在闭合的括号的逗号后

Yes: foo = (0,)
No:  bar = (0, )

- 避免紧挨着, ; :之前

Yes: if x == 4: print x, y; x, y = y, x
No:  if x == 4 : print x , y ; x , y = y , x

- 对于切片操作看下示例(原文讲的絮絮叨叨的= =)

Yes:

ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]
No:

ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]

- 避免带参数的函数调用(括号前,见下示例)

Yes: spam(1)
No:  spam (1)

- 索引操作示例

Yes: dct['key'] = lst[index]
No:  dct ['key'] = lst [index]

- 赋值操作示例

Yes:

x = 1
y = 2
long_variable = 3
No:

x             = 1
y             = 2
long_variable = 3

#### Other Recommendations

- Avoid trailing whitespace anywhere. Because it's usually invisible, it can be confusing: e.g. a backslash followed by a space and a newline does not count as a line continuation marker. Some editors don't preserve it and many projects (like CPython itself) have pre-commit hooks that reject it.(避免在行尾加空格, 这可能导入与反斜共同使用时, 续行不生效等原因.)

- Always surround these binary operators with a single space on either side: assignment (=), augmented assignment (+=, -= etc.), comparisons (==, <, >, !=, <>, <=, >=, in, not in, is, is not), Booleans (and, or, not).(在这些操作符的2侧, 一般都保有空格).

- If operators with different priorities are used, consider adding whitespace around the operators with the lowest priority(ies). Use your own judgment; however, never use more than one space, and always have the same amount of whitespace on both sides of a binary operator. 额外的还可添加空格用以区别不同优先级的计算等.

Yes:

i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
No:

i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

- Don't use spaces around the = sign when used to indicate a keyword argument or a default parameter value.(在函数的关键词参数的赋值语句2侧不使用空格.)

Yes:

def complex(real, imag=0.0):
    return magic(r=real, i=imag)
No:

def complex(real, imag = 0.0):
    return magic(r = real, i = imag)

- Function annotations should use the normal rules for colons and always have spaces around the -> arrow if present. (See Function Annotations below for more about function annotations.)(函数注释定义示例)

Yes:

def munge(input: AnyStr): ...
def munge() -> AnyStr: ...
No:

def munge(input:AnyStr): ...
def munge()->PosInt: ...

- When combining an argument annotation with a default value, use spaces around the = sign (but only for those arguments that have both an annotation and a default).(函数注释定义示例)

Yes:

def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
No:

def munge(input: AnyStr=None): ...
def munge(input: AnyStr, limit = 1000): ...

- Compound statements (multiple statements on the same line) are generally discouraged.(一行多个语句不被鼓励)

if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()
Rather not:

if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()

- While sometimes it's okay to put an if/for/while with a small body on the same line, never do this for multi-clause statements. Also avoid folding such long lines!(偶尔的一行表示if/for/while也是OK的, 但要避免多个子语写成一行, 示例)

Rather not:

if foo == 'blah': do_blah_thing()
for x in lst: total += x
while t < 10: t = delay()
Definitely not:

if foo == 'blah': do_blah_thing()
else: do_non_blah_thing()

try: something()
finally: cleanup()

do_one(); do_two(); do_three(long, argument,
                             list, like, this)

if foo == 'blah': one(); two(); three()

### When to use trailing commas

尾部的逗号通常是可选项, 除非是在单元素的元组中(及Pyton2中 print语句), 在括号中的冗余的逗号是被推荐的.

Yes:

FILES = ('setup.cfg',)
OK, but confusing:

FILES = 'setup.cfg',

When trailing commas are redundant, they are often helpful when a version control system is used, when a list of values, arguments or imported items is expected to be extended over time. The pattern is to put each value (etc.) on a line by itself, always adding a trailing comma, and add the close parenthesis/bracket/brace on the next line. However it does not make sense to have a trailing comma on the same line as the closing delimiter (except in the above case of singleton tuples).(说明优点, 示例)

Yes:

FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )
No:

FILES = ['setup.cfg', 'tox.ini',]
initialize(FILES, error=True,)

### Comments

注释不清晰, 比没有注释更糟. 及时更新注释, 在代码更新时!(优先级很高)

注释应该是完整的句子, 第一个单词的首字母应该大写, 除非这个首字母是某个标识符(本身就是小写)

大段注释由一个或多个段落组成, 每一句以句号结尾. 

每句间除了句点外, 加两个空格, 除非是最后一句

非英语使用者, 用英语注释, 除非你确定没有非你母语者阅读代码.

#### Block Comments

大段注释, #后加一个空格表示.

段落在被单独一个#来分隔开.

#### Inline Comments

少用(珍惜使用)行内注释.

行内注释是指注释与代码在同一行, 行内的注释应该至少与代码用2个空格分隔开, 然后以#分隔, 再加1个空格

表示意图很清晰的代码不必用行内注释, 如:

x = x + 1                 # Increment x

But sometimes, this is useful:

x = x + 1                 # Compensate for border

#### Documentation Strings

好的字符串文档的约定(也称docstrings)在PEP257中给出了标本.

- 为所有的public modules, functions, classes, and methods写docstrings, 非公共的methods不必, 并你也应该有相应 的注释来说明它的作用. (这样的注释一般出现在def后一行.)

- PEP 257 描述了好的docstings 的约定, 提示: 结束multiline docstring 应该自成一行, 如:

"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""

- 对于一行的注释, 结束的"""应该在同一行(译者注: 我并不喜欢这么做...).




### Naming Conventions

Python library的命名习惯有一点混乱, 应此, 我们从没有完全统一. 然而, 还是有一些目前被建议的命名标准. 新的模块和包(包括第三方), 应该该这些标准来写, 但当已经存在的库有不同的标准时, 保持内部的统一更好.

#### Overriding Principle 最重要的原则

对暴露给使用者的公共接口, 应该遵循反应使用而非实现的原则.

#### Descriptive: Naming Styles(写实,描述性的命名风格)

这有很多不同的命名风格, 这帮助认识哪种风格被使用, (由它们被用来做什么).

下面常见的不同的命名风格:

- b(single lowercase letter)
- B(single suppercase letter)
- lowercase
- lower_case_with_underscores
- UPPERCASE
- UPPER_CASE_WITH_UNDERSCORES
- CapitalizedWords(or CapWords, or CamelCase -- so names because of the bumpy look of its letters. This is alse sometimes known as StudlyCaps)

Note: 当使用驼峰命名法时, 缩写的首字母应该大写, 如HTTPServerError is better than HttpServerError. 

- mixedCase

- Capitalized_Worlds_With_Underscores(ugly!)

同时也有关于使用前缀, 表示一组相关名字的风格, 这不常用在Python中, 但这也提及出于完整性的考量. 如: the os.stat() function returns a tuple whose items traditionally have names like st_mode, st_size, st_mtime and so on. (this is done to emphasize the correspondence with the fields of the POSIX system call struct, which helps programmer familiar with that.)












### 引用
1. [1 PEP7 Style Guide for c Code, van Rossum](https://www.python.org/dev/peps/pep-0007/)

2. 2 Barry's GUN Mailman style guide [http://barry.warsaw.us/software/STYLEGUIDE.txt](http://barry.warsaw.us/software/STYLEGUIDE.txt)

3. 


## 注意

- 个人翻译, 经验能力有限, 难免不准确(一般都附有该段原文), 欢迎指正.

- 图片均来自互联网, 有出处都给出链接, 如有侵犯所有权, 请联系我, 
E-mail: scugjs@gmail.com. 