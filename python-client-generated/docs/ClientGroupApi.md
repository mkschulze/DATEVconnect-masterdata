# swagger_client.ClientGroupApi

All URIs are relative to *http://localhost:58454/datev/api/master-data/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_group_types_client_group_type_id_get**](ClientGroupApi.md#client_group_types_client_group_type_id_get) | **GET** /client-group-types/{client-group-type-id} | Retrieve a specific client group type.
[**client_group_types_client_group_type_id_put**](ClientGroupApi.md#client_group_types_client_group_type_id_put) | **PUT** /client-group-types/{client-group-type-id} | Update a spezific client group type.
[**client_group_types_get**](ClientGroupApi.md#client_group_types_get) | **GET** /client-group-types | Retrieve a list of client group types.
[**client_group_types_post**](ClientGroupApi.md#client_group_types_post) | **POST** /client-group-types | Creating a new client group type.
[**client_groups_get**](ClientGroupApi.md#client_groups_get) | **GET** /client-groups | Retrieve a list of client group assignments.
[**clients_client_id_client_groups_get**](ClientGroupApi.md#clients_client_id_client_groups_get) | **GET** /clients/{client-id}/client-groups | Retrieve the client group assignment for a specific client.
[**clients_client_id_client_groups_put**](ClientGroupApi.md#clients_client_id_client_groups_put) | **PUT** /clients/{client-id}/client-groups | Update the client group assignment for a specific client.


# **client_group_types_client_group_type_id_get**
> ClientGroupType client_group_types_client_group_type_id_get(client_group_type_id, select=select)

Retrieve a specific client group type.

 Retrieving a specific client group type.<br> Only relevant if the package 'Eigenorganisation comfort' is installed. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientGroupApi()
client_group_type_id = 'client_group_type_id_example' # str | The GUID of a client group type.
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)

try:
    # Retrieve a specific client group type.
    api_response = api_instance.client_group_types_client_group_type_id_get(client_group_type_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientGroupApi->client_group_types_client_group_type_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_group_type_id** | **str**| The GUID of a client group type. | 
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 

### Return type

[**ClientGroupType**](ClientGroupType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_group_types_client_group_type_id_put**
> client_group_types_client_group_type_id_put(client_group_type_id, client_group_type)

Update a spezific client group type.

Only relevant if the package 'Eigenorganisation comfort' is installed.<br> Updating a spezific client group type.  The following property may not be changed: - id 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientGroupApi()
client_group_type_id = 'client_group_type_id_example' # str | The GUID of a client group type.
client_group_type = swagger_client.ClientGroupType() # ClientGroupType | Client group type object

try:
    # Update a spezific client group type.
    api_instance.client_group_types_client_group_type_id_put(client_group_type_id, client_group_type)
except ApiException as e:
    print("Exception when calling ClientGroupApi->client_group_types_client_group_type_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_group_type_id** | **str**| The GUID of a client group type. | 
 **client_group_type** | [**ClientGroupType**](ClientGroupType.md)| Client group type object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_group_types_get**
> list[ClientGroupType] client_group_types_get(select=select, filter=filter)

Retrieve a list of client group types.

 Only relevant if the package 'Eigenorganisation comfort' is installed.  **Filter** Unless further parameters are entered, the list will contain all client group types.<br><br>  **Filter Options**  The number of results can be limited by using the following filters: - short_name - name - timestamp <br>  **Operators** <br>  *Filter Option: name, short_name*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | | contains(property, substring)  | Search for Substring in property's value                       | | startswith(property, substring)| Search for Substring at the beginning of the property's value  | <br>  *Filter Option: timestamp*  | Operator          | Description                                     | |-------------------|-------------------------------------------------| | eq                | Equal                                           | | gt                | Greater than                                    | | ge                | Greater than or equal                           | | lt                | Less than                                       | | le                | Less than or equal                              | <br>   **Filter Combinations**  Filters can be combined using the operator \"and\".<br><br> 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientGroupApi()
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)
filter = 'filter_example' # str | Entering a filter expression influences the number of results.  (optional)

try:
    # Retrieve a list of client group types.
    api_response = api_instance.client_group_types_get(select=select, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientGroupApi->client_group_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 
 **filter** | **str**| Entering a filter expression influences the number of results.  | [optional] 

### Return type

[**list[ClientGroupType]**](ClientGroupType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_group_types_post**
> client_group_types_post(new_client_group)

Creating a new client group type.

 Only relevant if the package 'Eigenorganisation comfort' is installed. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientGroupApi()
new_client_group = swagger_client.ClientGroupType() # ClientGroupType | 

try:
    # Creating a new client group type.
    api_instance.client_group_types_post(new_client_group)
except ApiException as e:
    print("Exception when calling ClientGroupApi->client_group_types_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_client_group** | [**ClientGroupType**](ClientGroupType.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_groups_get**
> list[ClientGroup] client_groups_get(select=select, filter=filter)

Retrieve a list of client group assignments.

 Only relevant if the package 'Eigenorganisation comfort' is installed.<br>  **Filter** Unless further parameters are entered, the list will contain the client group assignments for active and inactive clients.<br><br>  **Filter Options**  The number of results can be limited by using the following filters: - client_group_type_id - client_group_type_short_name - client_id - client_name - client_number - client_status - timestamp <br>  **Operators** <br>  *Filter Option: client_number, timestamp*  | Operator          | Description                                     | |-------------------|-------------------------------------------------| | eq                | Equal                                           | | gt                | Greater than                                    | | ge                | Greater than or equal                           | | lt                | Less than                                       | | le                | Less than or equal                              | <br>   *Filter Option: client_group_type_short_name, client_name*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | | contains(property, substring)  | Search for Substring in property's value                       | | startswith(property, substring)| Search for Substring at the beginning of the property's value  | <br>   *Filter Option: client_id, client_status, client_group_type_id*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | <br>  **Filter Combinations**  Filters can be combined using the operator \"and\".<br><br> 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientGroupApi()
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)
filter = 'filter_example' # str | Entering a filter expression influences the number of results.  (optional)

try:
    # Retrieve a list of client group assignments.
    api_response = api_instance.client_groups_get(select=select, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientGroupApi->client_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 
 **filter** | **str**| Entering a filter expression influences the number of results.  | [optional] 

### Return type

[**list[ClientGroup]**](ClientGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_client_id_client_groups_get**
> list[ClientGroup] clients_client_id_client_groups_get(client_id, select=select)

Retrieve the client group assignment for a specific client.

 Retrieving the client group assignment for a specific client.<br> Only relevant if the package 'Eigenorganisation comfort' is installed. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientGroupApi()
client_id = 'client_id_example' # str | The GUID of a client.
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)

try:
    # Retrieve the client group assignment for a specific client.
    api_response = api_instance.clients_client_id_client_groups_get(client_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientGroupApi->clients_client_id_client_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The GUID of a client. | 
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 

### Return type

[**list[ClientGroup]**](ClientGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_client_id_client_groups_put**
> clients_client_id_client_groups_put(client_id, client_category)

Update the client group assignment for a specific client.

 Only relevant if the package 'Eigenorganisation comfort' is installed.<br>   Updating the client group assignment for a specific client.<br><br>  The following property may not be changed: - client_id  If you would create a client group assignment, which was not yet defined for the client, you must create a new GUID for the property 'id'.<br><br> 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientGroupApi()
client_id = 'client_id_example' # str | The GUID of a client.
client_category = [swagger_client.ClientGroup()] # list[ClientGroup] | Client group object

try:
    # Update the client group assignment for a specific client.
    api_instance.clients_client_id_client_groups_put(client_id, client_category)
except ApiException as e:
    print("Exception when calling ClientGroupApi->clients_client_id_client_groups_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The GUID of a client. | 
 **client_category** | [**list[ClientGroup]**](ClientGroup.md)| Client group object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

