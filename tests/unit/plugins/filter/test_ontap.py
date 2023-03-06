from __future__ import absolute_import, division, print_function
__metaclass__ = type

import pytest

from ansible.module_utils._text import to_native
from ansible.plugins.filter.core import to_uuid
from ansible.errors import AnsibleFilterError

# TODO: Write tests...