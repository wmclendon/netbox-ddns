<<<<<<< HEAD
VERSION = '1.2.10'
=======
VERSION = '1.3.0'
>>>>>>> 9c8071bf33dea60827ba749fbf84f6dbf28de5b9

try:
    from netbox.plugins import PluginConfig
except ImportError:
    # Dummy for when importing outside of netbox
    class PluginConfig:
        pass


class NetBoxDDNSConfig(PluginConfig):
    name = 'netbox_ddns'
    verbose_name = 'Dynamic DNS'
    version = VERSION
<<<<<<< HEAD
    min_version = '3.0.0'
    max_version = '3.7.999'
=======
    min_version = '4.0.0'
    max_version = '4.0.999'
>>>>>>> 9c8071bf33dea60827ba749fbf84f6dbf28de5b9
    author = 'Sander Steffann'
    author_email = 'sander@steffann.nl'
    description = 'Dynamic DNS Connector for NetBox'
    base_url = 'ddns'
    required_settings = []
    default_settings = {}

    def ready(self):
        super().ready()

        from . import signals


config = NetBoxDDNSConfig
