# 说明
打包之前替换本地项目中的strings文件可以按以下方式执行脚本。这里的脚本是基于python3的，因此在执行之前请确保本地有python3的环境。
## 用法：
1. 首先执行**python_requests.py**脚本，这个脚本主要负责拉取多语言后台的多语言文件，并保存到本地指定的路径下。 <br>
    具体执行方法：
    ```
    python3 ./python_requests.py ~/Desktop/waka_language debug
    ```
    这里的`~/Desktop/waka_language`是指定的存放下载文件的路径，debug表示下载的环境。
1. 然后执行**waka_replace.py**脚本，这个脚本是负责替换本地的各个语言环境中的strings文件，在替换的过程中会过滤掉一些非法的key。<br>
    具体执行方法：
    ```
    python3 ./waka_replace.py /Documents/workspace/wakaandroidstudio/wakaAndroid/src/ain/res /Desktop/waka_language
    ```
    其中`~/Documents/workspace/wakaandroidstudio/wakaAndroid/src/main/res`表示本地项目的res文件夹路径，
    `~/Desktop/waka_language`是之前定义的存放下载文件的路径。
## 问题：
1. 关于os模块（脚本中用到的功能主要是在一个脚本中调用另一个脚本）
1. 关于sys模块（脚本中用到的功能主要是获取从命令行中输入的参数）
1. open文件时的几个参数说明
1. writelines和write区别
1. python中的三元表达式（`url = release_url if sys.argv[2] == 'release' else alpha_url`）
1. requests库简单使用
## os模块：
> Python os 模块提供了一个统一的操作系统接口函数, 这些接口函数通常是平台指定的，os 模块能在不同操作系统平台（如 nt 或 posix）中的特定函数间自动切换,从而能实现跨平台操作。

### os模块中的常用函数
* `os.getcwd()`：获取当前工作目录，相当于执行`pwd`命令
* `os.chdir("dirname")`：改变当前脚本的工作目录，相当于执行`cd`命令
* `os.name`：获取当前使用的操作系统（其中 ‘nt’ 是windows，’posix’ 是 linux 或者 unix）
* `os.environ`：获取系统环境变量
* `os.makedirs('dirname1/dirname2')`：可生成多层递归目录，父目录如果不存在，递归生成
* `os.removedirs('dirname1')`：若目录为空，则删除，并递归到上级目录，若也为空，则删除，依此类推
* `os.mkdir('dirname')`：生成单级目录，相当于执行`mkdir dirname`命令
* `os.rmdir('dirname')`：删除单级空目录，若目录不为空则无法删除，会报错；相当于执行`rmdir dirname`命令
* `os.listdir('dirname')`：列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表形式打印
* `os.remove()`：删除一个文件
* `os.rename("oldname", "newname")`：重命名文件/目录
* `os.popen('bash command')`：运行shell命令，生成对象，可赋给变量，再用read读取
## sys模块：
> sys 模块包含了与 Python 解释器和它的环境有关的函数。使用sys模块可以获得脚本的参数、处理模块、操作模块搜索路径、查找内建模块、查找已导入的模块等
### sys模块中的常用函数
* `sys.argv`：实现从程序外部向程序传递参数`sys.argv`变量是一个包含了命令行参数的字符串列表, 利用命令行向程序传递参数. 其中,脚本的名称总是`sys.argv`列表的第一个参数。
* `sys.path`：包含输入模块的目录名列表  
获取指定模块搜索路径的字符串集合，可以将写好的模块放在得到的某个路径下，就可以在程序中import时正确找到。 
`sys.path.append(“自定义模块路径”)`
* ` sys.exit([arg])`：程序中间的退出, arg=0为正常退出   
一般情况下执行到主程序末尾，解释器自动退出，但是如果需要中途退出程序，可以调用`sys.exit`函数，带有一个可选的整数参数返回给调用它的程序，表示你可以在主程序中捕获对`sys.exit`的调用。（0是正常退出，其他为异常）当然也可以用字符串参数，表示错误不成功的报错信息。
* `sys.modules`：`sys.modules`是一个全局字典，该字典是python启动后就加载在内存中。每当程序员导入新的模块，`sys.modules`将自动记录该模块。当第二次再导入该模块时，python会直接到字典中查找，从而加快了程序运行的速度。它拥有字典所拥有的一切方法.
* `sys.getdefaultencoding()` ：获取系统当前编码，在python3以下的版本一般默认为ascii，python3则默认为utf-8。 
* `sys.setdefaultencoding()` ：设置系统默认编码，执行dir（sys）时不会看到这个方法，在解释器中执行不通过，可以先执行reload(sys)，在执行 `setdefaultencoding(‘utf8’)`，此时将系统默认编码设置为utf8。 
* `sys.getfilesystemencoding()` ：获取文件系统使用编码方式，Windows下返回’mbcs’，mac下返回’utf-8’
* ` sys.stdin, sys.stdout, sys.stderr `：stdin , stdout , 以及stderr 变量包含与标准I/O 流对应的流对象. 如果需要更好地控制输出,而print 不能满足你的要求, 它们就是你所需要的. 你也可以替换它们, 这时候你就可以重定向输出和输入到其它设备( device ), 或者以非标准的方式处理它们
* `sys.platform`：获取当前系统平台. 如：win32、Linux等。
## open()函数：
> `open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`：在使用该函数的时候，除了file参数必填外，其他参数可以选用。
### 参数说明
* file：文件名称
* mode：文件的打开方式，函数提供了一些可选的打开方式，其中默认方式为‘rt’   
*‘r’*  ：open for reading (default)——只读，默认方式  
*‘w’*  ：open for writing, truncating the file first——写入，会覆盖源文件内容  
*‘x’*  ：create a new file and open it for writing——创建新文件，并写入内容，如果文件已存在，将会报错：FileExistsError  
*‘a’*  ：open for writing, appending to the end of the file if it exists——写入，如果文件有内容，则在末尾追加写入  
*‘b’*  ：binary mode——二进制模式  
*‘t’*  ：text mode (default)——文本模式  
*‘+’*  ：open a disk file for updating (reading and writing)——更新磁盘文件，读写     
*'U'*   ：universal newline mode (deprecated)——在paython3中已经弃用
* buffering：用于设置缓存策略   
在二进制模式下，使用0来切换缓冲；在文本模式下，通过1表示行缓冲（固定大小的缓冲区）。
在不给参数的时候，二进制文件的缓冲区大小由底层设备决定，可以通过io.DEFAULT_BUFFER_SIZE获取，通常为4096或8192字节，文本文件则采用行缓冲。
* encoding：编码或者解码方式。默认编码方式依赖平台，如果需要特殊设置，可以参考codecs模块，获取编码列表。
* errors：可选，并且不能用于二进制模式，指定了编码错误的处理方式，可以通过codecs.Codec获得编码错误字符串
* newline：换行控制，参数有：None，'\n'，'\r'，'\r\n'。
输入时，如果参数为None，那么行结束的标志可以是：'\n'，'\r'，'\r\n'任意一个，并且三个控制符都首先会被转化为：'\n'，然后才会被调用；
如果参数为''，所有的通用的换行结束标志都可以用，但是行结束标识符返回调用不会被编码。
输出时，如果参数为None，那么行结束的标志可以是：'\n'被转换为系统默认的分隔符；如果是''，'\n'则不会被编码。
* closefd：false：文件关闭时，底层文件描述符仍然为打开状态，这是不被允许的，所以，需要设置为ture
* opener：可以通过调用*opener*方式，使用自定义的开启器。底层文件描述符是通过调用*opener*或者*file*, *flags*获得的。
*opener*必须返回一个打开的文件描述。将os.open作为*opener*的结果，在功能上，类似于通过None。
## write()和writelines()：
- `file.write(str)`：方法用于向文件中写入指定字符串。在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。如果文件打开模式带 b，那写入文件内容时，str (参数)要用 encode 方法转为 bytes 形式，否则报错：TypeError: a bytes-like object is required, not 'str'。
- `file.writelines(sequence)`：方法用于向文件中写入一序列的字符串。这一序列字符串可以是由迭代对象产生的，如一个字符串列表。换行需要制定换行符 \n。
## python中的三元表达式：
> python中的三目运算符不像其他语言,其他的一般都是
`condition ? condition_is_true : condition_is_false`，但是在python中写法是这样：
`condition_is_true if condition else condition_is_false`   
它允许用简单的一行快速判断，而不是使用复杂的多行if语句。 这在大多数时候非常有用，而且可以使代码简单可维护。还有一个用法比较少见，它使用了元组：
#### 伪代码
```python
#(返回假，返回真)[真或假]
(if_test_is_false, if_test_is_true)[test]
```
#### 例子
```python
fat = True
fitness = ("skinny", "fat")[fat]
print("Ali is", fitness)
#输出: Ali is fat
```
## requests库：
> Python内置的urllib模块，用于访问网络资源。但是，它用起来比较麻烦，而且，缺少很多实用的高级功能。更好的方案是使用requests。它是一个Python第三方库，处理URL资源特别方便。

requests库不是python自带的，因此使用这个库需要安装.[使用详情](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)
### 安装requests
```
$ pip install requests
```
### 发送请求
首先需要*import*导入这个库，然后我们可以尝试来发送请求获取Github的公共时间线：
```
>>> r = requests.get('https://api.github.com/events')
```
这时我们已经有了一个Response对象，我们可以从这里拿到我们要的信息
```
>>> r.text
>>> r.status_code
# 200
```
那么其他 HTTP 请求类型：PUT，DELETE，HEAD 以及 OPTIONS 又是如何的呢？都是一样的简单：
```
>>> r = requests.post('http://httpbin.org/post', data = {'key':'value'})
>>> r = requests.put('http://httpbin.org/put', data = {'key':'value'})
>>> r = requests.delete('http://httpbin.org/delete')
>>> r = requests.head('http://httpbin.org/get')
>>> r = requests.options('http://httpbin.org/get')
```
### 传递url参数
Requests 允许你使用 params 关键字参数，以一个字符串字典来提供这些参数。举例来说，如果你想传递 key1=value1 和 key2=value2 到 httpbin.org/get ，那么你可以使用如下代码：
```
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get("http://httpbin.org/get", params=payload)
>>> print(r.url)
```
注意字典里值为 None 的键都不会被添加到 URL 的查询字符串里。你还可以将一个列表作为值传入：
```
>>> payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

>>> r = requests.get('http://httpbin.org/get', params=payload)
>>> print(r.url)
http://httpbin.org/get?key1=value1&key2=value2&key2=value3
```
### 响应内容
我们能读取服务器响应的内容。再次以 GitHub 时间线为例：
```
>>> import requests
>>> r = requests.get('https://api.github.com/events')
>>> r.text
u'[{"repository":{"open_issues":0,"url":"https://github.com/...
```
Requests 会自动解码来自服务器的内容。大多数 unicode 字符集都能被无缝地解码。

请求发出后，Requests 会基于 HTTP 头部对响应的编码作出有根据的推测。当你访问 r.text 之时，Requests 会使用其推测的文本编码。你可以找出 Requests 使用了什么编码，并且能够使用 r.encoding 属性来改变它：
```
>>> r.encoding
'utf-8'
>>> r.encoding = 'ISO-8859-1'
```
如果你改变了编码，每当你访问 r.text ，Request 都将会使用 r.encoding 的新值。你可能希望在使用特殊逻辑计算出文本的编码的情况下来修改编码。比如 HTTP 和 XML 自身可以指定编码。这样的话，你应该使用 r.content 来找到编码，然后设置 r.encoding 为相应的编码。这样就能使用正确的编码解析 r.text 了。

