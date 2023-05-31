import pyperclip
import time
import webbrowser
import difflib

def get_clipboard_history():
    clipboard_history = []
    clipboard_history.append(pyperclip.paste())
    while True:
        time.sleep(1)
        print('waitting...')
        current_value = pyperclip.paste()
        if current_value != clipboard_history[-1]:
            print(current_value)
            clipboard_history.append(current_value)
        if len(clipboard_history) > 3:
            clipboard_history.pop(0)
        if len(clipboard_history) == 3:
            break
    return clipboard_history


def compare_strings(str1, str2):
    d = difflib.HtmlDiff()

    # 生成HTML差异页面
    diff = d.make_file(str1.splitlines(), str2.splitlines())

    # 添加CSS样式
    styled_diff = """
    <style>
    body {
        font-family: “Microsoft YaHei”, sans-serif;
        margin: 20px;
    }

    table {
        width: 100%;
        border-collapse: collapse;
    }

    th, td {
        padding: 8px;
        border: 1px solid #ddd;
        border: 1px solid #ddd;
        white-space: pre-wrap; /* 保留换行符 */
    }

    .diff_header {
        background-color: #00000;
        background-color: #00000;
        background-color: #00000;
        font-weight: bold;
    }

    .diff_next {
        background-color: #c0c0c0;
        font-weight: bold;
    }

    .diff_add {
        background-color: #ddffdd;
    }

    .diff_chg {
        background-color: #ffffcc;
    }

    .diff_sub {
        background-color: #ffdddd;
    }
    </style>
    """ + diff

    # 将美化后的差异页面保存到HTML文件
    with open('diff.html', 'w', encoding='utf-8') as f:
        f.write(styled_diff)

    # 在默认浏览器中打开差异页面
    webbrowser.open('diff.html')


if __name__ == '__main__':
    # Read the last two clipboard contents
    clipboard_history = get_clipboard_history()
    clipboard_content = clipboard_history[1]
    clipboard_content2 = clipboard_history[2]
    compare_strings(clipboard_content, clipboard_content2)
