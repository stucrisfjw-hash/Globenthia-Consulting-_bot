# Bot Messenger 24/7 en Render

1. Subir a GitHub este repositorio.
2. Conectar con Render → New Web Service.
3. Build command:
   pip install -r requirements.txt
4. Start command:
   gunicorn app:app
5. Agregar en Environment Variables:
   FB_PAGE_TOKEN = (tu token de página)
   VERIFY_TOKEN = midemo123
6. Conectar en Meta Developers → Messenger → Webhook.
