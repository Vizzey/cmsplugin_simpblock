from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import Simpblock
from django.utils.translation import ugettext as _

class CMSSimpblockPlugin(CMSPluginBase):
	model = Simpblock
	name = _("Simpblock")
	render_template = "simpblock/template1.html"
	
	def render(self, context, instance, placeholder):
		context.update({
				'Simpblock': instance,
					})
		return context


plugin_pool.register_plugin(CMSSimpblockPlugin)

