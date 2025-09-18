import os
import csv
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Update movie images in the database from the images folder"

    def handle(self, *args, **kwargs):
        # Ruta de la carpeta de imágenes
        images_folder = os.path.join('media', 'movie', 'images')
        updated_count = 0

        # Recorre todas las películas en la base de datos
        for movie in Movie.objects.all():
            # Construye el nombre de archivo esperado (puedes ajustar esto según tu convención)
            # Ejemplo: m_{title}.png
            # Limpia el título para que coincida con el nombre del archivo
            filename = f"m_{movie.title}.png"
            image_path = os.path.join(images_folder, filename)

            # Si la imagen existe, actualiza la ruta en la base de datos
            if os.path.exists(image_path):
                # Guarda la ruta relativa para el campo de imagen
                movie.img = os.path.relpath(image_path, 'media')
                movie.save()
                updated_count += 1
                self.stdout.write(self.style.SUCCESS(f"Updated image for: {movie.title}"))
            else:
                self.stderr.write(f"Image not found for: {movie.title} (expected: {filename})")

        self.stdout.write(self.style.SUCCESS(f"Finished updating {updated_count} movie images from folder."))
