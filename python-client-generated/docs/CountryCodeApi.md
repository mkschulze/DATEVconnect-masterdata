# swagger_client.CountryCodeApi

All URIs are relative to *http://localhost:58454/datev/api/master-data/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**country_codes_get**](CountryCodeApi.md#country_codes_get) | **GET** /country-codes | Retrieve a list of countries.


# **country_codes_get**
> list[CountryCode] country_codes_get(select=select, filter=filter)

Retrieve a list of countries.

 **Filter**  Unless further parameters are entered, the list will contain all countries.<br><br>  **Filter Options**  The number of results can be limited by using the following filters: - id - name <br>  **Operators** <br> *Filter Option: id, name*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | | contains(property, substring)  | Search for Substring in property's value                       | | startswith(property, substring)| Search for Substring at the beginning of the property's value  | <br>  **Filter Combinations**  Filters can be combined using the operator \"and\".<br><br> 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CountryCodeApi()
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)
filter = 'filter_example' # str | Entering a filter expression influences the number of results.  (optional)

try:
    # Retrieve a list of countries.
    api_response = api_instance.country_codes_get(select=select, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryCodeApi->country_codes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 
 **filter** | **str**| Entering a filter expression influences the number of results.  | [optional] 

### Return type

[**list[CountryCode]**](CountryCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

