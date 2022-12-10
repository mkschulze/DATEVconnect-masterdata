# swagger_client.VersionApi

All URIs are relative to *http://localhost:58454/datev/api/master-data/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version_get**](VersionApi.md#version_get) | **GET** /version | Retrieve meta information (e.g. version information).


# **version_get**
> Version version_get(select=select)

Retrieve meta information (e.g. version information).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionApi()
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)

try:
    # Retrieve meta information (e.g. version information).
    api_response = api_instance.version_get(select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionApi->version_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 

### Return type

[**Version**](Version.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

