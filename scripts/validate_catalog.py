#!/usr/bin/env python3
"""Basic structural validation for the AI Atlas registry."""
import csv,json,re,sys
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/"data"/"ai-tools.json"; CSV=ROOT/"data"/"ai-tools.csv"
REQ={"id","name","resource_type","primary_category","description","official_url","record_status"}
TYPES={"product","model_family","model_checkpoint","api_provider","framework","library","dataset","benchmark","infrastructure","research_resource","protocol","learning_resource","company"}
STATES={"seed","needs_review","verified","stale","archived"}
def valid_url(s):
    if not isinstance(s,str): return False
    u=urlparse(s); return u.scheme in ("http","https") and bool(u.netloc)
def main():
    if not DATA.exists(): print("FAIL: missing JSON registry"); return 1
    try: rows=json.loads(DATA.read_text(encoding="utf-8"))
    except Exception as e: print("FAIL: invalid JSON "+str(e)); return 1
    if not isinstance(rows,list): print("FAIL: root must be array"); return 1
    errors=[]; ids=set(); names=set()
    for i,r in enumerate(rows):
        tag="record["+str(i)+"]"
        if not isinstance(r,dict): errors.append(tag+" is not object"); continue
        for k in sorted(REQ-set(r)): errors.append(tag+" missing "+k)
        rid=r.get("id")
        if not isinstance(rid,str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",rid): errors.append(tag+" invalid id")
        elif rid in ids: errors.append(tag+" duplicate id "+rid)
        ids.add(rid)
        nm=r.get("name"); nk=nm.casefold().strip() if isinstance(nm,str) else ""
        if nk in names: errors.append(tag+" duplicate name "+str(nm))
        names.add(nk)
        if r.get("resource_type") not in TYPES: errors.append(tag+" invalid resource type")
        if r.get("record_status") not in STATES: errors.append(tag+" invalid record status")
        if len(str(r.get("description","")).strip())<10: errors.append(tag+" description too short")
        if not valid_url(r.get("official_url")): errors.append(tag+" invalid official URL")
        if r.get("record_status")=="verified" and not r.get("last_verified"): errors.append(tag+" verified record missing date")
    if CSV.exists():
        with CSV.open(newline="",encoding="utf-8") as f:
            if not list(csv.DictReader(f)): errors.append("CSV empty")
    if errors:
        print("FAIL "+str(len(errors))+" issues"); print("\n".join("- "+e for e in errors[:100])); return 1
    print("PASS "+str(len(rows))+" registry records structurally valid. This does not verify facts or remote links.")
    return 0
if __name__=="__main__": sys.exit(main())
