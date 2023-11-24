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

class Config:

    def __init__(self, client, endpoint):
        self._client = client
        self._endpoint = endpoint

    @property
    def client(self):
        return self._client

    @property
    def endpoint(self):
        return self._endpoint

    @classmethod
    def from_json(cls, json):
        return cls(json["client"], json["endpoint"])
