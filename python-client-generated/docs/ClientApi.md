# swagger_client.ClientApi

All URIs are relative to *http://localhost:58454/datev/api/master-data/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clients_client_id_client_categories_get**](ClientApi.md#clients_client_id_client_categories_get) | **GET** /clients/{client-id}/client-categories | Retrieve a list of client category assignments for a specific client.
[**clients_client_id_client_categories_put**](ClientApi.md#clients_client_id_client_categories_put) | **PUT** /clients/{client-id}/client-categories | Update the client category assignments for a specific client.
[**clients_client_id_client_groups_get**](ClientApi.md#clients_client_id_client_groups_get) | **GET** /clients/{client-id}/client-groups | Retrieve the client group assignment for a specific client.
[**clients_client_id_client_groups_put**](ClientApi.md#clients_client_id_client_groups_put) | **PUT** /clients/{client-id}/client-groups | Update the client group assignment for a specific client.
[**clients_client_id_get**](ClientApi.md#clients_client_id_get) | **GET** /clients/{client-id} | Retrieve a specific client.
[**clients_client_id_put**](ClientApi.md#clients_client_id_put) | **PUT** /clients/{client-id} | Update a specific client.
[**clients_client_id_responsibilities_get**](ClientApi.md#clients_client_id_responsibilities_get) | **GET** /clients/{client-id}/responsibilities | Retrieve a list of responsibilities for a specific client.
[**clients_client_id_responsibilities_put**](ClientApi.md#clients_client_id_responsibilities_put) | **PUT** /clients/{client-id}/responsibilities | Update the responsibilities for a specific client.
[**clients_deletion_log_get**](ClientApi.md#clients_deletion_log_get) | **GET** /clients/deletion-log | Retrieve a list of deleted clients.
[**clients_get**](ClientApi.md#clients_get) | **GET** /clients | Retrieve a list of clients.
[**clients_next_free_number_get**](ClientApi.md#clients_next_free_number_get) | **GET** /clients/next-free-number | Retrieve the next available client number.
[**clients_post**](ClientApi.md#clients_post) | **POST** /clients | Creating a new client.


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
api_instance = swagger_client.ClientApi()
client_id = 'client_id_example' # str | The GUID of a client.
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)

try:
    # Retrieve a list of client category assignments for a specific client.
    api_response = api_instance.clients_client_id_client_categories_get(client_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->clients_client_id_client_categories_get: %s\n" % e)
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
api_instance = swagger_client.ClientApi()
client_id = 'client_id_example' # str | The GUID of a client.
client_category = [swagger_client.ClientCategory()] # list[ClientCategory] | Client category object

try:
    # Update the client category assignments for a specific client.
    api_instance.clients_client_id_client_categories_put(client_id, client_category)
except ApiException as e:
    print("Exception when calling ClientApi->clients_client_id_client_categories_put: %s\n" % e)
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
api_instance = swagger_client.ClientApi()
client_id = 'client_id_example' # str | The GUID of a client.
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)

try:
    # Retrieve the client group assignment for a specific client.
    api_response = api_instance.clients_client_id_client_groups_get(client_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->clients_client_id_client_groups_get: %s\n" % e)
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
api_instance = swagger_client.ClientApi()
client_id = 'client_id_example' # str | The GUID of a client.
client_category = [swagger_client.ClientGroup()] # list[ClientGroup] | Client group object

try:
    # Update the client group assignment for a specific client.
    api_instance.clients_client_id_client_groups_put(client_id, client_category)
except ApiException as e:
    print("Exception when calling ClientApi->clients_client_id_client_groups_put: %s\n" % e)
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

# **clients_client_id_get**
> Client clients_client_id_get(client_id, select=select)

Retrieve a specific client.

 Retrieving a specific client. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientApi()
client_id = 'client_id_example' # str | The GUID of a client.
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)

try:
    # Retrieve a specific client.
    api_response = api_instance.clients_client_id_get(client_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->clients_client_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The GUID of a client. | 
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 

### Return type

[**Client**](Client.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_client_id_put**
> clients_client_id_put(client_id, client)

Update a specific client.

With the PUT command, the client will be completely overwritten. We therefore recommend that you perform a request of the client being updated beforehand in order to prevent master data from being overwritten.<br><br>  The following properties may not be changed: - id - legal_person_id - natural_person_id - number - status - type 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientApi()
client_id = 'client_id_example' # str | The GUID of a client.
client = swagger_client.Client() # Client | Client object

try:
    # Update a specific client.
    api_instance.clients_client_id_put(client_id, client)
except ApiException as e:
    print("Exception when calling ClientApi->clients_client_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The GUID of a client. | 
 **client** | [**Client**](Client.md)| Client object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_client_id_responsibilities_get**
> list[Responsibility] clients_client_id_responsibilities_get(client_id, select=select)

Retrieve a list of responsibilities for a specific client.

 Retrieving the list of responsibilities for a specific client. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientApi()
client_id = 'client_id_example' # str | The GUID of a client.
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)

try:
    # Retrieve a list of responsibilities for a specific client.
    api_response = api_instance.clients_client_id_responsibilities_get(client_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->clients_client_id_responsibilities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The GUID of a client. | 
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 

### Return type

[**list[Responsibility]**](Responsibility.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_client_id_responsibilities_put**
> clients_client_id_responsibilities_put(client_id, responsibility)

Update the responsibilities for a specific client.

With the PUT command, the responsibilities for a specific client will be completely overwritten. We therefore recommend that you perform a request of the resonsibilities for a specifc client being updated beforehand in order to prevent master data from being overwritten.<br><br>  The following properties may not be changed: - client_id - client_number  If you would create a responsibility, which was not yet defined for the client, you must enter a value for the property 'id'. This id must be unique within the responsibilities of the client.<br><br>  *Example:*<br> The responsibilities 'Anlagenbuchführung' and 'Bescheidprüfung' are defined for the client:<br> [  {   \"area_of_responsibility_id\": \"AB\",   \"employee_number\": 1000,   \"id\": 345  },  {   \"area_of_responsibility_id\": \"BP\",   \"employee_number\": 1000,   \"id\": 346  } ]<br> If you want create the responsibility 'Mandatsverantwortung' for the client, the following request body is required:<br> [  {   \"area_of_responsibility_id\": \"AB\",   \"employee_number\": 1000,   \"id\": 345  },  {   \"area_of_responsibility_id\": \"BP\",   \"employee_number\": 1000,   \"id\": 346  },  {   \"area_of_responsibility_id\": \"MV\",   \"employee_number\": 1000,   \"id\": **347**  } ]<br><br>  *Note:* Instead of the property 'employee_number' you can specify the property 'employee_id'. If both properties are specified, the content must match. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientApi()
client_id = 'client_id_example' # str | The GUID of a client.
responsibility = [swagger_client.Responsibility()] # list[Responsibility] | Responsibility object

try:
    # Update the responsibilities for a specific client.
    api_instance.clients_client_id_responsibilities_put(client_id, responsibility)
except ApiException as e:
    print("Exception when calling ClientApi->clients_client_id_responsibilities_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The GUID of a client. | 
 **responsibility** | [**list[Responsibility]**](Responsibility.md)| Responsibility object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_deletion_log_get**
> list[DeletionLog] clients_deletion_log_get(select=select, filter=filter)

Retrieve a list of deleted clients.

**Filter** Unless a filter is entered, the list will contain all deleted clients. The \"timestamp\" filter option can be used to limit the results to a specific time period.<br><br>  **Filter Options**  The number of results can be limited by using the following filters: - id - timestamp <br>  **Operators** <br>  *Filter Option: timestamp*  | Operator          | Description                 | |-------------------|-----------------------------| | eq                | Equal                       | | gt                | Greater than                | | ge                | Greater than or equal       | | lt                | Less than                   | | le                | Less than or equal          |  <br>  *Filter Option: id*  | Operator                       | Description    | |--------------------------------|----------------| | eq                             | Equal          |  <br>  **Filter Combinations**  Filters can be combined using the operator \"and\".<br><br>  **URI Examples**  *Retrieving deleted clients who were deleted after 03/31/2018.*      .../clients/deletion-log?filter=timestamp gt 2018-03-31T00:00:00.000<br><br>            

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientApi()
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)
filter = 'filter_example' # str | Entering a filter expression influences the number of results.  (optional)

try:
    # Retrieve a list of deleted clients.
    api_response = api_instance.clients_deletion_log_get(select=select, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->clients_deletion_log_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 
 **filter** | **str**| Entering a filter expression influences the number of results.  | [optional] 

### Return type

[**list[DeletionLog]**](DeletionLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_get**
> list[Client] clients_get(select=select, filter=filter)

Retrieve a list of clients.

**Filter** Unless further parameters are entered, the list will contain both active and inactive clients.<br><br>  **Filter Options**  The number of results can be limited  by using the following filters: - name - number - status - timestamp - type - natural_person_id - legal_person_id - organization_id - organization_name - organization_number - establishment_id - establishment_name - establishment_number - establishment_short_name - functional_area_id - functional_area_name - functional_area_short_name <br>  **Operators** <br>  *Filter Option: number, timestamp, organization_number, establishment_number*  | Operator          | Description                 | |-------------------|-----------------------------| | eq                | Equal                       | | gt                | Greater than                | | ge                | Greater than or equal       | | lt                | Less than                   | | le                | Less than or equal          |  <br>  *Filter Option: name, organization_name, establishment_name, establishment_short_name, functional_area_name, functional_area_short_name*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | | contains(property, substring)  | Search for Substring in property's value                       | | startswith(property, substring)| Search for Substring at the beginning of the property's value  |  <br>  *Filter Option: status, type, organization_id, establishment_id, functional_area_id, natural_person_id, legal_person_id*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          |  <br>  **Filter Combinations**  Filters can be combined using the operator \"and\".<br><br>  **URI Examples**  *Retrieving a client with the client number 20000*      .../clients?filter=number eq 20000<br><br>  *Retrieving all clients whose client number is greater than or equal to 10000 and less than 70000*       .../clients?filter=number ge 20000 and number lt 70000<br><br>  *Retrieving all clients whose name contains the word \"Mustermeier\"*      .../clients?filter=contains(name, Mustermeier)<br><br>  *Retrieving all active clients*      .../clients?filter=status eq active            

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientApi()
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)
filter = 'filter_example' # str | Entering a filter expression influences the number of results.  (optional)

try:
    # Retrieve a list of clients.
    api_response = api_instance.clients_get(select=select, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->clients_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 
 **filter** | **str**| Entering a filter expression influences the number of results.  | [optional] 

### Return type

[**list[Client]**](Client.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_next_free_number_get**
> NextFreeNumber clients_next_free_number_get(start, range=range)

Retrieve the next available client number.

 When the parameter **start** is included in the URI, the starting point will be defined from which a search for the next available client number will be performed. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientApi()
start = 789 # int | This parameter sets the client number from which a search for the next available client number will be started. 
range = 789 # int | This parameter sets the range within which a search for the next available client number will be performed. If the parameter is not entered, then the default is 1000. If, for example, the \"start\" parameter is set to 10000 and the \"range\" parameter to 20000, then a search for the next available client number will be performed in the client number range from 10000 to 30000.  (optional)

try:
    # Retrieve the next available client number.
    api_response = api_instance.clients_next_free_number_get(start, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->clients_next_free_number_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| This parameter sets the client number from which a search for the next available client number will be started.  | 
 **range** | **int**| This parameter sets the range within which a search for the next available client number will be performed. If the parameter is not entered, then the default is 1000. If, for example, the \&quot;start\&quot; parameter is set to 10000 and the \&quot;range\&quot; parameter to 20000, then a search for the next available client number will be performed in the client number range from 10000 to 30000.  | [optional] 

### Return type

[**NextFreeNumber**](NextFreeNumber.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_post**
> clients_post(new_client, max_number=max_number)

Creating a new client.

 When creating a new client, please note that the addressee (POST /addressees) has to be created first, followed by the client (POST /clients). The property \"legal_person_id\" or \"natural_person_id\" must be completed in accordance with the property \"type\".<br><br> If **type is natural_person**, then complete **natural_person_id** with the GUID of the **addressee (person)** created.<br> If **type is legal_person**, then complete **legal_person_id** with the GUID of the **addressee (enterprise)** created.<br> If **type is individual_enterprise**, then complete **natural_person_id and legal_person_id** with the GUIDs of the **addressees (person and enterprise)** created.<br> 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientApi()
new_client = swagger_client.Client() # Client | 
max_number = 789 # int | Parameter that enables the automatic issuing of a client number (by the system). It determines the client number up to which a search can be performed for an available client number(= highest available client number).  (optional)

try:
    # Creating a new client.
    api_instance.clients_post(new_client, max_number=max_number)
except ApiException as e:
    print("Exception when calling ClientApi->clients_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_client** | [**Client**](Client.md)|  | 
 **max_number** | **int**| Parameter that enables the automatic issuing of a client number (by the system). It determines the client number up to which a search can be performed for an available client number(&#x3D; highest available client number).  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

