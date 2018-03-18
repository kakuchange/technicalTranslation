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

The X11 library uses a leading X for all its public functions. In Python, 这样的风格是不必须的, 因为所有的属性方法都有相同的类名为前缀, 而函数都有module名为前缀.

此外, 以下特殊的形式(使用在开头或尾部的下划线), 是被认可的(这样的形式可以与其它约定结合使用, 通常):

- _single_leading_underscore: 仅在内部使用的标志. 如: from M import * does not import objects whose name starts with an underscore.

- single_trailing_underscore_: 被约定用来避免跟Python关键词冲突.eg:

```Tkinter.Toplevel(master, class_='ClassName')```

- __double_leading_underscore: 用来非公有变量, when naming a class attribute, invokes name mangling (inside class FooBar, __boo becomes _FooBar_boo; see blow).

- \_\_double_leading_and_trailing_underscore\_\_: "magic" objects or attributes that live in user-controlled namespaces. Eg:. \_\_init\_\_, \_\_import\_\_ or \_\_file\_\_. Never invent such name; only use them as documented. 前后双下划线的为魔术方法(属性), 不要创造这样的名字, 并且使用它们按文档说明.

#### Prescriptive: Naming Conventions

**Names to Avoid**

不要使用"l", "o", 作为一个单字母的变量.

在某些字体中, 很难它们与1, 0 ,分开, 应该代而使用大写的L, 代替l.

**ASCII Compatibility**

标识符在标准库中必须使用ASCII能兼容的, 在pep 3131中有描述.

**Package and Module Names**

模块(module)名应该简短, 全为小写字母. 下划线可以被使用, 如果能提前可读性. Python 包(package)也应该是简短小写字母, 然而下划线不被推荐使用.

When an extension module written in C or C++ has an accompanying Python module that provides a higher level (e.g. more object oriented) interface, the C/C++ module has a leading underscore (e.g. _socket).(这一段说, 当拓展模块为c/c++, 并有相应的Python module 提供更高层级的接口(更面向对象), c/++应该有前缀的下划线, 如:_socket).

**Class Name**

类名一般约定使用首字母大写风格.

The naming convention for functions may be used instead in cases where the interface is documented and used primarily as a callable.(我的理解: 对于函数名的约定也可这样用, 而非文档中所记录的主要被用做callable的用途. ps: 感觉不通顺...但意思到了.)

注意, 对于builtin names 有独立的约定. 大多数的builtin names 为单个单词(或2个单词合并(run together)), CapWords(大驼峰命名法)仅在Exception, builtin constants(异常命名与内建常量)中使用.

**Type variable names**

Names of type variables 在PEP 484中被介绍, 通常使用CapWords preferring short names: T, AnyStr, Num. 被推荐增加前缀, _co or _contra to the variables used to declare covariant or contravariant(增加这2种前缀, 表示该变量为"协同变量", 或"逆变量").eg:

```
from typing import TypeVar

VT_co = TypeVar('VT_co', covariant=True)
KT_contra = TypeVar('KT_contra', contravariant=True)
```

**Exception Names**

由于异常应该是一个类, 类名的规定这里也适用, 然而, 你应该使用Error(suffix)尾缀.

**Global Variable Names**

(Let's hope that these variables are meant for use inside one module only.) The conventions are about the same as those for functions.(对于只在内部使用的变量, 与前面function的约定相同)

Modules that are designed for use via from M import * should use the \_\_all\_\_ mechanism to prevent exporting globals, or use the older convention of prefixing such globals with an underscore (which you might want to do to indicate these globals are "module non-public"). (使用\_\_all\_\_或者显示的加下线前缀, 来指明哪些是module不暴露给外部的)

**Functioin and variable names**

Function names should be lowercase, with words separeted by underscores as necessary to improve readability.(函数名应该小写, 有必要的话可以以下划线分隔开)

变量名与函数名约定相同.

mixedCase is allowed only in contexts where that's already the prevailing style (e.g. threading.py), to retain backwards compatibility.(mixedCase这种命名, 仅在已经这样使用, 出于兼容性考虑时被允许, 如threading.py)

**Function and method arguments**

使用self 作为实例方法的第一个参数.

使用cls 作为类方法的第一个参数.

如果函数的参数与保留关键词冲突, 通常更好的做法是在尾部加下划线而非使用缩写或(spelling corruption). 因此, class_ is better than clss. (也许使用同义词会更好)

**Method Names and Instance Variables**

与函数命名规则相同: lowercase with words separated by underscores as necessary to imporve readablity.

Use one leading underscore only for non-pablic methods and instace variables.(仅在非暴露的方法或实例属性(变量)前加下划线)

为了避免名字冲突与子类, 使用__(双下划线非公有) to invoke Python's name mangling rules.

Python mangles these names with the class name: if class Foo has an attribute name \_\_a, if can't be accessed by Foo.\_\_a. (An insistent user could still gain access by calling Fooo._Foo__a.) Generally, double leading underscores should be used only to avoid anme conflicts with attributes in classes designed to be subclassed.(这一段说, 双下划线开头的类属性(非公有), 可以避免在子类继承时发生名字冲突, 这时对非公有的类属性的在类外的访问, 須像上面给出的那样访问. 这也是这么设计的初衷.)

Note: there is sone controversy about the use of \_\_names (see below). (关于\_\_name的使用还有争论, 看下面).

**Constants**

常量经常定义在模块级, 并且全部以大写字母加下划线分隔单词. 例如: MAX_OVERFLOW and TOTAL.

**Designing for inheritance**

Always decide whether a class's methods and instance variables (collectively: "attributes") should be public or non-public. if in doubt, choose non-public; it's easier to make it public later than to make a public attribute non-public.(思考决定一个类的方法或,实例变量(统称为属性), 应该是公有还是非公有, 如果你不知道, 应该选择非公有. 因为之后如果你想使之成为公有,比公有变非公有, 更容易).

Public attributes are those that you expect unrelated clients of your class to use, with your commitment to avoid backward incompatible changes. Non-public attributes are those that are not intended to be used by third parties; you make no guarantees that non-public attributes won't change or even be removed.(这段说, 一个公有的属性是你期望与类客户端使用无关的, 这些属性你承诺会避免出现向后不兼容的改动. 非公有, 即非公有属性, 是不打算被其它三方使用的, 你也不保证该非公有属性不会改动, 甚至移除.)

We don't use the term "private" here, since no attribute is really private in Python (without a generally unnecessary amount of work).(我们不用"private"(私有), 由于Python中没有真正意义上的私有属性(Python没有做通常上是不必要的一系列工作))

Another category of attributes are those that are part of the "subclass API" (often called "protected" in other languages). Some classes are designed to be inherited from, either to extend or modify aspects of the class's behavior. When designing such a class, take care to make explicit decisions about which attributes are public, which are part of the subclass API, and which are truly only to be used by your base class.(另一类属性是那些子类的接口, (在其它语言中称为protected), 一些类被设计用来继承, 拓展或调整类的某方面表现, 当设计这样的类时, 特别小心的显示决定哪些属性是公有, 哪些是类的API之一, 哪些仅在基类中使用.)

With this in mind, here are the Pythonic guidelines:(这有些更Pythonic的指引)

- Public attributes should have no leading underscores.(公有属性, 应该没有前缀的下划线.)

- If your public attribute name collides with a reserved keyword, append a single trailing underscore to your attribute name. This is preferable to an abbreviation or corrupted spelling. (However, notwithstanding this rule, 'cls' is the preferred spelling for any variable or argument which is known to be a class, especially the first argument to a class method.)(前面说过, 关于函数参数与保留关键词冲突时的做法, 这里public attribute 一样. 不同的是, cls是类方法的第一个关键词)

Note 1: See the argument name recommendation above for class methods.(注意, 参照前面有关类方法的命名推荐)

- For simple public data attributes, it is best to expose just the attribute name, without complicated accessor/mutator methods. Keep in mind that Python provides an easy path to future enhancement, should you find that a simple data attribute needs to grow functional behavior. In that case, use properties to hide functional implementation behind simple data attribute access syntax.(这段说, 对于简单的公有数据属性, 暴露简单的属性访问比暴露一个复杂的函数调用更好, @property 实现, 后面会有一篇来说明property是如何工作的.)

Note 1: Properties only work on new-style classes.(注意: property只在新式类使用)

Note 2: Try to keep the functional behavior side-effect free, although side-effects such as caching are generally fine.(这段说, 对这样做的副作用要free? ps:猜测意为自由的, 不影响主要作用的...例如:缓存通常是可以接受的)

Note 3: Avoid using properties for computationally expensive operations; the attribute notation makes the caller believe that access is (relatively) cheap.(避免在计算密集型的操作上使用property, 像属性一样的访问, 使得调用者认为这样访问是(相对)cheap(容易?))

If your class is intended to be subclassed, and you have attributes that you do not want subclasses to use, consider naming them with double leading underscores and no trailing underscores. This invokes Python's name mangling algorithm, where the name of the class is mangled into the attribute name. This helps avoid attribute name collisions should subclasses inadvertently contain attributes with the same name.(使用非公有属性, 如果你的类被设计用来继承, 并一些属性不想被子类访问, 前面提过)

Note 1: Note that only the simple class name is used in the mangled name, so if a subclass chooses both the same class name and attribute name, you can still get name collisions.(如果子类使用相同的类名与属性名, 还是用冲突)

Note 2: Name mangling can make certain uses, such as debugging and \_\_getattr\_\_(), less convenient. However the name mangling algorithm is well documented and easy to perform manually.(name mangle can make certain uses, 如debugging 或通过\_\_getattr\_\_, 这减少了便利性, 但name mangling algorithm 有很好的文档, 易于手动执行)

Note 3: Not everyone likes name mangling. Try to balance the need to avoid accidental name clashes with potential use by advanced callers.(不是所有人都喜欢name mangling. 去平衡可能的命名冲突, 被更高级的调用者造成)

**Public and internal interfaces**

Any backwards compatibility guarantees apply only to public interfaces. Accordingly, it is important that users be able to clearly distinguish between public and internal interfaces.(向后的兼容性保证, 仅针对公有的接口. 据此, 使用者能清晰的分辨公有和内部接口)

Documented interfaces are considered public, unless the documentation explicitly declares them to be provisional or internal interfaces exempt from the usual backwards compatibility guarantees. All undocumented interfaces should be assumed to be internal.(文档中描述的接口都应该是公有的, 除非文档显示的声明了临时或内部接口, 免除其向后兼容的保证, 未在文档中描述的都被假定为内部的使用的)

To better support introspection, modules should explicitly declare the names in their public API using the __all__ attribute. Setting __all__ to an empty list indicates that the module has no public API.(为了更好的)

Even with __all__ set appropriately, internal interfaces (packages, modules, classes, functions, attributes or other names) should still be prefixed with a single leading underscore.

An interface is also considered internal if any containing namespace (package, module or class) is considered internal.

Imported names should always be considered an implementation detail. Other modules must not rely on indirect access to such imported names unless they are an explicitly documented part of the containing module's API, such as os.path or a package's __init__ module that exposes functionality from submodules.

Programming Recommendations
Code should be written in a way that does not disadvantage other implementations of Python (PyPy, Jython, IronPython, Cython, Psyco, and such).

For example, do not rely on CPython's efficient implementation of in-place string concatenation for statements in the form a += b or a = a + b. This optimization is fragile even in CPython (it only works for some types) and isn't present at all in implementations that don't use refcounting. In performance sensitive parts of the library, the ''.join() form should be used instead. This will ensure that concatenation occurs in linear time across various implementations.

Comparisons to singletons like None should always be done with is or is not, never the equality operators.

Also, beware of writing if x when you really mean if x is not None -- e.g. when testing whether a variable or argument that defaults to None was set to some other value. The other value might have a type (such as a container) that could be false in a boolean context!

Use is not operator rather than not ... is. While both expressions are functionally identical, the former is more readable and preferred.

Yes:

if foo is not None:
No:

if not foo is None:
When implementing ordering operations with rich comparisons, it is best to implement all six operations (__eq__, __ne__, __lt__, __le__, __gt__, __ge__) rather than relying on other code to only exercise a particular comparison.

To minimize the effort involved, the functools.total_ordering() decorator provides a tool to generate missing comparison methods.

PEP 207 indicates that reflexivity rules are assumed by Python. Thus, the interpreter may swap y > x with x < y, y >= x with x <= y, and may swap the arguments of x == y and x != y. The sort() and min() operations are guaranteed to use the < operator and the max() function uses the > operator. However, it is best to implement all six operations so that confusion doesn't arise in other contexts.

Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier.

Yes:

def f(x): return 2*x
No:

f = lambda x: 2*x
The first form means that the name of the resulting function object is specifically 'f' instead of the generic '<lambda>'. This is more useful for tracebacks and string representations in general. The use of the assignment statement eliminates the sole benefit a lambda expression can offer over an explicit def statement (i.e. that it can be embedded inside a larger expression)

Derive exceptions from Exception rather than BaseException. Direct inheritance from BaseException is reserved for exceptions where catching them is almost always the wrong thing to do.

Design exception hierarchies based on the distinctions that code catching the exceptions is likely to need, rather than the locations where the exceptions are raised. Aim to answer the question "What went wrong?" programmatically, rather than only stating that "A problem occurred" (see PEP 3151 for an example of this lesson being learned for the builtin exception hierarchy)

Class naming conventions apply here, although you should add the suffix "Error" to your exception classes if the exception is an error. Non-error exceptions that are used for non-local flow control or other forms of signaling need no special suffix.

Use exception chaining appropriately. In Python 3, "raise X from Y" should be used to indicate explicit replacement without losing the original traceback.

When deliberately replacing an inner exception (using "raise X" in Python 2 or "raise X from None" in Python 3.3+), ensure that relevant details are transferred to the new exception (such as preserving the attribute name when converting KeyError to AttributeError, or embedding the text of the original exception in the new exception message).

When raising an exception in Python 2, use raise ValueError('message') instead of the older form raise ValueError, 'message'.

The latter form is not legal Python 3 syntax.

The paren-using form also means that when the exception arguments are long or include string formatting, you don't need to use line continuation characters thanks to the containing parentheses.

When catching exceptions, mention specific exceptions whenever possible instead of using a bare except: clause.

For example, use:

try:
    import platform_specific_module
except ImportError:
    platform_specific_module = None
A bare except: clause will catch SystemExit and KeyboardInterrupt exceptions, making it harder to interrupt a program with Control-C, and can disguise other problems. If you want to catch all exceptions that signal program errors, use except Exception: (bare except is equivalent to except BaseException:).

A good rule of thumb is to limit use of bare 'except' clauses to two cases:

If the exception handler will be printing out or logging the traceback; at least the user will be aware that an error has occurred.
If the code needs to do some cleanup work, but then lets the exception propagate upwards with raise. try...finally can be a better way to handle this case.
When binding caught exceptions to a name, prefer the explicit name binding syntax added in Python 2.6:

try:
    process_data()
except Exception as exc:
    raise DataProcessingFailedError(str(exc))
This is the only syntax supported in Python 3, and avoids the ambiguity problems associated with the older comma-based syntax.

When catching operating system errors, prefer the explicit exception hierarchy introduced in Python 3.3 over introspection of errno values.

Additionally, for all try/except clauses, limit the try clause to the absolute minimum amount of code necessary. Again, this avoids masking bugs.

Yes:

try:
    value = collection[key]
except KeyError:
    return key_not_found(key)
else:
    return handle_value(value)
No:

try:
    # Too broad!
    return handle_value(collection[key])
except KeyError:
    # Will also catch KeyError raised by handle_value()
    return key_not_found(key)
When a resource is local to a particular section of code, use a with statement to ensure it is cleaned up promptly and reliably after use. A try/finally statement is also acceptable.

Context managers should be invoked through separate functions or methods whenever they do something other than acquire and release resources. For example:

Yes:

with conn.begin_transaction():
    do_stuff_in_transaction(conn)
No:

with conn:
    do_stuff_in_transaction(conn)
The latter example doesn't provide any information to indicate that the __enter__ and __exit__ methods are doing something other than closing the connection after a transaction. Being explicit is important in this case.

Be consistent in return statements. Either all return statements in a function should return an expression, or none of them should. If any return statement returns an expression, any return statements where no value is returned should explicitly state this as return None, and an explicit return statement should be present at the end of the function (if reachable).

Yes:

def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)
No:

def foo(x):
    if x >= 0:
        return math.sqrt(x)

def bar(x):
    if x < 0:
        return
    return math.sqrt(x)
Use string methods instead of the string module.

String methods are always much faster and share the same API with unicode strings. Override this rule if backward compatibility with Pythons older than 2.0 is required.

Use ''.startswith() and ''.endswith() instead of string slicing to check for prefixes or suffixes.

startswith() and endswith() are cleaner and less error prone. For example:

Yes: if foo.startswith('bar'):
No:  if foo[:3] == 'bar':
Object type comparisons should always use isinstance() instead of comparing types directly.

Yes: if isinstance(obj, int):

No:  if type(obj) is type(1):
When checking if an object is a string, keep in mind that it might be a unicode string too! In Python 2, str and unicode have a common base class, basestring, so you can do:

if isinstance(obj, basestring):
Note that in Python 3, unicode and basestring no longer exist (there is only str) and a bytes object is no longer a kind of string (it is a sequence of integers instead)

For sequences, (strings, lists, tuples), use the fact that empty sequences are false.

Yes: if not seq:
     if seq:

No: if len(seq):
    if not len(seq):
Don't write string literals that rely on significant trailing whitespace. Such trailing whitespace is visually indistinguishable and some editors (or more recently, reindent.py) will trim them.

Don't compare boolean values to True or False using ==.

Yes:   if greeting:
No:    if greeting == True:
Worse: if greeting is True:
Function Annotations
With the acceptance of PEP 484, the style rules for function annotations are changing.

In order to be forward compatible, function annotations in Python 3 code should preferably use PEP 484 syntax. (There are some formatting recommendations for annotations in the previous section.)

The experimentation with annotation styles that was recommended previously in this PEP is no longer encouraged.

However, outside the stdlib, experiments within the rules of PEP 484 are now encouraged. For example, marking up a large third party library or application with PEP 484 style type annotations, reviewing how easy it was to add those annotations, and observing whether their presence increases code understandability.

The Python standard library should be conservative in adopting such annotations, but their use is allowed for new code and for big refactorings.

For code that wants to make a different use of function annotations it is recommended to put a comment of the form:

# type: ignore
near the top of the file; this tells type checker to ignore all annotations. (More fine-grained ways of disabling complaints from type checkers can be found in PEP 484.)

Like linters, type checkers are optional, separate tools. Python interpreters by default should not issue any messages due to type checking and should not alter their behavior based on annotations.

Users who don't want to use type checkers are free to ignore them. However, it is expected that users of third party library packages may want to run type checkers over those packages. For this purpose PEP 484 recommends the use of stub files: .pyi files that are read by the type checker in preference of the corresponding .py files. Stub files can be distributed with a library, or separately (with the library author's permission) through the typeshed repo [5].

For code that needs to be backwards compatible, type annotations can be added in the form of comments. See the relevant section of PEP 484 [6].

Variable annotations
PEP 526 introduced variable annotations. The style recommendations for them are similar to those on function annotations described above:

Annotations for module level variables, class and instance variables, and local variables should have a single space after the colon.

There should be no space before the colon.

If an assignment has a right hand side, then the equality sign should have exactly one space on both sides.

Yes:

code: int

class Point:
    coords: Tuple[int, int]
    label: str = '<unknown>'
No:

code:int  # No space after colon
code : int  # Space before colon

class Test:
    result: int=0  # No spaces around equality sign
Although the PEP 526 is accepted for Python 3.6, the variable annotation syntax is the preferred syntax for stub files on all versions of Python (see PEP 484 for details).

Footnotes

[7]	Hanging indentation is a type-setting style where all the lines in a paragraph are indented except the first line. In the context of Python, the term is used to describe a style where the opening parenthesis of a parenthesized statement is the last non-whitespace character of the line, with subsequent lines being indented until the closing parenthesis.











### 引用
1. [1 PEP7 Style Guide for c Code, van Rossum](https://www.python.org/dev/peps/pep-0007/)

2. 2 Barry's GUN Mailman style guide [http://barry.warsaw.us/software/STYLEGUIDE.txt](http://barry.warsaw.us/software/STYLEGUIDE.txt)

3. 


**brace**: 大括号(花括号)
**bracket**: 中括号(方括号)
**parenthese**: 小括号(圆括号) 

## 注意

- 个人翻译, 经验能力有限, 难免不准确(一般都附有该段原文), 欢迎指正.

- 图片均来自互联网, 有出处都给出链接, 如有侵犯所有权, 请联系我, 
E-mail: scugjs@gmail.com. 