# Mopidy-FadePause

Este plugin realiza un fade out de X segundos al pulsar pausa en Mopidy. Una vez pausado, el volumen se restablece al valor original.

## Instalación

```bash
pip install .
```

## Configuración

Agrega esto en `~/.config/mopidy/mopidy.conf`:

```ini
[fadepause]
enabled = true
fade_duration = 5  ; o el número de segundos que desees
```
