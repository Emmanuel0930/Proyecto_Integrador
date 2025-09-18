import random
import numpy as np
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
	help = "Muestra los embeddings de una película seleccionada al azar"

	def handle(self, *args, **kwargs):
		count = Movie.objects.count()
		if count == 0:
			self.stdout.write(self.style.ERROR("No hay películas en la base de datos."))
			return
		idx = random.randint(0, count - 1)
		movie = Movie.objects.all()[idx]
		self.stdout.write(self.style.SUCCESS(f"Película seleccionada: {movie.title}"))
		# Decodificar el embedding
		emb_array = np.frombuffer(movie.emb, dtype=np.float64)
		self.stdout.write(f"Embedding shape: {emb_array.shape}")
		self.stdout.write(f"Embedding (primeros 50 valores): {emb_array[:50]}")
