from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
js=(root/'app.js').read_text(encoding='utf-8')
engine=(root/'lab-engine.js').read_text(encoding='utf-8')
content=(root/'content-library.js').read_text(encoding='utf-8')
html=(root/'index.html').read_text(encoding='utf-8')
css=(root/'styles.css').read_text(encoding='utf-8')
checks={
 'five complete starter lessons': all(x in js for x in ['Qué es Linux y qué significa una distribución','Conoce el escritorio Cinnamon','Abrir aplicaciones y encontrar ajustes','Actualizar Linux Mint','Primeros ajustes del equipo']),
 'lesson completion and progress': 'complete-lesson' in js and 'linux404.completed' in js and 'lesson-list' in js,
 'favorites and export/import': 'linux404.favorites' in js and 'export-progress' in js and 'import-progress' in js,
 'combined search': 'lessonMatches' in js and 'commandMatches' in js and 'librarySearch' in js,
 'lesson view and navigation': 'id="view-lesson"' in html and 'data-lesson-index' in js,
 'responsive lesson layout': '.lesson-layout' in css and '@media(max-width:680px)' in css,
 'content scripts loaded before app': html.index('src="content-library.js"') < html.index('src="app.js"') and html.index('src="course-content.js"') < html.index('src="app.js"'),
 'individual quiz retry wired': 'data-quiz-retry' in js and 'delete state.quizAnswers[retry.dataset.quizRetry]' in js,
 'all course modules and distribution comparison wired': 'distributionTemplate' in js and 'data-view="distributions"' in js and 'const lessons=[...starterLessons,...course.lessons]' in js,
 '10 troubleshooting guides and official references': 'const issues=[' in content and 'const references=[' in content and 'troubleshootTemplate' in js and 'issueTemplate' in js,
 'quiz responses persist and are validated in exports': 'linux404.quizAnswers' in js and 'quizAnswers:state.quizAnswers' in js and 'Number.isInteger(answer)' in js,
 'issue status persists through import/export/reset': all(x in js for x in ['solvedIssues:[...state.solvedIssues]','linux404.solvedIssues','state.solvedIssues.clear()']),
 'no real command execution': 'exec(' not in js and 'eval(' not in js and 'spawn(' not in js,
}
for label,ok in checks.items(): print(('OK' if ok else 'FAIL')+': '+label)
assert all(checks.values())
checks.update({
 'simulator script loaded before interface': html.index('src="lab-engine.js"') < html.index('src="app.js"'),
 'ten simulated exercises with goals and hints': all(x in js for x in ['¿Dónde estás?','Explora tus carpetas','Entra en Documentos','Crea una carpeta de práctica','Crea tu primer archivo','Duplica una nota','Renombra un archivo','Busca una palabra en un texto','Identifica un archivo sin abrirlo','Organiza dos archivos de prueba']) and 'hints:[' in js and 'check:vm=>' in js,
 'separate simulator and allowlisted commands': 'Linux404Lab.createState()' in js and 'const createState=' in engine and all(f"verb==='{verb}'" in engine for verb in ['mkdir','touch','pwd','cp','mv','grep','file']),
 'content command, issue and glossary collections exposed': 'glossary:Object.freeze(glossary)' in content and 'const glossary=[' in content,
 'progress for practice saved and exported': 'linux404.labCompleted' in js and 'labCompleted:[...state.labCompleted]' in js,
 'shell operators and traversal rejected': "command.includes('..')" in engine and 'rutas ascendentes' in engine,
 'no command execution APIs': all(x not in js+engine for x in ['child_process','eval(','new Function(','fetch(','XMLHttpRequest']),
})
for label,ok in list(checks.items())[-5:]: print(('OK' if ok else 'FAIL')+': '+label)
assert all(checks.values())
