# swagger_client.ResponsibilityApi

All URIs are relative to *http://localhost:58454/datev/api/master-data/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**area_of_responsibilities_get**](ResponsibilityApi.md#area_of_responsibilities_get) | **GET** /area-of-responsibilities | Retrieve a list of areas of responsibility.
[**clients_client_id_responsibilities_get**](ResponsibilityApi.md#clients_client_id_responsibilities_get) | **GET** /clients/{client-id}/responsibilities | Retrieve a list of responsibilities for a specific client.
[**clients_client_id_responsibilities_put**](ResponsibilityApi.md#clients_client_id_responsibilities_put) | **PUT** /clients/{client-id}/responsibilities | Update the responsibilities for a specific client.
[**responsibilities_get**](ResponsibilityApi.md#responsibilities_get) | **GET** /responsibilities | Retrieve a list of responsibilities.


# **area_of_responsibilities_get**
> list[AreaOfResponsibility] area_of_responsibilities_get(select=select, filter=filter)

Retrieve a list of areas of responsibility.

 **Filter** Unless further parameters are entered, the list will contain both active and inactive areas of responsibility.<br><br>  **Filter Options**  The number of results can be limited by using the following filters: - name - status <br>  **Operators** <br>   *Filter Option: name*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | | contains(property, substring)  | Search for Substring in property's value                       | | startswith(property, substring)| Search for Substring at the beginning of the property's value  | <br>   *Filter Option: status, standard*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | <br>  **Filter Combinations**  Filters can be combined using the operator \"and\".<br><br>  **URI Examples**  *Retrieving the area of responsibility \"Mandatsverantwortung\"*        .../area-of-responsibilities?filter=name eq Mandatsverantwortung<br><br>  *Retrieving all active areas of responsibility*        .../area-of-responsibilities?filter=status eq active<br><br>            

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResponsibilityApi()
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)
filter = 'filter_example' # str | Entering a filter expression influences the number of results.  (optional)

try:
    # Retrieve a list of areas of responsibility.
    api_response = api_instance.area_of_responsibilities_get(select=select, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponsibilityApi->area_of_responsibilities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 
 **filter** | **str**| Entering a filter expression influences the number of results.  | [optional] 

### Return type

[**list[AreaOfResponsibility]**](AreaOfResponsibility.md)

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
api_instance = swagger_client.ResponsibilityApi()
client_id = 'client_id_example' # str | The GUID of a client.
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)

try:
    # Retrieve a list of responsibilities for a specific client.
    api_response = api_instance.clients_client_id_responsibilities_get(client_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponsibilityApi->clients_client_id_responsibilities_get: %s\n" % e)
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
api_instance = swagger_client.ResponsibilityApi()
client_id = 'client_id_example' # str | The GUID of a client.
responsibility = [swagger_client.Responsibility()] # list[Responsibility] | Responsibility object

try:
    # Update the responsibilities for a specific client.
    api_instance.clients_client_id_responsibilities_put(client_id, responsibility)
except ApiException as e:
    print("Exception when calling ResponsibilityApi->clients_client_id_responsibilities_put: %s\n" % e)
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

# **responsibilities_get**
> list[Responsibility] responsibilities_get(select=select, filter=filter)

Retrieve a list of responsibilities.

 **Filter** Unless further parameters are entered, the list will contain all responsibilities for both active and inactive clients.<br><br>  **Filter Options**  The number of results can be limited by using the following filters: - area_of_responsibility_id - area_of_responsibility_name - employee_id - employee_display_name - employee_number - employee_status - client_id - client_name - client_number - client_status <br>  **Operators** <br>  *Filter Option: employee_number, client_number*  | Operator          | Description           | |-------------------|-----------------------| | eq                | Equal                 | | gt                | Greater than          | | ge                | Greater than or equal | | lt                | Less than             | | le                | Less than or equal    | <br>   *Filter Option: area_of_responsibility_id, area_of_responsibility_name, employee_display_name, client_name*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | | contains(property, substring)  | Search for Substring in property's value                       | | startswith(property, substring)| Search for Substring at the beginning of the property's value  | <br>   *Filter Option: employee_id, employee_status, client_id, client_status*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | <br>  **Filter Combinations**  Filters can be combined using the operator \"and\".<br><br>  **URI Examples**  *Retrieving the responsibilities for the client with the client number 20000*        .../responsibilities?filter=client_number eq 20000 <br><br>            

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResponsibilityApi()
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)
filter = 'filter_example' # str | Entering a filter expression influences the number of results.  (optional)

try:
    # Retrieve a list of responsibilities.
    api_response = api_instance.responsibilities_get(select=select, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponsibilityApi->responsibilities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 
 **filter** | **str**| Entering a filter expression influences the number of results.  | [optional] 

### Return type

[**list[Responsibility]**](Responsibility.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

