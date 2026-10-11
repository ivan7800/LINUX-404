'use strict';
const fs = require('node:fs');
const vm = require('node:vm');
const context = {globalThis:{}};
vm.runInNewContext(fs.readFileSync(new URL('../content-library.js', `file://${__filename}`), 'utf8'), context);
const data = context.globalThis.Linux404Content;
const assert = require('node:assert/strict');
assert.equal(data.commands.length, 42, 'Debe haber 42 fichas de comandos');
assert.equal(data.issues.length, 10, 'Debe haber 10 guías de diagnóstico');
assert.equal(data.glossary.length, 24, 'Debe haber 24 conceptos de glosario');
assert.ok(data.references.length >= 5, 'Debe haber fuentes oficiales de apoyo');
assert.equal(new Set(data.commands.map(x => x.id)).size, data.commands.length, 'IDs de comando únicos');
assert.equal(new Set(data.issues.map(x => x.id)).size, data.issues.length, 'IDs de guía únicos');
assert.equal(new Set(data.glossary.map(x => x.id)).size, data.glossary.length, 'IDs de glosario únicos');
for (const c of data.commands) {
  for (const key of ['id','cmd','title','cat','risk','desc','example','tags']) assert.ok(c[key], `Comando incompleto: ${key}`);
}
for (const i of data.issues) {
  for (const key of ['id','title','summary','steps','avoid','next','tags']) assert.ok(i[key], `Guía incompleta: ${key}`);
  assert.ok(i.steps.length >= 3, `Guía corta: ${i.id}`);
}
for (const t of data.glossary) for (const key of ['id','term','definition','example','tags']) assert.ok(t[key], `Concepto incompleto: ${key}`);
const rm = data.commands.find(x => x.cmd === 'rm nombre');
assert.ok(rm && rm.caution && rm.alt, 'La ficha destructiva debe incluir precaución y alternativa');
assert.ok(Object.isFrozen(data.commands) && Object.isFrozen(data.issues), 'Colecciones inmutables');
console.log('OK: 42 comandos, 24 conceptos, 10 guías completas, IDs, referencias y cautela para rm.');
