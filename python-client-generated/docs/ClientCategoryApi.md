# swagger_client.ClientCategoryApi

All URIs are relative to *http://localhost:58454/datev/api/master-data/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_categories_get**](ClientCategoryApi.md#client_categories_get) | **GET** /client-categories | Retrieve a list of client category assignments.
[**client_category_types_client_category_type_id_get**](ClientCategoryApi.md#client_category_types_client_category_type_id_get) | **GET** /client-category-types/{client-category-type-id} | Retrieve a specific client category type.
[**client_category_types_client_category_type_id_put**](ClientCategoryApi.md#client_category_types_client_category_type_id_put) | **PUT** /client-category-types/{client-category-type-id} | Update a spezific client category type.
[**client_category_types_get**](ClientCategoryApi.md#client_category_types_get) | **GET** /client-category-types | Retrieve a list of client category types.
[**client_category_types_post**](ClientCategoryApi.md#client_category_types_post) | **POST** /client-category-types | Creating a new client category type.
[**clients_client_id_client_categories_get**](ClientCategoryApi.md#clients_client_id_client_categories_get) | **GET** /clients/{client-id}/client-categories | Retrieve a list of client category assignments for a specific client.
[**clients_client_id_client_categories_put**](ClientCategoryApi.md#clients_client_id_client_categories_put) | **PUT** /clients/{client-id}/client-categories | Update the client category assignments for a specific client.


# **client_categories_get**
> list[ClientCategory] client_categories_get(select=select, filter=filter)

Retrieve a list of client category assignments.

 Only relevant if the package 'Eigenorganisation comfort' is installed.  **Filter** Unless further parameters are entered, the list will contain the client category assignments for active and inactive clients.<br><br>  **Filter Options**  The number of results can be limited by using the following filters: - client_category_type_id - client_category_type_short_name - client_id - client_name - client_number - client_status - timestamp <br>  **Operators** <br>  *Filter Option: client_number, timestamp*  | Operator          | Description                                     | |-------------------|-------------------------------------------------| | eq                | Equal                                           | | gt                | Greater than                                    | | ge                | Greater than or equal                           | | lt                | Less than                                       | | le                | Less than or equal                              | <br>   *Filter Option: client_category_type_short_name, client_name*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | | contains(property, substring)  | Search for Substring in property's value                       | | startswith(property, substring)| Search for Substring at the beginning of the property's value  | <br>   *Filter Option: client_id, client_status, client_category_type_id*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | <br>  **Filter Combinations**  Filters can be combined using the operator \"and\".<br><br> 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientCategoryApi()
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)
filter = 'filter_example' # str | Entering a filter expression influences the number of results.  (optional)

try:
    # Retrieve a list of client category assignments.
    api_response = api_instance.client_categories_get(select=select, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientCategoryApi->client_categories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 
 **filter** | **str**| Entering a filter expression influences the number of results.  | [optional] 

### Return type

[**list[ClientCategory]**](ClientCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_category_types_client_category_type_id_get**
> ClientCategoryType client_category_types_client_category_type_id_get(client_category_type_id, select=select)

Retrieve a specific client category type.

 Retrieving a specific client category type.<br> Only relevant if the package 'Eigenorganisation comfort' is installed. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientCategoryApi()
client_category_type_id = 'client_category_type_id_example' # str | The GUID of a client categorie type.
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)

try:
    # Retrieve a specific client category type.
    api_response = api_instance.client_category_types_client_category_type_id_get(client_category_type_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientCategoryApi->client_category_types_client_category_type_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_category_type_id** | **str**| The GUID of a client categorie type. | 
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 

### Return type

[**ClientCategoryType**](ClientCategoryType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_category_types_client_category_type_id_put**
> client_category_types_client_category_type_id_put(client_category_type_id, client_category_type)

Update a spezific client category type.

Only relevant if the package 'Eigenorganisation comfort' is installed.<br> Updating a spezific client category type.  The following property may not be changed: - id 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientCategoryApi()
client_category_type_id = 'client_category_type_id_example' # str | The GUID of a client categorie type.
client_category_type = swagger_client.ClientCategoryType() # ClientCategoryType | Client category type object

try:
    # Update a spezific client category type.
    api_instance.client_category_types_client_category_type_id_put(client_category_type_id, client_category_type)
except ApiException as e:
    print("Exception when calling ClientCategoryApi->client_category_types_client_category_type_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_category_type_id** | **str**| The GUID of a client categorie type. | 
 **client_category_type** | [**ClientCategoryType**](ClientCategoryType.md)| Client category type object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_category_types_get**
> list[ClientCategoryType] client_category_types_get(select=select, filter=filter)

Retrieve a list of client category types.

 Only relevant if the package 'Eigenorganisation comfort' is installed.<br>  **Filter** Unless further parameters are entered, the list will contain all client category types.<br><br>  **Filter Options**  The number of results can be limited by using the following filters: - short_name - name - timestamp <br>  **Operators** <br>  *Filter Option: name, short_name*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | | contains(property, substring)  | Search for Substring in property's value                       | | startswith(property, substring)| Search for Substring at the beginning of the property's value  | <br>  *Filter Option: timestamp*  | Operator          | Description                                     | |-------------------|-------------------------------------------------| | eq                | Equal                                           | | gt                | Greater than                                    | | ge                | Greater than or equal                           | | lt                | Less than                                       | | le                | Less than or equal                              | <br>   **Filter Combinations**  Filters can be combined using the operator \"and\".<br><br> 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientCategoryApi()
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)
filter = 'filter_example' # str | Entering a filter expression influences the number of results.  (optional)

try:
    # Retrieve a list of client category types.
    api_response = api_instance.client_category_types_get(select=select, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientCategoryApi->client_category_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 
 **filter** | **str**| Entering a filter expression influences the number of results.  | [optional] 

### Return type

[**list[ClientCategoryType]**](ClientCategoryType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_category_types_post**
> client_category_types_post(new_client_category)

Creating a new client category type.

 Only relevant if the package 'Eigenorganisation comfort' is installed. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientCategoryApi()
new_client_category = swagger_client.ClientCategoryType() # ClientCategoryType | 

try:
    # Creating a new client category type.
    api_instance.client_category_types_post(new_client_category)
except ApiException as e:
    print("Exception when calling ClientCategoryApi->client_category_types_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_client_category** | [**ClientCategoryType**](ClientCategoryType.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_client_id_client_categories_get**
> list[ClientCategory] clients_client_id_client_categories_get(client_id, select=select)

Retrieve a list of client category assignments for a specific client.

 Retrieving the list of client category assignments for a specific client.<br> Only relevant if the package 'Eigenorganisation comfort' is installed. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientCategoryApi()
client_id = 'client_id_example' # str | The GUID of a client.
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)

try:
    # Retrieve a list of client category assignments for a specific client.
    api_response = api_instance.clients_client_id_client_categories_get(client_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientCategoryApi->clients_client_id_client_categories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The GUID of a client. | 
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 

### Return type

[**list[ClientCategory]**](ClientCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_client_id_client_categories_put**
> clients_client_id_client_categories_put(client_id, client_category)

Update the client category assignments for a specific client.

 Only relevant if the package 'Eigenorganisation comfort' is installed.<br> With the PUT command, the client category assignments for a specific client will be completely overwritten. We therefore recommend that you perform a request of the client category assignments for a specific client being updated beforehand in order to prevent master data from being overwrittten.<br><br>  The following property may not be changed: - client_id  If you would create a client category assignment, which was not yet defined for the client, you must create a new GUID for the property 'id'.<br><br> 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientCategoryApi()
client_id = 'client_id_example' # str | The GUID of a client.
client_category = [swagger_client.ClientCategory()] # list[ClientCategory] | Client category object

try:
    # Update the client category assignments for a specific client.
    api_instance.clients_client_id_client_categories_put(client_id, client_category)
except ApiException as e:
    print("Exception when calling ClientCategoryApi->clients_client_id_client_categories_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The GUID of a client. | 
 **client_category** | [**list[ClientCategory]**](ClientCategory.md)| Client category object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

