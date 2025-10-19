from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import getpass

class Command(BaseCommand):
    help = 'Permite cambiar la contraseña de un usuario desde la terminal'

    def handle(self, *args, **options):
        username = input("Ingresa tu usuario: ")
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('Usuario no existe'))
            return

        new_password = getpass.getpass("Ingresa la nueva contraseña: ")
        new_password2 = getpass.getpass("Confirma la nueva contraseña: ")

        if new_password != new_password2:
            self.stdout.write(self.style.ERROR('Las contraseñas no coinciden'))
            return
        
        user.set_password(new_password)
        user.save()
        self.stdout.write(self.style.SUCCESS('Contraseña actualizada con éxito'))
