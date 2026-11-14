from pathlib import Path
import json,re,shutil
D=Path(__file__).resolve().parents[1]
api={
 'introduction.md':'introduction.md','authentication-and-api-keys.md':'authentication.md','rate-limits.md':'rate-limits.md','accounts-api.md':'accounts.md','addresses-api.md':'addresses.md','transactions-api.md':'transactions.md','tokens-api.md':'tokens.md','blocks-api.md':'blocks.md','logs-api.md':'logs.md','stats-api.md':'stats.md','error-handling.md':'error-handling.md','api-v2.md':'api-v2.md','smart-contracts-api.md':'smart-contracts.md','contract-verification-api.md':'contract-verification.md','nft-api.md':'nft.md','search-api.md':'search.md','pagination.md':'pagination.md','request-examples.md':'request-examples.md','compatibility-api.md':'compatibility.md','compatibility-matrix.md':'compatibility-matrix.md','availability.md':'availability.md','configuration-api.md':'configuration.md'}
helpmap={p.name:p.name for p in (D/'faq').glob('*.md')}
def generate(root,source,mapping,title,intro):
 r=D/root;r.mkdir(exist_ok=True)
 nav='# Table of contents\n\n* ['+title+'](README.md)\n';index='# '+title+'\n\n'+intro+'\n\n'
 for old,new in mapping.items():
  text=(D/source/old).read_text()
  def link(m):
   label,target=m.group(1),m.group(2)
   if '://' in target or target.startswith('#'):return m.group(0)
   path,sep,anchor=target.partition('#');resolved=((D/source/old).parent/path).resolve()
   if resolved.parent==(D/source).resolve() and resolved.name in mapping:return '['+label+']('+mapping[resolved.name]+(sep+anchor if sep else '')+')'
   if path.startswith('../reference/'):return '['+label+'](reference/'+resolved.name+(sep+anchor if sep else '')+')'
   if resolved.is_relative_to(D.resolve()):return '['+label+'](https://doc.turkscan.com/'+str(resolved.relative_to(D.resolve())).removesuffix('.md')+(sep+anchor if sep else '')+')'
   return m.group(0)
  text=re.sub(r'\[([^\]]*)\]\(([^)]+)\)',link,text)
  (r/new).write_text(text);page_title=text.splitlines()[0].removeprefix('# ')
  nav+='* ['+page_title+']('+new+')\n';index+='* ['+page_title+']('+new+')\n'
 (r/'README.md').write_text(index);(r/'SUMMARY.md').write_text(nav)
 (r/'.gitbook.yaml').write_text('root: ./\n\nstructure:\n  readme: README.md\n  summary: SUMMARY.md\n')
 if root=='api-reference':
  (r/'reference').mkdir(exist_ok=True)
  for f in ['openapi.json','endpoint-evidence.json']:shutil.copy2(D/'reference'/f,r/'reference'/f)
generate('api-reference','api-documentation',api,'TurkScan® API Reference','Use the public API to read indexed Turkchain® data. This reference includes exact deployed URLs, parameter requirements, captured responses and explicit compatibility limits. Public reads are distinct from private account features and state-changing verification submissions.')
generate('help-center','faq',helpmap,'TurkScan® Help Center','Find help with wallets, transactions, gas, token visibility, contract verification, APIs and cross-chain transfers. Never share a recovery phrase or private key. When reporting a problem, include the network, public address or transaction hash and the exact error, without credentials.')

print('Generated API Reference and Help Center publication roots')
