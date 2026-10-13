"""Execution-layer observation only; delegates coordination to the unchanged CLI."""
from pathlib import Path
import sys, json, hashlib, subprocess, datetime, shutil

ROOT = Path(__file__).resolve().parents[3]
RUN = 'normal-prep-20261013-01'
ARCH = ROOT / 'experiments' / ('coordinator-' + RUN)
CLI = ROOT / '../../personal-learning-suite/scripts/coordinate_preparation.py'
def stamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()
def record(role, kind, data):
    dest = ARCH / 'observations' / role
    dest.mkdir(parents=True, exist_ok=True)
    name = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%f') + '-' + kind + '.json'
    (dest / name).write_text(json.dumps({'recorded_at':stamp(), 'role':role, 'kind':kind, **data},ensure_ascii=False,indent=2),encoding='utf-8')
def invoke(role, args):
    command = [sys.executable,'-B','-X','utf8',str(CLI),'--workspace',str(ROOT),'--role',role,*args]
    result = subprocess.run(command,capture_output=True,text=True,encoding='utf-8')
    record(role,'coordinator',{'command':command,'stdout':result.stdout,'stderr':result.stderr,'exit_code':result.returncode})
    return result
def main():
    mode, role, *args = sys.argv[1:]
    if mode == 'read':
        for arg in args:
            path = (ROOT / arg).resolve()
            raw = path.read_bytes()
            digest = hashlib.sha256(raw).hexdigest()
            dest = ARCH / 'read-bytes' / digest
            dest.parent.mkdir(parents=True,exist_ok=True)
            if not dest.exists(): dest.write_bytes(raw)
            record(role,'read',{'path':str(path),'sha256':digest,'bytes':len(raw),'byte_copy':str(dest.relative_to(ROOT))})
            print(str(path))
            print(raw.decode('utf-8-sig'))
    elif mode == 'query':
        result = invoke(role,args)
        print(result.stdout,end='')
        if result.stderr: print(result.stderr,file=sys.stderr,end='')
        return result.returncode
    elif mode == 'coord':
        action, request_path = args
        request_file = (ROOT / request_path).resolve()
        payload = json.loads(request_file.read_text(encoding='utf-8-sig'))
        state_result = invoke(role,['state'])
        if state_result.returncode: print(state_result.stdout); return state_result.returncode
        state = json.loads(state_result.stdout)
        revision = state.get('state_revision',state.get('state',{}).get('state_revision'))
        if revision is None: raise ValueError('state_revision_unavailable')
        payload.setdefault('expected_state_revision',revision)
        submitted = request_file.with_name(request_file.stem + '-submitted.json')
        if submitted.exists(): raise ValueError('submitted_request_already_exists_no_automatic_retry')
        submitted.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
        record(role,'request',{'action':action,'source_request':str(request_file),'submitted_request':str(submitted),'payload':payload})
        result = invoke(role,['execute','--action',action,'--request-file',str(submitted)])
        print(result.stdout,end='')
        if result.stderr: print(result.stderr,file=sys.stderr,end='')
        return result.returncode
    else: raise ValueError(mode)
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
