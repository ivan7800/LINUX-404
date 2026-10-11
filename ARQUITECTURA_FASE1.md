# LINUX 404 — Fase 1: arquitectura y mapa de contenidos

**Versión:** 0.1.0 · **Estado:** especificación inicial · **Idioma de la interfaz:** español  
**Objetivo:** enseñar Linux de forma práctica y progresiva, con Linux Mint Cinnamon como entorno de referencia.

## 1. Propósito

LINUX 404 será una guía interactiva para aprender, practicar y consultar Linux. Debe permitir que una persona que acaba de instalar Linux Mint pueda orientarse, realizar tareas cotidianas con confianza y entender cuándo una instrucción depende de su distribución.

La aplicación es educativa: no ejecutará comandos en el equipo, no instalará software, no modificará archivos del usuario y no enviará datos a un servidor.

## 2. Público y alcance

- **Principal:** persona principiante que usa Linux Mint Cinnamon en un portátil.
- **Secundario:** usuario que ya conoce lo básico y necesita consultar comandos o resolver una incidencia común.
- **Primera plataforma documentada:** Linux Mint Cinnamon.
- **Referencias comparativas:** Ubuntu/Debian y Fedora solo cuando los pasos difieran de forma relevante.
- **Fuera de alcance inicial:** emulación completa de un sistema operativo, terminal real, reparación automática del equipo y guía exhaustiva de todas las distribuciones.

## 3. Navegación principal

1. **Inicio** — continuar aprendiendo, progreso y accesos rápidos.
2. **Ruta** — itinerario secuencial de módulos y lecciones.
3. **Laboratorio** — terminal simulada y ejercicios guiados.
4. **Biblioteca** — comandos, conceptos y soluciones buscables.
5. **Retos** — prácticas cortas con pistas y explicación de la respuesta.
6. **Progreso** — módulos completados, racha opcional y reinicio de datos.
7. **Ajustes** — tamaño de texto, movimiento reducido, tema, exportar/importar progreso y aviso de versión.

La cabecera tendrá marca, búsqueda global, acceso a ayuda y progreso. En escritorio se usará navegación lateral; en móvil, menú compacto inferior o desplegable con las mismas secciones.

## 4. Pantallas

### 4.1 Inicio

- Mensaje de bienvenida y objetivo de aprendizaje actual.
- Tarjeta **Continuar ruta** con módulo, lección y progreso.
- Accesos: «Mi primer día», «Abrir laboratorio», «Buscar un comando».
- Bloque «Linux Mint en este equipo» con contenido educativo, sin leer el dispositivo.
- Consejo de seguridad breve y contextual.

### 4.2 Ruta de aprendizaje

- Vista por módulos con estado: pendiente, en curso o completado.
- Cada módulo muestra duración estimada, objetivos y requisitos previos.
- Las lecciones se pueden abrir libremente; la secuencia recomendada no bloquea contenido.
- Al final de la lección: resumen breve, práctica, marcar completada y siguiente paso.

### 4.3 Lección

- Explicación breve por bloques, capturas/diagramas locales cuando aporten valor.
- Pasos numerados y resultado esperado.
- Bloques de terminal con botón de copiar y etiqueta de riesgo.
- Aviso visible cuando la instrucción sea específica de Mint/Cinnamon o requiera Internet.
- Enlaces internos a conceptos y solución de problemas relacionados.

### 4.4 Laboratorio simulado

- Terminal visual con prompt ficticio y contexto declarado, por ejemplo `usuario@mint:~$`.
- Lista explícita de comandos soportados y sus escenarios.
- Salida didáctica predefinida; nada se ejecuta en el sistema anfitrión.
- Validación de ejercicios por coincidencia de comando/objetivo, con tolerancia a espacios y opciones documentadas.
- Pistas graduadas, explicación de la salida y botón de reiniciar ejercicio.
- Aviso permanente: «Simulación educativa. No es una terminal real».

### 4.5 Biblioteca

- Búsqueda por palabra, comando, tarea o síntoma.
- Filtros: Mint, terminal, archivos, software, red, seguridad y solución de problemas.
- Cada resultado incluye propósito, ejemplo, efecto esperado, riesgo y compatibilidad.
- Favoritos guardados localmente.

### 4.6 Progreso y ajustes

- Progreso local en el navegador; no requiere cuenta.
- Exportación/importación JSON validada para poder llevar el progreso a otro navegador.
- Acción de borrar progreso con confirmación clara.
- Preferencias accesibles y persistidas localmente.

## 5. Programa de contenidos

### Módulo 0 — Orientarse en Linux Mint
1. Qué es Linux y qué significa una distribución.
2. Conocer el escritorio Cinnamon: menú, panel, ventanas y área de notificación.
3. Abrir aplicaciones y ajustes del sistema.
4. Actualizar Linux Mint desde el Gestor de actualizaciones.
5. Primeros ajustes: idioma, pantalla, energía y conexión.

### Módulo 1 — Archivos y carpetas
1. Sistema de archivos y carpeta personal.
2. Rutas absolutas y relativas; `/`, `/home` y dispositivos extraíbles.
3. Archivos ocultos y extensiones.
4. Copiar, mover, renombrar y eliminar desde el gestor de archivos.
5. Papelera, USB y expulsión segura.

### Módulo 2 — Primeros pasos con la terminal
1. Abrir y cerrar la terminal; prompt y directorio actual.
2. `pwd`, `ls` y `cd`.
3. Ayuda con `man`, `--help` y búsqueda.
4. Autocompletado, historial y rutas con espacios.
5. Leer una salida sin memorizarla.

### Módulo 3 — Comandos cotidianos
1. Crear carpetas y archivos de prueba: `mkdir`, `touch`.
2. Copiar, mover y renombrar: `cp`, `mv`.
3. Leer texto: `cat`, `less`, `head`, `tail`.
4. Buscar archivos y texto: `find`, `grep` (introducción segura).
5. Comodines y tuberías con ejemplos simples.

### Módulo 4 — Instalar y mantener aplicaciones
1. Gestor de software de Mint.
2. Qué son repositorios, paquetes y dependencias.
3. APT: `apt update`, `apt upgrade`, `apt install` y `apt remove`.
4. Flatpak y diferencias visibles para el usuario.
5. Cómo comprobar el origen de una aplicación y evitar instaladores dudosos.

### Módulo 5 — Usuarios, permisos y procesos
1. Usuario normal frente a administrador.
2. `sudo`: cuándo aparece y cómo interpretar la petición de contraseña.
3. Permisos de lectura, escritura y ejecución.
4. Procesos con Monitor del sistema y `ps`/`top` como consulta.
5. Qué no cambiar sin entenderlo: permisos recursivos y propiedad de carpetas.

### Módulo 6 — Internet, red y dispositivos
1. Wi-Fi, Ethernet y ajustes de red de Mint.
2. Diagnóstico inicial: comprobar enlace, dirección y DNS.
3. Comandos de consulta: `ip`, `ping`, `nmcli` (con nota de compatibilidad).
4. Bluetooth, audio, pantalla e impresoras: comprobaciones básicas.
5. Qué información recopilar antes de pedir ayuda.

### Módulo 7 — Discos, copias y recuperación
1. Espacio disponible con el analizador de uso y `df -h`.
2. Discos y particiones: conceptos, sin instrucciones de formateo en prácticas.
3. Copias de seguridad con Timeshift y copias de documentos personales.
4. Puntos de restauración frente a copia de archivos: diferencias.
5. Recuperación prudente y cuándo detenerse antes de escribir en un disco.

### Módulo 8 — Seguridad y mantenimiento
1. Actualizaciones y reinicios.
2. Contraseñas, bloqueo de pantalla y fuentes de software.
3. Firewall de Mint: concepto y uso desde la interfaz.
4. Descargas, permisos y señales de riesgo.
5. Copias de seguridad, restauración y hábitos sostenibles.

### Módulo 9 — Solución de problemas frecuentes
1. No hay sonido o no se detecta el micrófono.
2. Wi-Fi lento o desconectado.
3. Aplicación congelada o que no abre.
4. Poco espacio en disco.
5. Pantalla, Bluetooth, USB e impresora.
6. Recopilar versión, mensaje de error y pasos para reproducir.

### Módulo 10 — Siguiente nivel
1. Shell y scripts: qué son y cómo leer un script antes de ejecutarlo.
2. Variables, redirecciones y tuberías (introducción).
3. Servicios y registros: conceptos, sin cambios de configuración iniciales.
4. Virtualización y contenedores: diferencias generales.
5. Rutas de aprendizaje: administración, desarrollo y escritorio Linux.

## 6. Ficha estándar de cada comando

Cada entrada de la Biblioteca tendrá estos campos:

- Nombre y categoría.
- Sintaxis y ejemplo seguro.
- Qué hace, explicado en lenguaje claro.
- Resultado esperado en el escenario indicado.
- Requisitos y distribución probada/documentada.
- Nivel de riesgo: **informativo**, **cambia el sistema**, **puede borrar datos**.
- Alternativa gráfica cuando exista.
- Errores habituales y cómo deshacer el cambio, si es posible.

No se publicará un comando destructivo como ejercicio ejecutable. Los ejemplos peligrosos se mostrarán desactivados o como texto explicativo, con el riesgo señalado antes del comando.

## 7. Criterios pedagógicos y de seguridad

- Una lección debe resolver una tarea concreta y explicar el resultado.
- No presuponer experiencia con Linux ni con la terminal.
- Separar comandos de consulta de los que cambian el sistema.
- No recomendar `sudo` por rutina ni comandos copiados de fuentes desconocidas.
- No usar `curl | sh`, borrados recursivos, formateo o cambios masivos de permisos en prácticas.
- Explicar diferencias entre Mint, Ubuntu/Debian y Fedora justo donde afecten al paso.
- Mostrar fecha o versión editorial para contenido sensible a cambios.
- Incluir alternativa gráfica cuando sea razonable.
- Permitir avanzar y consultar sin puntos, castigos ni bloqueos artificiales.

## 8. Persistencia y datos

Datos locales previstos:

- Lecciones completadas y última lección visitada.
- Favoritos y preferencias de interfaz.
- Estado de retos, sin guardar texto libre innecesario.

No se almacenarán nombres reales, contraseñas, rutas del equipo ni datos del sistema operativo. El progreso podrá borrarse y exportarse desde Ajustes.

## 9. Estructura técnica prevista

Web estática, apta para GitHub Pages, sin backend, sin telemetría y sin CDNs. Objetivo de mantener el paquete por debajo de 100 archivos si el contenido y las pruebas lo permiten.

```text
LINUX-404/
├── index.html
├── styles.css
├── app.js
├── content/
│   ├── lessons.js
│   ├── commands.js
│   ├── challenges.js
│   └── troubleshooting.js
├── assets/
│   ├── icons/                 (SVG locales)
│   └── images/                (solo recursos propios/locales necesarios)
├── tests/
│   ├── test_content.py
│   └── test_app.py
├── README.md
├── CHANGELOG.md
├── LICENSE
└── INICIAR_WINDOWS.bat
```

La estructura podrá ajustarse al implementar, siempre que conserve separación entre contenido y lógica, rutas válidas en subcarpeta de GitHub Pages y funcionamiento sin conexión a servicios externos.

## 10. Criterios de aceptación de la Fase 1

- [x] Público y objetivo definidos.
- [x] Navegación y pantallas principales definidas.
- [x] Ruta de aprendizaje ordenada de principiante a siguiente nivel.
- [x] Laboratorio delimitado como simulación segura.
- [x] Formato para comandos y niveles de riesgo definido.
- [x] Persistencia local y controles de privacidad definidos.
- [x] Estructura técnica inicial compatible con web estática.
- [x] Validación de la ruta educativa mientras se redactan e implementan las lecciones (Fase 6: 60 lecciones, retos, comparación de distribuciones).

**Salida de fase:** mapa aprobado como base de implementación. Las lecciones concretas se completarán por bloques durante las fases de aprendizaje y contenido.
