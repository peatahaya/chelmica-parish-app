from django.db import models

class ParishProfile(models.Model):
    """
    Model profilu parafii (Single-tenant).
    Przechowuje dane kontaktowe oraz ustawienia wizualne dla frontendu Next.js.
    """
    name = models.CharField(max_length=255, verbose_name="Nazwa Parafii")
    description = models.TextField(verbose_name="Opis (Rich Text)", blank=True)
    address = models.TextField(verbose_name="Adres")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    email = models.EmailField(verbose_name="Email")
    
    # Luxury Dark Mode UI configuration
    primary_color = models.CharField(max_length=7, default="#D4AF37", help_text="HEX gold color")
    secondary_color = models.CharField(max_length=7, default="#1F1F1F", help_text="HEX secondary color")
    background_color = models.CharField(max_length=7, default="#121212", help_text="HEX dark background")
    logo_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Profil Parafii"
        verbose_name_plural = "Profile Parafii"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Zapewnia, że istnieje tylko jeden rekord profilu."""
        if not self.pk and ParishProfile.objects.exists():
            return # Można rzucić błąd, ale tutaj po prostu blokujemy stworzenie drugiego
        super(ParishProfile, self).save(*args, **kwargs)
