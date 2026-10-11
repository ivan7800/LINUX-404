from pathlib import Path
from html.parser import HTMLParser
import re

ROOT=Path(__file__).resolve().parents[1]
html=(ROOT/'index.html').read_text(encoding='utf-8')
js=(ROOT/'app.js').read_text(encoding='utf-8')
css=(ROOT/'styles.css').read_text(encoding='utf-8')

class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.tags=[]; self.errors=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs); self.tags.append((tag,a))
        if 'id' in a:self.ids.append(a['id'])
        if any(k.lower().startswith('on') for k in a):self.errors.append(f'evento inline en <{tag}>')
        if tag=='a' and a.get('target')=='_blank' and 'noopener' not in a.get('rel','').split():self.errors.append('enlace externo sin noopener')

a=AuditParser();a.feed(html)
assert len(a.ids)==len(set(a.ids)), 'Hay IDs duplicados en el HTML'
assert not a.errors, '; '.join(a.errors)
assert '<meta name="viewport"' in html and 'id="inicio"' in html
assert all(name in html for name in ['id="view-home"','id="view-route"','id="view-lesson"','id="view-lab"','id="view-library"','id="view-troubleshoot"','id="view-issue"','id="view-distributions"','id="view-platforms"','id="view-challenges"','id="view-progress"'])
local_refs=[]
for tag,attrs in a.tags:
    for attr in ('src','href'):
        value=attrs.get(attr,'')
        if value and not value.startswith(('#','http://','https://','mailto:','tel:')):local_refs.append(value)
for ref in local_refs:
    assert (ROOT/ref.split('#')[0]).is_file(),f'Recurso local roto: {ref}'
assert html.index('src="content-library.js"') < html.index('src="app.js"')
assert html.index('src="course-content.js"') < html.index('src="app.js"')
assert all(x in js for x in ['function render(view','function exportProgress()','function importProgress()','function updateHomeNextLesson()','function platformTemplate()','data-quiz-retry'])
assert all(x in js for x in ['validLessonIds','validExerciseIds','validIssueIds','Number.isInteger(answer)'])
assert all(x in css for x in ['@media(max-width:820px)','@media(max-width:620px)','@media(max-width:560px)','prefers-reduced-motion','html.matrix-mode','@keyframes matrix-drift'])
assert all(x in css for x in ['Fase 10','@keyframes page-arrive','@keyframes window-float','backdrop-filter:blur(22px)','html.reduce-motion .mint-window','grid-template-columns:278px minmax(0,1fr)'])
assert all(x in css for x in ['.nav-item.active .nav-icon','.quick-card:hover','.topbar{position:sticky','@media(prefers-reduced-motion:reduce){.mint-window'])
assert all(x in js for x in ['matrixMode','linux404.matrixMode','simulatedHost()'])
assert all(x in js for x in ['homeLessonCount','homeQuizCount','homeCommandCount','homeGlossaryCount','glossaryMatches',"'Conceptos'"])
assert all(x in html for x in ['id="homeLessonCount"','id="homeQuizCount"','id="homeCommandCount"','id="homeGlossaryCount"'])
assert all(x in css for x in ['.content-ribbon{','.glossary-grid{','.glossary-card{'])
assert '0.11.0-rc1' in js and 'Fase 11' in js
assert 'new Worker(' not in js and 'serviceWorker' not in js
assert all(x not in js for x in ['fetch(','XMLHttpRequest','eval(','new Function(','child_process'])
assert 'navigator.userAgent' not in js and 'navigator.platform' not in js, 'No debe detectar el sistema operativo'
assert 'linux404.platform' in js and 'learn.microsoft.com/windows/wsl/install' in js
assert 'rel="noopener noreferrer"' in js, 'Los enlaces externos generados deben aislar la ventana de origen'
assert not re.search(r'(?<!:)\b(?:src|href)=["\']/(?!/)',html), 'Hay rutas absolutas que pueden romper bajo subruta de GitHub Pages'
print(f'OK: release estática, {len(a.ids)} IDs únicos, recursos relativos, navegación, seguridad y responsive.')
