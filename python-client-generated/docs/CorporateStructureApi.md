# swagger_client.CorporateStructureApi

All URIs are relative to *http://localhost:58454/datev/api/master-data/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**corporate_structures_get**](CorporateStructureApi.md#corporate_structures_get) | **GET** /corporate-structures | Retrieve a list of corporate structures.
[**corporate_structures_organization_id_establishments_establishment_id_get**](CorporateStructureApi.md#corporate_structures_organization_id_establishments_establishment_id_get) | **GET** /corporate-structures/{organization-id}/establishments/{establishment-id} | Retrieve a specific establishment.
[**corporate_structures_organization_id_get**](CorporateStructureApi.md#corporate_structures_organization_id_get) | **GET** /corporate-structures/{organization-id} | Retrieve a specific organization.


# **corporate_structures_get**
> list[CorporateStructure] corporate_structures_get(select=select, filter=filter)

Retrieve a list of corporate structures.

 **Filter**  Unless further parameters are entered, the list will contain all corporate structures (all organizations, all establishments, all functional areas).<br><br>  **Filter Options**  The number of results can be limited  by using the following filters: - id - name - number - status - timestamp <br>  **Operators** <br> *Filter Option: name*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | | contains(property, substring)  | Search for Substring in property's value                       | | startswith(property, substring)| Search for Substring at the beginning of the property's value  | <br>  *Filter Option: number, timestamp*  | Operator          | Description                 | |-------------------|-----------------------------| | eq                | Equal                       | | gt                | Greater than                | | ge                | Greater than or equal       | | lt                | Less than                   | | le                | Less than or equal          | <br>  *Filter Option: id, status*  | Operator          | Description                 | |-------------------|-----------------------------| | eq                | Equal                       | <br>  **Filter Combinations**  Filters can be combined using the operator \"and\".<br><br> 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CorporateStructureApi()
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)
filter = 'filter_example' # str | Entering a filter expression influences the number of results.  (optional)

try:
    # Retrieve a list of corporate structures.
    api_response = api_instance.corporate_structures_get(select=select, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporateStructureApi->corporate_structures_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 
 **filter** | **str**| Entering a filter expression influences the number of results.  | [optional] 

### Return type

[**list[CorporateStructure]**](CorporateStructure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporate_structures_organization_id_establishments_establishment_id_get**
> Establishment corporate_structures_organization_id_establishments_establishment_id_get(organization_id, establishment_id, select=select)

Retrieve a specific establishment.

 Retrieving a specific establishment. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CorporateStructureApi()
organization_id = 'organization_id_example' # str | The GUID of an organization.
establishment_id = 'establishment_id_example' # str | The GUID of an establishment.
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)

try:
    # Retrieve a specific establishment.
    api_response = api_instance.corporate_structures_organization_id_establishments_establishment_id_get(organization_id, establishment_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporateStructureApi->corporate_structures_organization_id_establishments_establishment_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The GUID of an organization. | 
 **establishment_id** | **str**| The GUID of an establishment. | 
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 

### Return type

[**Establishment**](Establishment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporate_structures_organization_id_get**
> CorporateStructure corporate_structures_organization_id_get(organization_id, select=select)

Retrieve a specific organization.

 Retrieving a specific organization. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CorporateStructureApi()
organization_id = 'organization_id_example' # str | The GUID of an organization.
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)

try:
    # Retrieve a specific organization.
    api_response = api_instance.corporate_structures_organization_id_get(organization_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CorporateStructureApi->corporate_structures_organization_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The GUID of an organization. | 
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 

### Return type

[**CorporateStructure**](CorporateStructure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

