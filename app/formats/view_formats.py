#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import Any


class ViewFormats(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def reading(self, data, environ, start_response) -> Any:
        pass
