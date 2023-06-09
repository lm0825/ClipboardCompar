# Clipboard Diff Tool

该项目是一个剪贴板差异比较工具，它可以将剪贴板的历史内容进行比较，并生成差异页面来展示不同之处。

## 效果图

![image-20230531165110191](C:\Users\liuming\AppData\Roaming\Typora\typora-user-images\image-20230531165110191.png)

## 依赖

- `pyperclip`：用于获取剪贴板内容
- `difflib`：用于生成差异页面
- `webbrowser`：用于在默认浏览器中打开差异页面

确保在运行之前安装了上述依赖项。您可以使用以下命令安装依赖：

```
pip install pyperclip
```

## 如何使用

1. 运行脚本 `clipboard_diff.py`。
2. 脚本将监视剪贴板的内容，并将最近三次（两次）的剪贴板内容保存为历史记录。
3. 当检测到剪贴板内容发生变化时，脚本将生成差异页面并在默认浏览器中打开。
4. 差异页面将展示最近两次剪贴板内容之间的差异，以便进行比较。
5. 关闭差异页面后，脚本将退出。

## 自定义设置

- 差异页面的样式可以在 `compare_strings()` 函数中进行自定义修改。您可以根据需要更改表格样式、颜色等。
- 默认情况下，差异页面将保存为 `diff.html` 文件。如果需要更改保存路径和文件名，可以在 `compare_strings()` 函数中修改。

## 注意事项

- 由于该项目使用了默认浏览器来显示差异页面，确保您的系统已经设置了默认浏览器，并且浏览器能够正常打开HTML文件。
- 请注意，在使用剪贴板时，可能会包含敏感信息。确保在安全的环境中使用此工具，以免泄露敏感数据。
- 本项目仅作为示例提供，如果需要更复杂的差异比较功能或其他定制需求，建议使用专业的差异比较工具或库。