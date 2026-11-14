#!/usr/bin/env python3
"""Check GitBook paths, local links, media, JSON examples and API schema references."""
import json,re,subprocess,sys
from pathlib import Path
from urllib.parse import urlsplit,unquote
ROOT=Path(__file__).resolve().parents[1]
errors=[];links=0;examples=0
pages=list(ROOT.rglob('*.md'))
for file in pages:
 text=file.read_text();fences=list(re.finditer(r'^```([^\n]*)\n(.*?)^```\s*$',text,re.M|re.S))
 if len(re.findall(r'^```',text,re.M))!=2*len(fences):errors.append(f'{file.relative_to(ROOT)}: unmatched code fence')
 for fence in fences:
  if fence.group(1).strip()=='json':
   examples+=1
   try:json.loads(fence.group(2))
   except ValueError as e:errors.append(f'{file.relative_to(ROOT)}: invalid JSON example {e}')
 clean=re.sub(r'^```.*?^```\s*$','',text,flags=re.M|re.S)
 targets=re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',clean)+re.findall(r'<(?:img|a)\b[^>]*(?:src|href)="([^"]+)"',clean)
 for target in targets:
  target=target.strip().split(' "')[0];u=urlsplit(target)
  if u.scheme or u.netloc:continue
  if not u.path:continue
  links+=1;p=(file.parent/unquote(u.path)).resolve()
  if not p.is_relative_to(ROOT):errors.append(f'{file.relative_to(ROOT)}: link leaves repository: {target}')
  elif not p.exists():errors.append(f'{file.relative_to(ROOT)}: missing local target: {target}')
roots=[ROOT]+[p.parent for p in ROOT.rglob('.gitbook.yaml') if p.parent!=ROOT]
navpaths=[]
for root in roots:
 nav=(root/'SUMMARY.md').read_text();items=re.findall(r'\]\(([^)#]+)',nav)
 if len(items)!=len(set(items)):errors.append('Duplicate navigation path in '+str(root))
 navpaths+=items
 for file in pages:
  owner=max((r for r in roots if file.is_relative_to(r)),key=lambda r:len(r.parts))
  if owner!=root:continue
  rel=str(file.relative_to(root))
  if rel!='SUMMARY.md' and rel not in items:errors.append('Page missing from navigation: '+str(file.relative_to(ROOT)))
for name in ['reference/openapi.json','reference/endpoint-evidence.json']:
 try:json.loads((ROOT/name).read_text())
 except ValueError as e:errors.append(f'{name}: {e}')
spec=json.loads((ROOT/'reference/openapi.json').read_text())
def refs(x):
 if isinstance(x,dict):
  if '$ref' in x and x['$ref'].startswith('#/'):
   cur=spec
   try:
    for k in x['$ref'][2:].split('/'):cur=cur[k.replace('~1','/').replace('~0','~')]
   except KeyError:errors.append('Unresolved schema '+x['$ref'])
  for v in x.values():refs(v)
 elif isinstance(x,list):
  for v in x:refs(v)
refs(spec)
print(json.dumps({'markdown_files':len(pages),'navigation_pages':len(navpaths),'local_links':links,'json_examples':examples,'openapi_paths':len(spec['paths']),'errors':errors},indent=2))
sys.exit(bool(errors))
