# 维护者脚本化逐事件枚举，仅核对模型数值，不构成独立评审或真实用户验证。
import json
from pathlib import Path
p=Path(__file__).parent/'probes'
cs=json.loads((p/'counting-probes.json').read_text(encoding='utf-8'))['cases']
assert len(cs)==9
for c in cs:
 if c['kind']=='score_max':
  events=[kind for q in range(c['q']) for k in range(c['keys']) for kind in (['qread']*c['d']+['kread']*c['d']+['scorewrite','scoreread'])]
  assert len(events)==c['total'] and events.count('scorewrite')+events.count('scoreread')==c['score_layer']
  assert sum(x not in ('scorewrite','scoreread') for x in events)==c['new_total'] and c['new_score_layer']==0
 elif c['kind']=='tile_matmul':
  reads=[('a',i,k) for i in range(c['m']) for k in range(c['k'])]+[('b',k,j) for k in range(c['k']) for j in range(c['n'])]
  writes=[('c',i,j) for i in range(c['m']) for j in range(c['n'])]
  assert len(reads)==c['input_reads'] and len(writes)==c['output_writes'] and len(reads)+len(writes)==c['total']
  assert sum(1 for i in range(c['m']) for k in range(c['k']) for j in range(c['n']))==c['mac']
 else:
  assert len([1 for _ in range(c['elements']) for __ in range(c['bits'])])+len([1 for _ in range(c['scale_bits'])])==c['total_bits']
h=json.loads((p/'h-probes.json').read_text(encoding='utf-8'))['cases']
assert len(h)==8
for c in h:
 if 'P' in c:
  rate=min(c['P'],c['B']*c['mac']/c['elements'])
  if 'expected_rate' in c: assert rate==c['expected_rate']
  if c.get('category')=='numeric' or 'expected' in c: assert c['expected']==('compute' if c['P']<c['B']*c['mac']/c['elements'] else 'bandwidth' if c['P']>c['B']*c['mac']/c['elements'] else 'balanced')
  if 'claimed_rate' in c: assert c['claimed_rate'] != rate
  if 'claimed_label' in c: assert c['claimed_label'] != c['expected']
print('PASS: 9 counting and 8 teaching probes checked; synthetic, not measured')
