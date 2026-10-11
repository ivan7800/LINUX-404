# LINUX 404 — v0.11.0-rc1

Curso completo · Release Candidate para revisión local

Guía estática en español para aprender Linux con Linux Mint Cinnamon como referencia principal y una orientación específica para quien abre la app desde Windows. Incluye comparaciones prudentes con Ubuntu, Fedora y Arch. No necesita cuenta, backend ni dependencias externas.

## Abrir

- **Linux Mint:** ejecuta `INICIAR_LINUX.sh` o abre `index.html`.
- **Windows:** abre `INICIAR_WINDOWS.bat` o `index.html`.
- También puede alojarse en GitHub Pages; las rutas son relativas.
- En **Mint y Windows**, abre la sección del mismo nombre para elegir tu punto de partida. La app no detecta el sistema ni lo modifica.

## Contenido

- 86 lecciones: cinco de orientación inicial, 55 de fundamentos Mint, 18 de práctica ampliada y ocho para Windows + WSL.
- Módulos de archivos, terminal, comandos, software, permisos, red, almacenamiento, seguridad, diagnóstico y siguientes pasos.
- Ruta opcional WSL: requisitos, instalación segura, primera shell, comandos, archivos, APT y exportación/respaldo de la distribución.
- Veinticuatro preguntas de repaso con explicación; respuestas guardadas localmente.
- Diez retos de terminal simulada con navegación, lectura, copia y renombrado dentro de un sistema ficticio en memoria.
- Comparativa educativa de Linux Mint, Ubuntu, Fedora Workstation y Arch Linux, con enlaces a documentación de cada proyecto.
- Guía para usarla desde Mint, Windows sin WSL o Windows con WSL. WSL es opcional y no proporciona el escritorio Mint Cinnamon.
- Biblioteca de 42 fichas de comandos, 24 conceptos explicados y diez guías de incidencias comunes.
- Favoritos, lecciones, retos, diagnósticos revisados y respuestas exportables/importables en JSON.
- Diseño adaptable con estética Matrix configurable, animaciones discretas y reducción de movimiento.

## Seguridad y datos

La aplicación no consulta el sistema operativo, no recoge credenciales y no ejecuta órdenes reales. El laboratorio acepta solo instrucciones explícitas sobre un entorno temporal ficticio. La biblioteca es material educativo; comprueba siempre distribución, versión y contexto antes de seguir una instrucción en una terminal real. PowerShell/CMD no son shells Linux. WSL requiere una instalación separada y puede necesitar componentes de Windows, permisos y reinicio; consulta la documentación oficial de Microsoft. Las comparaciones de distribuciones son orientativas y remiten a fuentes oficiales.

El progreso se almacena en `localStorage`. La exportación JSON permite moverlo entre navegadores; la importación valida los identificadores contra el contenido incluido.

## Licencia

El código y los materiales de este repositorio se distribuyen bajo la licencia MIT. Consulta [`LICENSE`](LICENSE) para ver sus condiciones.

## Verificación local

```bash
node --check content-library.js
node --check course-content.js
node --check app.js
node --check lab-engine.js
node tests/test_lab_engine.cjs
node tests/test_content_data.cjs
node tests/test_course_data.cjs
python3 tests/test_structure.py
python3 tests/test_content.py
python3 tests/test_release_readiness.py
python3 tests/test_platform_support.py
```

## Estado

Fases 1–10 completadas; la Fase 11 amplía el curso con tareas de mantenimiento, archivos y copias, herramientas técnicas, glosario y práctica simulada. La interfaz de Fase 10 aporta navegación flotante y animaciones suaves. Las pruebas automatizadas revisan recursos locales, rutas relativas, estructura, privacidad, datos del curso, laboratorio seguro y contenido multiplataforma. No se pudo hacer la prueba visual/E2E en el entorno de construcción porque no hay un ejecutable de Chromium disponible. Revisa esta compilación en Mint y Windows antes de publicarla.
