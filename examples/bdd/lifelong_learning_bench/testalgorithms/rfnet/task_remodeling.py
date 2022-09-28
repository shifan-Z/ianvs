# Copyright 2021 The KubeEdge Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Remodeling tasks based on their relationships

Parameters
----------
mappings ：all assigned tasks get from the `task_mining`
samples : input samples

Returns
-------
models : List of groups which including at least 1 task.
"""

from typing import List

import numpy as np
import pandas as pd

from sedna.datasources import BaseDataSource
from sedna.common.class_factory import ClassFactory, ClassType

__all__ = ('DefaultTaskRemodeling',)


@ClassFactory.register(ClassType.STP, alias="TaskRemodeling")
class TaskRemodeling:
    """
    Assume that each task is independent of each other
    """

    def __init__(self, models: list, **kwargs):
        self.models = models

    def __call__(self, samples: BaseDataSource, mappings: List):
        """
        Grouping based on assigned tasks
        """
        mappings = np.array(mappings)
        data, models = samples, []
        for m in mappings:
            try:
                model = self.models[m]
            except Exception as err:
                print(f"self.models[{m}] not exists. {err}")
                model = self.models[0]
            models.append(model)
        return data, models
