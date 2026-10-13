"""Build a factual index from already observable records; never a teaching input."""
from pathlib import Path
import json, hashlib, datetime, shutil

ROOT = Path(__file__).resolve().parents[3]
ARCH = ROOT / 'experiments/coordinator-normal-prep-20261013-01'
def main():
    reads, calls, unknown = [], [], []
    for path in sorted((ARCH / 'observations').rglob('*.json')):
        try:
            obj = json.loads(path.read_text(encoding='utf-8-sig'))
        except (ValueError, UnicodeError):
            unknown.append(str(path.relative_to(ROOT)))
            continue
        if isinstance(obj,dict) and obj.get('kind') == 'read':
            reads.append({**obj,'record_path':str(path.relative_to(ROOT))})
        elif isinstance(obj,dict) and obj.get('kind') in {'coordinator','request'}:
            calls.append({**obj,'record_path':str(path.relative_to(ROOT))})
    professional = []
    directories = ['artifacts/bc-normal-20261013-01','materials/bc-normal-20261013-01',
                   'goals/bc-normal-20261013-01','questions/visible/bc-normal-20261013-01',
                   'questions/teacher-reference/bc-normal-20261013-01','questions/backup/bc-normal-20261013-01',
                   'assessment/bc-normal-20261013-01','plan/bc-normal-20261013-01','code/bc-normal-20261013-01',
                   'sessions/2026-10-13-normal-prep-01','coordination/runs/normal-prep-20261013-01',
                   'experiments/bc-normal-20261013-01','code/coordination/normal-prep-20261013-01']
    for directory in directories:
        start = ROOT / directory
        if not start.exists(): continue
        for path in sorted(start.rglob('*')):
            if not path.is_file(): continue
            rel = path.relative_to(ROOT)
            raw = path.read_bytes()
            digest = hashlib.sha256(raw).hexdigest()
            dest = ARCH / 'file-snapshots' / rel
            dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_bytes(raw)
            professional.append({'path':str(rel),'sha256':digest,'bytes':len(raw),'archived_path':str(dest.relative_to(ROOT))})
    for name,value in [('actual-reads.json',reads),('coordinator-calls.json',calls),('file-snapshot-manifest.json',professional)]:
        (ARCH/name).write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')
    histories = {}
    for event in reads:
        item = histories.setdefault(event['path'], {'path':event['path'],'observed_versions':[]})
        if not any(v['sha256'] == event['sha256'] for v in item['observed_versions']):
            item['observed_versions'].append({'sha256':event['sha256'],'first_observed_read_record':event['record_path'],
                'recorded_at':event['recorded_at'],'byte_copy':event['byte_copy']})
    for file in professional:
        absolute = str((ROOT/file['path']).resolve())
        item = histories.setdefault(absolute, {'path':absolute,'observed_versions':[]})
        item['final_archive_copy'] = file
    (ARCH/'observed-file-version-history.json').write_text(json.dumps(list(histories.values()),ensure_ascii=False,indent=2),encoding='utf-8')
    (ARCH/'observation-coverage.json').write_text(json.dumps({'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'actual_read_events':len(reads),'coordinator_call_and_request_events':len(calls),'copied_files':len(professional),
        'nonstandard_json_records':unknown,'limits':['This index covers observed files and saved tool returns, not hidden model thoughts.',
            'The complete host conversation export and some initial tool-invocation metadata are unavailable.',
            'Copies made at finalization are not falsely labeled as original read times.'],
        'authority':'archive only; current adopted pointers remain solely in coordinator database'},ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'read_events':len(reads),'coordination_events':len(calls),'file_copies':len(professional)},ensure_ascii=False))
if __name__ == '__main__': main()
