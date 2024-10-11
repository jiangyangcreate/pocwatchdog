import unittest
from src.pocwatchdog.task_scheduler import run

class TestPocWatchdog(unittest.TestCase):
    def test_run_without_notifications(self):
        def sample_task():
            return "任务执行成功"

        try:
            run(
                job=sample_task,
                schedule_time=1,  # 每秒执行一次
                notify_success=False,
                notify_failure=False
            )
        except Exception as e:
            self.fail(f"run raised an exception {e}")

    def test_send_email_failure_without_credentials(self):
        def sample_task():
            raise Exception("测试异常")

        with self.assertRaises(ValueError):
            run(
                job=sample_task,
                schedule_time=1,
                notify_failure=True
            )

if __name__ == '__main__':
    unittest.main()
