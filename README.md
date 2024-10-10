# pocwatchdog

[中文版](README_CN.md)

pocwatchdog is a cross-platform Python task scheduler that supports scheduled task execution and email notifications.

## Features

- Easy to use
- Cross-platform support (Windows, Linux, macOS)
- Flexible task scheduling
- Configurable email notifications (success and failure)
- Automatic SMTP server selection
- Detailed error reporting

## Installation

Install pocwatchdog using pip:

```bash
pip install -U pocwatchdog
```

## Usage

1. Import the pocwatchdog module:

```python
import pocwatchdog
```

2. Define your task:

```python
def your_task():
    print("Task is running...")
```

3. Run the task scheduler:

```python:path/to/main.py
pocwatchdog.run(
    job=your_task, 
    schedule_time="08:00",
    sender=None,  # Default is not to send
    password=None,  # Default is not to send
    recipients=[],  # Default is not to send
    smtp_server='smtp.exmail.qq.com',  # Default is auto-select
    smtp_port=465,  # Default is auto-select
    smtp_ssl=True,  # Default is auto-select
    success_subject="success",  # Default value
    success_body="success",  # Default value
    failure_subject="failure",  # Default value
    failure_body="task failure: error_message",  # Default value
    notify_success=True,  # Default value
    notify_failure=True  # Default value
)
```

- `schedule_time`: Execution time

If it's a number, the default unit is seconds, and the task will be executed every `schedule_time` seconds. For example, `120` means execute every 2 minutes.

If it's a string, it's treated as a time point in the format `HH:MM`. For example, `08:00` means execute once a day at this time.

If it's a list, it's treated as multiple time points. For example, `["08:00", "12:00", "16:00"]` means execute once a day at these times.

If it's a dictionary, the keys are interpreted as follows:

If the key is a number, it's treated as a date, and the corresponding value follows the above number, string, or list interpretation.

If the key is a string, it's treated as a day of the week (e.g., for Monday, supported formats include: `1`, `monday`, `Monday`, `MONDAY`, `mon`, `mon.`, `m`, and so on), and the corresponding value follows the above number, string, or list interpretation.

For example, the following schedule executes at 8:00 on the 1st, at 8:00, 12:00, and 16:00 on the 2nd, every hour on the 3rd, and at 8:00 every Monday:

```python:path/to/main.py
schedule_time = {
    1: "08:00",
    2: ["08:00", "12:00", "16:00"],
    3: 216000,
    "1": "08:00",
}
```

- `sender`: Sender's email address. If you don't want to send emails, you can leave it unconfigured.
- `password`: Sender's email password. If you don't want to send emails, you can leave it unconfigured.
- `recipients`: List of recipient email addresses. If you don't want to send emails, you can leave it unconfigured.
- `smtp_server`: SMTP server address. Default value is auto-select.
- `smtp_port`: SMTP server port. Default value is auto-select.
- `smtp_ssl`: Whether to use SSL. Default value is auto-select.
- `success_subject`: Email subject for successful tasks. Default value provided.
- `success_body`: Email content for successful tasks. Default value provided.
- `failure_subject`: Email subject for failed tasks. Default value provided.
- `failure_body`: Email content for failed tasks. The error message will replace `error_message`. Default value provided.
- `notify_success`: Whether to send notifications for successful tasks (True/False). If `sender`, `password`, and `recipients` are empty, an exception will be raised.
- `notify_failure`: Whether to send notifications for failed tasks (True/False). If `sender`, `password`, and `recipients` are empty, an exception will be raised.

```python:path/to/main.py
import pocwatchdog

def your_task():
    print("Task is running...")

pocwatchdog.run(
    job=your_task, 
    schedule_time="08:00",
    sender='your_email@example.com',
    password='your_password',
    recipients=['recipient1@example.com', 'recipient2@example.com'],
    smtp_server='smtp.exmail.qq.com',
    smtp_port=465,
    smtp_ssl=True,
    success_subject="Task Successful",
    success_body="The task has been executed successfully.",
    failure_subject="Task Failed",
    failure_body="Task execution failed. Error message: error_message",
    notify_success=True,
    notify_failure=True
)
```

## Testing

Run the test cases:

```bash
python -m unittest tests/test_pocwatchdog.py
```