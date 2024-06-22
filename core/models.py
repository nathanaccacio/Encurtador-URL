from django.db import models

class Links(models.Model):
    #Link para onde a pessoa será redirecionada
    #URLField() faz uma verificação de links
    link_redirecionado = models.URLField()
    # Este é o link compactado
    # O código do link terá no máximo 8 caracteres
    link_encurtado = models.CharField(max_length=8, unique=True)
    
    def __str__(self) -> str:
        return self.link_encurtado