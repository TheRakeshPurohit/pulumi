# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins as _builtins
from . import _utilities
import typing
# Export this package's modules as members:
from .provider import *
from .string import *
_utilities.register(
    resource_modules="""
[
 {
  "pkg": "large",
  "mod": "index",
  "fqn": "pulumi_large",
  "classes": {
   "large:index:String": "String"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "large",
  "token": "pulumi:providers:large",
  "fqn": "pulumi_large",
  "class": "Provider"
 }
]
"""
)
