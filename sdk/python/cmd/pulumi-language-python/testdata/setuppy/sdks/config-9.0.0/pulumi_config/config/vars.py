# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins as _builtins
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities

import types

__config__ = pulumi.Config('config')


class _ExportableConfig(types.ModuleType):
    @_builtins.property
    def name(self) -> Optional[str]:
        return __config__.get('name')

    @_builtins.property
    def plugin_download_url(self) -> Optional[str]:
        return __config__.get('pluginDownloadURL')

