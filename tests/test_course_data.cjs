'use strict';
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const context = {globalThis:{}};
vm.runInNewContext(fs.readFileSync(new URL('../course-content.js', `file://${__filename}`), 'utf8'), context);
const course = context.globalThis.Linux404Course;
assert.equal(course.lessons.length, 81, 'Debe haber 81 lecciones ampliadas en los módulos 01–14');
for (const module of ['01','02','03','04','05','06','07','08','09','10','11','12','13','14']) {
  const lessons = course.lessons.filter(x => x.module === module);
  const expected = {'01':5,'02':5,'03':5,'04':5,'05':6,'06':6,'07':5,'08':6,'09':7,'10':5,'11':8,'12':6,'13':6,'14':6}[module];
  assert.equal(lessons.length, expected, `Número de lecciones del módulo ${module}`);
}
assert.equal(new Set(course.lessons.map(x => x.id)).size, course.lessons.length, 'IDs de lección únicos');
for (const lesson of course.lessons) {
  for (const key of ['id','module','title','summary','sections','task','takeaway']) assert.ok(lesson[key], `${lesson.id}: falta ${key}`);
  assert.equal(lesson.sections.length, 3, `${lesson.id}: requiere tres bloques pedagógicos`);
  assert.ok(lesson.sections.every(s => s.title && s.text.length > 55), `${lesson.id}: bloque sin desarrollo suficiente`);
}
assert.equal(course.quizzes.length, 24, 'Veinticuatro preguntas de repaso');
for (const q of course.quizzes) assert.ok(q.options.length >= 3 && Number.isInteger(q.answer) && q.answer < q.options.length && q.explanation);
assert.deepEqual(Array.from(course.distributions, x => x.name), ['Linux Mint (Cinnamon)','Ubuntu Desktop','Fedora Workstation','Arch Linux']);
assert.ok(course.references.length >= 7);
assert.equal(course.lessons.filter(x => x.module === '11')[0].title, 'Windows, WSL y Linux: tres entornos distintos');
assert.match(course.lessons.filter(x => x.module === '11').at(-1).title, /distribución/);
assert.ok(course.quizzes.filter(x => x.module === '11').length >= 3);
for (const module of ['12','13','14']) assert.ok(course.quizzes.filter(x => x.module===module).length>=3, `Preguntas del módulo ${module}`);
console.log('OK: 81 lecciones en módulos 01–14, 24 preguntas, cuatro distribuciones y fuentes.');
