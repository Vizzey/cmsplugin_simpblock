from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _

class Simpblock(CMSPlugin):
	imgsrc = models.ImageField(_("Image"), upload_to='simpblock/')
	the_link = models.SlugField(_("Link"))
	the_text = models.TextField(_("Text"))