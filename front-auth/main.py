# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os, urllib

from flask import Flask, request

import back

app = Flask(__name__)

front_target = os.environ.get('TARGET', 'World')

@app.route('/')
def hello_world():
    return f'Hello from frontend {front_target}\n'

@app.route('/full')
def chain_services():
    backend_data = back.new_request()
    return f'Hello from frontend {front_target} and... {backend_data}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
