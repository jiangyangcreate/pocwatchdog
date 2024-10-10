# pocwatchdog

[English](README.md)

pocwatchdog 是一个跨平台的 Python 任务调度器，支持定时执行任务并通过邮件发送通知。

## 特性

- 简单易用
- 跨平台支持 (Windows, Linux, macOS)
- 灵活的任务调度
- 可配置的邮件通知 (成功和失败)
- 自动 SMTP 服务器选择
- 详细的错误报告

## 安装

使用 pip 安装 pocwatchdog:

```bash
pip install pocwatchdog
```

## 使用

1. 导入 pocwatchdog 模块:

```python
import pocwatchdog
```

2. 定义您的任务:

```python
def your_task():
    print("任务执行中...")
```

3. 运行任务调度器:

```python:path/to/main.py
pocwatchdog.run(
    job=your_task, 
    schedule_time="08:00",
    sender=None,  # 缺省则不发送
    password=None,  # 缺省则不发送
    recipients=[],  # 缺省则不发送
    smtp_server='smtp.exmail.qq.com',  # 缺省值则自动选择
    smtp_port=465,  # 缺省值则自动选择
    smtp_ssl=True,  # 缺省值则自动选择
    success_subject="success",  # 缺省默认值
    success_body="success",  # 缺省默认值
    failure_subject="failure",  # 缺省默认值
    failure_body="task failure: error_message",  # 缺省默认值
    notify_success=True,  # 缺省默认值
    notify_failure=True  # 缺省默认值
)
```

- `schedule_time`: 执行时间

如果是数字则默认单位是秒，每间隔`schedule_time`秒执行一次，例如`120`，则每2分钟执行一次。

如果是字符串则默认是时间点，请遵从`HH:MM`的格式，例如`08:00`，每天在这个时间点执行一次。

如果是列表，则默认是多个时间点，例如`["08:00", "12:00", "16:00"]`，每天在这些时间点执行一次。

如果传入的是字典，则解析字典的键：

如果字典的键为数字，则默认是日期，对应字典的值遵从上方数字、字符串、列表的判断。

如果字典的键为字符串，则默认是星期几（以周一为例，支持的写法包括：`1`、`monday`、`Monday`、`MONDAY`、`mon`、`mon.`、`m`，以此类推），对应字典的值遵从上方数字、字符串、列表的判断。

例如下面是1号的8点、2号的8点、12点、16点、3号每隔一个小时执行一次、每周一的8点执行一次。

```python:path/to/main.py
schedule_time = {
    1: "08:00",
    2: ["08:00", "12:00", "16:00"],
    3: 216000,
    "1": "08:00",
}
```

- `sender`: 发件人邮箱，如果不想发送邮件，则可以不配置。
- `password`: 发件人邮箱密码，如果不想发送邮件，则可以不配置。
- `recipients`: 收件人邮箱列表，如果不想发送邮件，则可以不配置。
- `smtp_server`: SMTP服务器地址，缺省值则自动选择。
- `smtp_port`: SMTP服务器端口，缺省值则自动选择。
- `smtp_ssl`: 是否使用SSL，缺省值则自动选择。
- `success_subject`: 任务成功时的邮件主题，缺省默认值。
- `success_body`: 任务成功时的邮件内容，缺省默认值。
- `failure_subject`: 任务失败时的邮件主题，缺省默认值。
- `failure_body`: 任务失败时的邮件内容，错误信息将替换`error_message`，缺省默认值。
- `notify_success`: 任务成功时是否发送通知（True/False），如果`sender`、`password`、`recipients`为空，则抛出异常。
- `notify_failure`: 任务失败时是否发送通知（True/False），如果`sender`、`password`、`recipients`为空，则抛出异常。

```python:path/to/main.py
import pocwatchdog

def your_task():
    print("任务执行中...")

pocwatchdog.run(
    job=your_task, 
    schedule_time="08:00",
    sender='your_email@example.com',
    password='your_password',
    recipients=['recipient1@example.com', 'recipient2@example.com'],
    smtp_server='smtp.exmail.qq.com',
    smtp_port=465,
    smtp_ssl=True,
    success_subject="任务成功",
    success_body="任务已成功执行。",
    failure_subject="任务失败",
    failure_body="任务执行失败，错误信息：error_message",
    notify_success=True,
    notify_failure=True
)
```

## 测试

运行测试用例：

```bash
python -m unittest tests/test_pocwatchdog.py
```