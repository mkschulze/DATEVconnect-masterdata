# swagger_client.InstitutionApi

All URIs are relative to *http://localhost:58454/datev/api/master-data/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**banks_get**](InstitutionApi.md#banks_get) | **GET** /banks | Retrieve a list of banks.
[**tax_authorities_get**](InstitutionApi.md#tax_authorities_get) | **GET** /tax-authorities | Retrieve a list of tax authorities.


# **banks_get**
> list[Bank] banks_get(select=select, filter=filter)

Retrieve a list of banks.

 **Filter**  Unless further parameters are entered, the list will contain all banks.<br><br>  **Filter Options**  The number of results can be limited by using the following filters: - id - bank_code - bic - city - country_code - name - standard - timestamp <br>  **Operators** <br> *Filter Option: timestamp*  | Operator          | Description               | |-------------------|---------------------------| | eq                | Equal                     | | gt                | Greater than              | | ge                | Greater than or equal     | | lt                | Less than                 | | le                | Less than or equal        |  <br>  *Filter Option: bank_code, bic, city, name*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | | contains(property, substring)  | Search for Substring in property's value                       | | startswith(property, substring)| Search for Substring at the beginning of the property's value  |  <br>  *Filter Option: id, country_code, standard*  | Operator                       | Description  | |--------------------------------|--------------| | eq                             | Equal        |  <br>  **Filter Combinations**  Filters can be combined using the operator \"and\".<br><br> 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InstitutionApi()
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)
filter = 'filter_example' # str | Entering a filter expression influences the number of results.  (optional)

try:
    # Retrieve a list of banks.
    api_response = api_instance.banks_get(select=select, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionApi->banks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 
 **filter** | **str**| Entering a filter expression influences the number of results.  | [optional] 

### Return type

[**list[Bank]**](Bank.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_authorities_get**
> list[TaxAuthority] tax_authorities_get(select=select, filter=filter)

Retrieve a list of tax authorities.

 **Filter**  Unless further parameters are entered, the list will contain all tax authorities.<br><br>  **Filter Options**  The number of results can be limited by using the following filters: - id - city - country_code - name - number - standard - timestamp <br>  **Operators** <br> *Filter Option: number, timestamp*  | Operator          | Description               | |-------------------|---------------------------| | eq                | Equal                     | | gt                | Greater than              | | ge                | Greater than or equal     | | lt                | Less than                 | | le                | Less than or equal        |  <br>  *Filter Option: city, name*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | | contains(property, substring)  | Search for Substring in property's value                       | | startswith(property, substring)| Search for Substring at the beginning of the property's value  |  <br>  *Filter Option: id, country_code, standard*  | Operator                       | Description  | |--------------------------------|--------------| | eq                             | Equal        |  <br>  **Filter Combinations**  Filters can be combined using the operator \"and\".<br><br> 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InstitutionApi()
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)
filter = 'filter_example' # str | Entering a filter expression influences the number of results.  (optional)

try:
    # Retrieve a list of tax authorities.
    api_response = api_instance.tax_authorities_get(select=select, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionApi->tax_authorities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 
 **filter** | **str**| Entering a filter expression influences the number of results.  | [optional] 

### Return type

[**list[TaxAuthority]**](TaxAuthority.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

