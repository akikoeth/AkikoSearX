# SPDX-License-Identifier: AGPL-3.0-or-later
"""Within this module we implement a *demo online engine*.  Do not look to
close to the implementation, its just a simple example which queries `The Art
Institute of Chicago <https://www.artic.edu>`_

To get in use of this *demo* engine add the following entry to your engines
list in ``settings.yml``:

.. code:: yaml

  - name: AkikoLlama
    engine: akikollama
    shortcut: ak
    disabled: false

"""

from json import loads
from urllib.parse import urlencode

engine_type = 'online'
send_accept_language_header = True
categories = ['general']
disabled = True
timeout = 2.0
categories = ['images']
paging = True
page_size = 20

search_api = 'http://127.0.0.1:8080/search?'

about = {
    "website": 'http://akiko.eth',
    "wikidata_id": 'none',
    "official_api_documentation": 'https://github.com/akikoeth/',
    "use_official_api": True,
    "require_api_key": False,
    "results": 'JSON',
}

def request(query, params):
    """Build up the ``params`` for the online request.  In this example we build a
    URL to fetch images from `artic.edu <https://artic.edu>`__

    """
    args = urlencode(
        {
            'query': query,
        }
    )
    params['url'] = search_api + args

    return params


def response(resp):
    """Parse out the result items from the response.  In this example we parse the
    response from `api.artic.edu <https://artic.edu>`__ and filter out all
    images.

    """
    results = []
    json_data = loads(resp.text)

    print("json_data: ", json_data)

    for result in json_data:

        results.append(
            {
                'url': result['url'],
                'title': result['name'],
                'content': result['description'],
                'tvl': result['tvl']
            }
        )

    print(results)
    return results
