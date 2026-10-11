from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / 'index.html').read_text(encoding='utf-8')
app = (ROOT / 'app.js').read_text(encoding='utf-8')
linux_launcher = (ROOT / 'INICIAR_LINUX.sh').read_text(encoding='utf-8')
windows_launcher = (ROOT / 'INICIAR_WINDOWS.bat').read_text(encoding='utf-8')
readme = (ROOT / 'README.md').read_text(encoding='utf-8')

assert 'data-view="platforms"' in html and 'id="view-platforms"' in html
assert all(f"{profile}:" in app for profile in ("mint", "windows", "wsl"))
assert all(f'data-profile="{profile}"' in app for profile in ("mint", "windows", "wsl"))
assert 'linux404.platform' in app, 'El perfil debe persistir localmente'
assert 'navigator.userAgent' not in app and 'navigator.platform' not in app
assert 'learn.microsoft.com/windows/wsl/install' in app
assert 'PowerShell y Símbolo del sistema no son terminales Linux' in app
assert 'no convierte Windows en Mint Cinnamon' in app
course = (ROOT / 'course-content.js').read_text(encoding='utf-8')
assert "add('11','Windows, WSL" in course and "id:'q:wsl-shell',module:'11'" in course
assert 'linux404.matrixMode' in app and 'matrix-drift' in (ROOT / 'styles.css').read_text(encoding='utf-8')
assert 'xdg-open' in linux_launcher and 'index.html' in linux_launcher
assert 'start "LINUX 404" "%~dp0index.html"' in windows_launcher
assert 'INICIAR_LINUX.sh' in readme and 'INICIAR_WINDOWS.bat' in readme
assert 'no ejecuta órdenes reales' in readme
print('OK: rutas de uso Mint/Windows, perfiles locales, WSL opcional y lanzadores multiplataforma.')
