from datetime import datetime
from io import StringIO
from typing import TextIO, Dict, List, Union

from pianosdk.api_response import ApiResponse
from pianosdk.base_api import BaseApi
from pianosdk.configuration import Configuration
from pianosdk.httpwrap import HttpCallBack
from pianosdk.utils import _json_deserialize, _encode_parameter
from pianosdk.publisher.models.term_conversion import TermConversion


class PublisherConversionCustomApi(BaseApi):
    def __init__(self, config: Configuration, http_callback: HttpCallBack = None) -> None:
        super().__init__(config, http_callback)

    def custom_create(self, aid: str, term_id: str, uid: str, access_period: int = None, unlimited_access: bool = False, extend_existing: bool = True) -> ApiResponse[TermConversion]:
        _url_path = '/api/v3/publisher/conversion/custom/create'
        _query_url = self.config.get_base_url() + _url_path
        _query_parameters = {

        }

        _headers = {
            'api_token': self.config.api_token,
            'Accept': 'application/json'
        }

        _parameters = {
            'aid': _encode_parameter(aid),
            'term_id': _encode_parameter(term_id),
            'uid': _encode_parameter(uid),
            'access_period': _encode_parameter(access_period),
            'unlimited_access': _encode_parameter(unlimited_access),
            'extend_existing': _encode_parameter(extend_existing)
        }

        _body = None
        _files = None

        _request = self.config.http_client.build_request('POST',
                                                         _query_url,
                                                         headers=_headers,
                                                         query_parameters=_query_parameters,
                                                         parameters=_parameters,
                                                         json=_body,
                                                         files=_files)
        _response = self._execute_request(_request)
        _result = _json_deserialize(_response, TermConversion)
        return _result

