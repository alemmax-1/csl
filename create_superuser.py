from django.contrib.auth import get_user_model
import os

# Ottieni il modello utente
User = get_user_model()

# Dati del superuser da variabili d'ambiente
SUPERUSER_USERNAME = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
SUPERUSER_EMAIL = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
SUPERUSER_PASSWORD = os.getenv("DJANGO_SUPERUSER_PASSWORD", "admin123")

# Crea il superuser se non esiste già
if not User.objects.filter(username=SUPERUSER_USERNAME).exists():
    User.objects.create_superuser(
        username=SUPERUSER_USERNAME,
        email=SUPERUSER_EMAIL,
        password=SUPERUSER_PASSWORD,
    )
    print(f"Superuser '{SUPERUSER_USERNAME}' creato con successo.")
else:
    print(f"Superuser '{SUPERUSER_USERNAME}' esiste già.")