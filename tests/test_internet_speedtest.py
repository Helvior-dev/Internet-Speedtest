"""Offline tests for speed test output and spinner cleanup."""

import io
import unittest
from contextlib import redirect_stdout
from types import SimpleNamespace
from unittest.mock import patch

import internet_speedtest


class SpeedTestTests(unittest.TestCase):
    def test_speed_test_reports_measured_values_without_network(self):
        fake_speedtest = SimpleNamespace(
            results=SimpleNamespace(ping=12.567),
            get_best_server=lambda: None,
            download=lambda: 154_250_000,
            upload=lambda: 92_400_000,
        )
        output = io.StringIO()
        with patch("internet_speedtest.speedtest.Speedtest", return_value=fake_speedtest), \
             patch("internet_speedtest.run_with_spinner", side_effect=lambda _name, task: task()), \
             redirect_stdout(output):
            internet_speedtest.speed_test()

        self.assertIn("Download Speed : 154.25 Mbps", output.getvalue())
        self.assertIn("Upload Speed   : 92.4 Mbps", output.getvalue())
        self.assertIn("Ping           : 12.57 ms", output.getvalue())

    def test_speed_test_reports_initialization_errors(self):
        output = io.StringIO()
        with patch("internet_speedtest.speedtest.Speedtest", side_effect=OSError("offline")), \
             redirect_stdout(output):
            internet_speedtest.speed_test()

        self.assertIn("Error during speed test: offline", output.getvalue())

    def test_spinner_stops_and_joins_when_task_fails(self):
        captured = {}

        class FakeThread:
            def __init__(self, target, args):
                self.target = target
                self.args = args

            def start(self):
                captured["event"] = self.args[1]

            def join(self):
                captured["joined"] = True

        def fail():
            raise RuntimeError("task failed")

        with patch("internet_speedtest.threading.Thread", FakeThread):
            with self.assertRaisesRegex(RuntimeError, "task failed"):
                internet_speedtest.run_with_spinner("test", fail)

        self.assertTrue(captured["event"].is_set())
        self.assertTrue(captured["joined"])


if __name__ == "__main__":
    unittest.main()
