# 如何编辑 Python 代码

> Declare: this article is translated from [How To Edit Python Code @python.org](https://wiki.python.org/moin/HowToEditPythonCode)
> 
> License: GPL licensed

---

## 发展起源

十九世纪八十年代末，在阿姆斯特丹的工人国际委员会上，Guido van Rossum 提出了 Python 的构想并着手加以实现。Python 继承自 ABC 编程语言(SETL)，具备处理异常的能力以及与 Amoeba OS 交互的接口。Van Rossum 是 Python 的主要创始人，在决定 Python 发展方向上一直扮演着重要的角色——“仁慈的独裁者”——通过社区对他的称呼，我们可以看出这一点。

---

## 编程哲学

Python 是一种多重范式(multi-paradigm)的编程语言。Python 支持面向对象编程(OOP)和结构化程序设计，同时也能满足函数式程序设计和面向切面编程(AOP)的需求，程序员不需要采用特定的编程风格。许多其他范式则是使用相应的扩展来实现功能，比如 pyDBC，Contract for Python。

Python 的设计初衷是高度可扩展性，而非将所有的功能都添加到内核中。新的内置模块可以由 C/C++ 或者 Cython 实现。Python 也可以用作现有应用模块的扩展，以此实现可编程接口。出于这种想法，以及无法继续忍受使用 ABC 语言的原因，Van Rossum 一开始就打算设计一个具有轻量内核，自带庞大标准库，并且易于扩展的解释程序。

---

## 命名风格

Python 开发的一个重要目标是让 Python 的使用充满乐趣。这一点可以从 Python 名称的由来(Monty Python's Flying Circus)看出来，因此在示例代码，部分趣味教程和参考资料中，开发者通常习惯使用 Monty Python 来指代 Python。再比如，Python 经常会使用 spam 和 eggs 作为变量名，而非传统的 foo 和 bar。

---

## 常见用途

Python 通常被用作网络应用的脚本语言，比如 Apache 的 mod_wsgi。借助网络服务器的网关接口，由 Python 封装的标准接口可以使应用开发更加快捷。诸如 Diango，Pylons，TurboGears，web2py，Flask 以及 Zope 这些框架可以帮助开发者设计维护复杂的网络应用。借助 NumPy，SciPy 以及 Matplotlib 这些三方库，Python 也能用于科学计算的领域。

---

## 语法和语义

Python 的另一个设计初衷就是高度可读性。Python 拥有整洁的代码布局，习惯使用关键词替代标点符号。相比于传统的强类型结构化语言 C 或者 Pascal，Python 使用更少的引用，语法异常和特例。关于 2.x 和 3.x 之间的区别，可以浏览 *History of Python* 获取详情。

### 缩进

Python 使用空格缩进来划分代码块，而非成对的大括号或者关键词(off-side rule)。通常在特定的声明语句后面增加缩进，而在当前代码块末尾减少缩进。

### 语句

- condition
    ```python
    if condition_1: 
        ...
    elif condition_2: 
        ...
    else: 
        ...
    ```

- for loop
    ```python
    for condition : 
        ...
    ```

- while loop
    ```python
    while condition : 
        ...
    ```

- exception
    ```python
    try: 
        ...
    except: 
        ...
    ```

除了这些，`class, def, with, pass, assert, yield` 也是常用的声明和控制语句。

### 表达式

- 在 Python 2，/ 操作符可以实现 int 值的整除操作，将运算结果截取为整数值。浮点型和整型相除，则是将其中一个整数转化为浮点数再计算结果(eg: float(x) / y)。在 Python 3 中，/ 操作符的结果为浮点数，同时引入了 // 操作符实现整除，在 Python 2.2+ 中添加 `from __future__ import division` 语句后可以使用该操作。

- 不同于 Java 使用 == 操作符比较引用，使用 equal() 比较两者的值；Python 分别使用 == 和 is 比较值和引用。

- 不同于 C 的逻辑操作符 &&，||，!；Python 使用 and，or，not 表示与或非。

- Python 使用叫做 "list comprehension" 的表达式，2.4 版本将其扩展为一般表达式 "generator expression" 。

- Python 使用 lamda 表达式实现匿名函数，但局限在于只能只用单句表达式。

- 不同于其他语言使用 x ? y : z 实现条件运算，Python 通常写作 x if c else y 。

- Python 中列表和数组的写法也不一样，列表一般写作 [1, 2, 3]，数组则是 (1, 2, 3) 。

- Python 2 使用“字符格式”操作符 %，类似于 C 语言的格式化输出。比如，"foo=%s bar=%d" % ("blah", 2) 等价于 "foo=blah bar=2"。在 Python 3 中，这一用法被 str 类的 format() 方法替代，示例："foo={0} bar={1}".format("blah", 2) 。

- Python 还有多种字符串表达式：

    - 使用单引号或双引号定义字符串的内容，不同于 Unix shells, Perl 以及受 Perl 影响的语言, 单引号和双引号起到类似的作用。两种字符串都可以使用反斜杠 (\\) 定义转义字符，并且不存在类似 "$foo" 的隐式字符串。

    - 形如 """string""" 或者 '''string''' 的三重引用字符串则会在 shells，Perl，Ruby 中以当前文档格式输出内容。

### 对象方法

和其他 OOP 语言一样，方法其实就是指对象所属类的函数，在实际代码中通常表现为 `object.method(argument)`，它的一般形式是 `Class.method(instance, argument)`。相比其他 OOP 语言(比如 Java, C++ or Ruby)，Python 中的函数需要明确定义自变量(形参)，借此来访问实际数据(实参)。

### 变量类型

Python 使用动态类型(duck typing)，这意味着它具有类型化的对象而非类型化的变量名。虽然在编译的时候不会检查变量类型，但是某些操作也会导致报错，这表明对象的类型可能存在问题。尽管 Python 具有动态类型的特点，但也是一门强类型的语言，禁止使用没有明确定义的操作(比如，将 number 赋值给 string)。

### 数学运算

Python 定义了取模运算符，计算之后 a % b 的结果会落在 [0, b) 区间内，这是 b > 0 的情况，相应地当 b < 0 时，结果则是落在区间 (b, 0] 。这种处理方式会影响整除运算的定义，为了保证等式 b * (a//b) + a % b == a 的有效性，整除的结果需要四舍五入到负无穷(round towards minus infinity，即调整运算结果为最接近并且不大于结果的值)。因此 7//3 = 2，而 (-7)//3 = -3，这和其他编程语言通常习惯四舍五入到零不同， Python 的取模运算在这种逻辑下则会返回负值。

---

## 实现的组件

*(这一小节内容理解困难，暂不转译)*

---

## 开发指南

Python 的开发主要是通过 “Python 优化计划”(Python Enhancement Proposal) 进行管理。PEPS 是一个提供 Python 相关信息的标准化设计文档，包括建议，描述，设计理念以及其他语言的说明。其中比较重要的计划会经由 Van Rossum 评审制订。CPython 的开发者也会通过邮件来沟通，或者通过论坛在线交流，比如 python-dev 主要是探讨 Python 未来的发展，python.org 讨论的是关于 Bug 的细节问题，hg.python.org 则是开发相关的话题。

CPython 的公开发行版大致分为三种( 非向后兼容的版本，先行版本，稳定版本 )，我们可以通过版本号进行区分。在发布最终版之前，也会放出一些 alpha，beta 版本，用于测试预览。尽管针对每个版本都安排了发布时间，但是如果代码尚未完善，我们也会推迟原定计划。在开发过程中，团队会进行大量的单元测试，使用 BuildBot 持续集成系统来监控代码的状态。

---

## 标准库

Python 拥有庞大的标准库，预先实现了用于任务处理的工具，就像是“内置电池”，这通常被认为是 Python 最棒的地方之一。(对于开发者而言，)可以使用 C/Python 实现自定义组件，借此增强标准库的模块，比如 Boost C++ Library 可以让我们同时使用 C++ 和 Python 进行开发。得益于标准库提供的种类庞大的工具，Python 获得了使用其他低级语言(C/C++)的能力，恰好这些语言已经实现了操作其他三方库的接口，因此 Python 可以作为一种连接语言和工具的强效粘合剂。

基于标准格式和协议，我们可以使用标准库来实现外部网际网路应用。除此以外，标准库还包含其他模块，可以实现诸如创建图形用户接口(GUI)，访问关系型数据库，计算任意精度小数，使用正则表达式以及执行单元测试等功能。

部分标准库是依据设计文档实现的(比如，WSGI 依据 PEP 333 实现的 wsgiref )，但是多数模块是根据自身代码，内部文档以及测试套件进行设计的。尽管如此，由于大部分标准库代码具有跨平台的特点，所以只有少数的模块需要进行改动或者重写。

---

## 产生的影响

面世多年，Python 的设计哲学已经对其他编程语言有所影响，包括：

- Pyrex 和其派生的 CPython 作为译码器，可以实现用于 CPython 解释器的高性能 C 扩展程序。Pyrex 基本就是支持 C/C++ 特性语法扩展的 Python 语言。两者都能输出兼容 C 的代码。

- Boo 使用缩进，相似的语法结构和对象模型。但 Boo 使用的是静态类型并且集成于 .NET 框架。

- Cobra 同样使用缩进和相似的语法结构，并在致谢文档中将 Python 列为对其影响最大的语言。但是，Cobra 本身就具备了契约式设计，单元测试以及静态类型等特性。

- \ 语言借鉴了 Python 的迭代器，生成器和列表解析等特性。

- Go 语言则是结合了使用动态语言(Python)开发的便捷性。

- Groovy 是出于将 Python 编程哲学带入 Java 的初衷而设计的。

- Ocaml 受 Python 和 Haskell 影响，语法结构也比较随意。

---

## 参考文档

[[1]: The Wiki Pages For Python @wiki.python](https://wiki.python.org/moin/FrontPage)

[[2]: Google Python Style Guide @google.official](https://google.github.io/styleguide/pyguide.html)

---

*HowToEditPythonCode(last edited 2020-01-10 11:20 by palepriest)*