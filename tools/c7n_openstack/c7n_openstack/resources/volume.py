# Copyright The Cloud Custodian Authors.
# SPDX-License-Identifier: Apache-2.0
#
from c7n_openstack.query import QueryResourceManager, TypeInfo
from c7n_openstack.provider import resources


@resources.register('volume')
class Volume(QueryResourceManager):
    class resource_type(TypeInfo):
        enum_spec = ('list_volumes', None)
        id = 'id'
        name = 'name'
        default_report_fields = ['id', 'name', 'status', 'size']
