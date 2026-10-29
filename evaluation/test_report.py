import json
import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name('summarize.py')


class ReportTests(unittest.TestCase):
    def run_report(self, data):
        return subprocess.run([sys.executable, str(SCRIPT), '-'], input=json.dumps(data, ensure_ascii=False), capture_output=True, text=True, encoding='utf-8')

    def record(self):
        return {'case_id': 'beginner', 'run_id': '001', 'date': '2026-10-29', 'model': '示例模型', 'environment': '手动交接', 'result': 'partial', 'evidence': '第 3 轮询问了偏好', 'issues': '没有核实时间预算', 'limitations': '无联网', 'transcript': 'user: 我是初学者\nassistant: 你好'}

    def test_reports_manual_results_and_limitation(self):
        result = self.run_report(self.record())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('beginner', result.stdout)
        self.assertIn('partial', result.stdout)
        self.assertIn('没有核实时间预算', result.stdout)
        self.assertIn('无联网', result.stdout)

    def test_rejects_blank_evidence(self):
        record = self.record()
        record['evidence'] = '  '
        result = self.run_report(record)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('evidence', result.stderr)

    def test_rejects_made_up_status(self):
        record = self.record()
        record['result'] = 'perfect'
        result = self.run_report(record)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('result', result.stderr)


if __name__ == '__main__':
    unittest.main()
