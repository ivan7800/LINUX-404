from pathlib import Path
from html.parser import HTMLParser
ROOT = Path(__file__).resolve().parents[1]
html=(ROOT/'index.html').read_text(encoding='utf-8'); js=(ROOT/'app.js').read_text(encoding='utf-8'); content=(ROOT/'content-library.js').read_text(encoding='utf-8'); css=(ROOT/'styles.css').read_text(encoding='utf-8')
class Parser(HTMLParser):
 def __init__(self): super().__init__(); self.ids=[]; self.attrs=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  self.attrs.append((tag,a))
p=Parser();p.feed(html)
assert len(p.ids)==len(set(p.ids)),'IDs duplicados'
for view in ('home','route','lesson','lab','library','troubleshoot','issue','distributions','platforms','challenges','progress'):
 assert f'id="view-{view}"' in html,f'Falta vista {view}'
assert all(x in content for x in ('pwd','ls','cd','df -h'))
assert html.index('src="content-library.js"') < html.index('src="app.js"')
assert html.index('src="course-content.js"') < html.index('src="app.js"')
assert 'new Set(storedArray' in js and 'linux404.completed' in js
assert 'SIMULACIÓN EDUCATIVA' in html and 'no ejecuta órdenes reales' in (ROOT/'README.md').read_text(encoding='utf-8').lower()
assert 'prefers-reduced-motion' in css and '.reduce-motion' in css
assert not any(('http://' in v or 'https://' in v) for _,a in p.attrs for v in a.values() if isinstance(v,str))
print('OK: HTML, vistas, accesibilidad básica, recursos locales y aviso de laboratorio simulado.')
