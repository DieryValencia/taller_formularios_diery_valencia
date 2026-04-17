# Despliegue en Vercel

Este repositorio queda preparado para desplegar el proyecto Django en Vercel.

## Archivos agregados

- `requirements.txt`
- `vercel.json`
- `.vercelignore`

## Variables de entorno recomendadas en Vercel

- `SECRET_KEY`
- `DEBUG=False`
- `ALLOWED_HOSTS=.vercel.app,.now.sh`

## Comandos

Desde la raiz del repositorio:

```bash
vercel
```

Para produccion:

```bash
vercel --prod
```

## Nota

El proyecto usa `whitenoise` para servir los archivos estaticos de Django dentro de Vercel.
