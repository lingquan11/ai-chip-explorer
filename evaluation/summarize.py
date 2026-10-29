"""Validate and summarize human-supplied test records; does not evaluate the skill."""
import json
import sys
from pathlib import Path

FIELDS = ('case_id', 'run_id', 'date', 'model', 'environment', 'result',
          'evidence', 'issues', 'limitations', 'transcript')
RESULTS = {'pass', 'partial', 'fail', 'not_run'}


def main():
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    if len(sys.argv) < 2:
        print('用法: python summarize.py record.json [record2.json ...]，或用 - 读取标准输入', file=sys.stderr)
        return 2
    records = []
    try:
        for name in sys.argv[1:]:
            content = sys.stdin.read() if name == '-' else Path(name).read_text(encoding='utf-8')
            record = json.loads(content)
            if not isinstance(record, dict):
                raise ValueError(f'{name}: 顶层必须是对象')
            for field in FIELDS:
                if not isinstance(record.get(field), str) or not record[field].strip():
                    raise ValueError(f'{name}: {field} 必须是非空字符串')
            if record['result'] not in RESULTS:
                raise ValueError(f'{name}: result 必须为 pass、partial、fail 或 not_run')
            records.append(record)
    except (OSError, ValueError) as exc:
        print(f'记录无效: {exc}', file=sys.stderr)
        return 1
    print('# 模拟测试记录汇总\n\n仅整理提交的记录，不验证评价真实性，也不代表真实用户效果。')
    for row in records:
        print(f"\n## {row['case_id']} / {row['run_id']}\n")
        for field in FIELDS:
            if field != 'transcript':
                print(f"- **{field}**: {row[field].replace(chr(10), ' ')}")
        print('\n完整对话保存在原始 JSON 的 transcript 字段，请发布前检查隐私。')
    return 0


if __name__ == '__main__':
    sys.exit(main())
