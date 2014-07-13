from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _

class Simpblock(CMSPlugin):
	imgsrc = models.ImageField(_("Image"), upload_to='simpblock/')
	the_title = models.CharField(_("Title"))
	the_link = models.CharField(_("Link"))
	the_text = models.TextField(_("Text"))