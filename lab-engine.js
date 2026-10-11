/* Intérprete cerrado para el laboratorio educativo. No invoca procesos ni el shell del sistema. */
(function(root){
  'use strict';
  const HOME='/home/usuario';
  const createState=()=>({cwd:HOME,dirs:new Set([HOME,HOME+'/Documentos',HOME+'/Descargas']),files:new Map([[HOME+'/bienvenida.txt','Este es un archivo de ejemplo del laboratorio Linux 404.']]),lastCmd:'',lastOutput:'',log:[{prompt:'',command:'',output:'Laboratorio listo. Escribe help para ver los comandos permitidos.',type:'system'}]});
  const allowedName=(s,max=48)=>/^[A-Za-z0-9._-]{1,48}$/.test(s)&&s.length<=max&&s!=='.'&&s!=='..';
  function execute(state,raw){
    const command=String(raw||'').trim().replace(/\s+/g,' ');
    const prompt=state.cwd.replace(HOME,'~')||'/';
    if(!command)return {prompt,command:'',output:'',type:'normal'};
    const parts=command.split(' '),verb=parts[0],arg=parts.slice(1).join(' ');
    let output='',type='normal';state.lastCmd=verb;
    if(/[;&|><`$\\]/.test(command)||command.includes('..')){output='Por seguridad, esta simulación no admite operadores, rutas ascendentes ni cadenas de comandos. Escribe help para ver lo permitido.';type='error';state.lastCmd=''}
    else if(verb==='help'&&parts.length===1)output='Comandos simulados: pwd, ls, cd [carpeta], mkdir nombre, touch nombre, cat archivo, cp origen destino, mv origen destino, grep palabra archivo, file archivo, whoami, clear. Solo afectan a este entorno ficticio.';
    else if(verb==='clear'&&parts.length===1){state.log=[];return {prompt,command,output:'',type:'clear'}}
    else if(verb==='pwd'&&parts.length===1)output=state.cwd;
    else if(verb==='whoami'&&parts.length===1)output='usuario';
    else if(verb==='ls'&&parts.length===1){const dirs=[...state.dirs].filter(p=>p!==state.cwd&&p.substring(0,p.lastIndexOf('/'))===state.cwd).map(p=>p.split('/').pop());const files=[...state.files.keys()].filter(p=>p.substring(0,p.lastIndexOf('/'))===state.cwd).map(p=>p.split('/').pop());output=[...dirs,...files].sort().join('  ')||'(carpeta vacía)'}
    else if(verb==='cd'&&parts.length<=2){const target=arg===''?HOME:arg==='..'?state.cwd.substring(0,state.cwd.lastIndexOf('/')):state.cwd+'/'+arg;if(state.dirs.has(target)&&target.startsWith(HOME)){state.cwd=target;output='Carpeta actual: '+target}else{output='No existe esa carpeta en el entorno de práctica.';type='error';state.lastCmd=''}}
    else if(verb==='mkdir'&&parts.length===2&&allowedName(arg,32)){const target=state.cwd+'/'+arg;if(state.dirs.has(target)||state.files.has(target)){output='Ya existe un elemento con ese nombre.';type='error';state.lastCmd=''}else{state.dirs.add(target);output=`Carpeta creada en la simulación: ${target}`}}
    else if(verb==='touch'&&parts.length===2&&allowedName(arg)){const target=state.cwd+'/'+arg;if(state.dirs.has(target)){output='Ya existe una carpeta con ese nombre.';type='error';state.lastCmd=''}else{state.files.set(target,'');output=`Archivo vacío creado en la simulación: ${target}`}}
    else if(verb==='cat'&&parts.length===2&&allowedName(arg)){const target=state.cwd+'/'+arg;if(state.files.has(target))output=state.files.get(target)||'(archivo vacío)';else{output='No existe ese archivo en la carpeta actual.';type='error';state.lastCmd=''}}
    else if(verb==='cp'&&parts.length===3&&allowedName(parts[1])&&allowedName(parts[2])){const source=state.cwd+'/'+parts[1],target=state.cwd+'/'+parts[2];if(!state.files.has(source)){output='No existe el archivo de origen en esta carpeta.';type='error';state.lastCmd=''}else if(source===target||state.files.has(target)||state.dirs.has(target)){output='El destino ya existe o coincide con el origen. No se sobrescribió nada.';type='error';state.lastCmd=''}else{state.files.set(target,state.files.get(source));output=`Copia creada en la simulación: ${parts[2]}`}}
    else if(verb==='mv'&&parts.length===3&&allowedName(parts[1])&&allowedName(parts[2])){const source=state.cwd+'/'+parts[1],target=state.cwd+'/'+parts[2];if(!state.files.has(source)){output='No existe el archivo de origen en esta carpeta.';type='error';state.lastCmd=''}else if(source===target||state.files.has(target)||state.dirs.has(target)){output='El destino ya existe o coincide con el origen. No se sobrescribió nada.';type='error';state.lastCmd=''}else{const value=state.files.get(source);state.files.delete(source);state.files.set(target,value);output=`Nombre cambiado en la simulación: ${parts[2]}`}}
    else if(verb==='grep'&&parts.length===3&&allowedName(parts[1])&&allowedName(parts[2])){const value=state.files.get(state.cwd+'/'+parts[2]);if(value===undefined){output='No existe ese archivo en la carpeta actual.';type='error';state.lastCmd=''}else{const matches=value.split(/\r?\n/).filter(line=>line.includes(parts[1]));output=matches.join('\n')||'Sin coincidencias.'}}
    else if(verb==='file'&&parts.length===2&&allowedName(arg)){const value=state.files.get(state.cwd+'/'+arg);if(value===undefined){output='No existe ese archivo en la carpeta actual.';type='error';state.lastCmd=''}else output=value===''?'archivo de texto vacío':'archivo de texto UTF-8'}
    else{output=`Comando no disponible en esta práctica: ${verb}. No se ejecutó. Escribe help para ver la lista permitida.`;type='error';state.lastCmd=''}
    state.lastOutput=output;
    return {prompt,command,output,type};
  }
  root.Linux404Lab=Object.freeze({createState,execute});
})(globalThis);
