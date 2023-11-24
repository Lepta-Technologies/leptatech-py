# Copyright 2023 Lepta Technologies
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
import threading

from . import clients
from .config import Config

__all__ = ["Lithium", "Config"]


# This class uses the singleton pattern
class Lithium:
    _client = None
    _config = None
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        # There should only be a single instance of this class
        if cls._instance is None:
            # Ensure thread-safety while initialising
            cls._lock.acquire()
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            cls._lock.release()
        return cls._instance

    @property
    def client(self):
        if self._client is None:
            raise Exception("Lithium must be configured")
        return self._client

    @property
    def config(self):
        if self._config is None:
            raise Exception("Lithium must be configured")
        return self._config

    def _reset(self):
        # This method should only be used during testing
        self._lock.acquire()
        self._client = None
        self._config = None
        self._instance = None
        self._lock.release()

    def configure(self, config):
        # Ensure thread-safety while configuring
        self._lock.acquire()
        if self._config is not None:
            self._lock.release()
            raise Exception("Lithium can only be configured once")
        self._config = config
        # Initialise client
        try:
            client_cls = clients.get_client_cls(self._config.client)
            self._client = client_cls()
            asyncio.get_event_loop().run_until_complete(self._client.initialise(self._config))
        except Exception:
            self._config = None
            self._client = None
            self._lock.release()
            raise
        self._lock.release()

    #
    # Client methods
    #

    async def subscribe_async(self, topic, callback):
        return await self.client.subscribe(topic, callback)
