from django.contrib.auth.context_processors import PermWrapper
from django.template.context_processors import csrf

from netbox.plugins.templates import PluginTemplateExtension
from . import tables


class ReverseZoneRecreate(PluginTemplateExtension):
    # NetBox up to 4.1
    model = 'netbox_ddns.reversezone'
    # NetBox from 4.2, required to be present as of NetBox 4.3
    models = [model]

    def buttons(self):
        """
        A button to force DNS re-provisioning
        """
        context = {
            'perms': PermWrapper(self.context['request'].user),
        }
        context.update(csrf(self.context['request']))
        return self.render('netbox_ddns/update_reverse_zone.html', context)


class ZoneRecreate(PluginTemplateExtension):
    # NetBox up to 4.1
    model = 'netbox_ddns.zone'
    # NetBox from 4.2, required to be present as of NetBox 4.3
    models = [model]

    def buttons(self):
        """
        A button to force DNS re-provisioning
        """
        context = {
            'perms': PermWrapper(self.context['request'].user),
        }
        context.update(csrf(self.context['request']))
        return self.render('netbox_ddns/update_zone.html', context)


class DNSInfo(PluginTemplateExtension):
    # NetBox up to 4.1
    model = 'ipam.ipaddress'
    # NetBox from 4.2, required to be present as of NetBox 4.3
    models = [model]

    def buttons(self):
        """
        A button to force DNS re-provisioning
        """
        context = {
            'perms': PermWrapper(self.context['request'].user),
        }
        context.update(csrf(self.context['request']))
        return self.render('netbox_ddns/ipaddress/dns_refresh_button.html', context)

    def left_page(self):
        """
        An info-box with the status of the DNS modifications and records
        """
        extra_dns_name_table = tables.ExtraDNSNameTable(list(self.context['object'].extradnsname_set.all()),
                                                        exclude=["id", "ip_address"], orderable=False)

        return (
                self.render('netbox_ddns/ipaddress/dns_info.html') +
                self.render('netbox_ddns/ipaddress/dns_extra.html', {
                    'perms': PermWrapper(self.context['request'].user),
                    'extra_dns_name_table': extra_dns_name_table,
                })
        )


template_extensions = [DNSInfo, ZoneRecreate, ReverseZoneRecreate]
