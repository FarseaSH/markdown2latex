# Markdown转换Latex的辅助Python脚本

学术文章通常使用Latex进行最后的渲染，但是直接利用Latex语言进行写作并不方便，各种命令细节（例如，命令的花括号的输入）常会打断书写的思路；此外，较为笨重的渲染引擎也很难做到“所见即所得”的写作模式，给文本（尤其是数学公式）修改带来了一定不便；相对的，Markdown作为一种“轻量级”的修饰语言，简单的修饰符，加上完备的工具生态，码字的体验更为流畅。自己读书期间进行学术写作时候，采用了先Markdown写作，再进行Latex转换的步骤。这其中的Markdown到Latex的转换可以利用Pandoc(https://pandoc.org/index.html)进行。但转换后的Latex会有很多附带的不必要的代码，尝试几种方案后，我发现利用正则表达式处理这些不必要的代码是最为直接有效的方法。本文将相关脚本代码以及简单使用说明贴出。

## 文件说明

代码文件整个结构如下：

```
./
├─ src/
│  ├─ YOUR_MD_FILE1.md
│  ├─ YOUR_MD_FILE2.md
│  ├─ folder_inside/
│     ├─ YOUR_MD_FILE3.md
├─ template.latex
├─ md2latex.py
```

其中

- `src`下存放Markdown文件原稿，原稿可以放在二级（或者任意级）目录下 ，只要文件在`src`下且以`.md`结尾，都会被转换
- `template.latex` 是模版文件，用于指定转换后latex文件形式；你可以在这里指定转换后latex的preamble部分，例如导入相关包的，后面使用说明部分
- `md2latex.py` 文件是markdown 转换 latex的主要脚本，运行其便可开始进行转换。

## 使用说明

### 环境安装

脚本运行需要安装Pandoc，具体安装方法参见 Pandoc - Installing  pandoc - https://pandoc.org/installing.html

### 修改template

根据自身需要修改template.latex文件，可以在这里加入相关导入的包，调整文本相关的格式。模版文件中的`$body$`，会被替换为Markdown文本对应的Latex文本。

例如，下面的模版代码，为每个转换后的Latex文件，在preamble部分添加命令，载入amsfonts数学符号包、hyperref文本链接辅助包，并且在正文前添加目录。

```
\\documentclass{ctexart}

\\usepackage{amsfonts}
\\usepackage{hyperref}

\\begin{document}

\\tableofcontents

$body$

\\end{document}
```

### 进行转换

将所需要转换的Markdown文件放入`src`目录下，运行`md2latex.py`脚本可以完成对应转换，所有对应生成的Latex文件都默认放在output文件夹下。

