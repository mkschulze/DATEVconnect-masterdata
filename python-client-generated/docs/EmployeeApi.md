# swagger_client.EmployeeApi

All URIs are relative to *http://localhost:58454/datev/api/master-data/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**employees_employee_id_get**](EmployeeApi.md#employees_employee_id_get) | **GET** /employees/{employee-id} | Retrieve a specific consultancy employee.
[**employees_employee_id_put**](EmployeeApi.md#employees_employee_id_put) | **PUT** /employees/{employee-id} | Update a specific consultancy employee.
[**employees_get**](EmployeeApi.md#employees_get) | **GET** /employees | Retrieve a list of consultancy employees.
[**employees_post**](EmployeeApi.md#employees_post) | **POST** /employees | Creating a new consultancy employee.


# **employees_employee_id_get**
> Employee employees_employee_id_get(employee_id, select=select)

Retrieve a specific consultancy employee.

 Retrieving a specific consultancy employee. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmployeeApi()
employee_id = 'employee_id_example' # str | The GUID of an employee.
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)

try:
    # Retrieve a specific consultancy employee.
    api_response = api_instance.employees_employee_id_get(employee_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeeApi->employees_employee_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| The GUID of an employee. | 
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 

### Return type

[**Employee**](Employee.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employees_employee_id_put**
> employees_employee_id_put(employee_id, employee)

Update a specific consultancy employee.

With the PUT command, the consultancy employee will be completely overwritten. We therefore recommend that you perform a request of the employee being updated beforehand in order to prevent master data from being overwritten.<br><br>  The following properties may not be changed: - id - natural_person_id - number 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmployeeApi()
employee_id = 'employee_id_example' # str | The GUID of an employee.
employee = swagger_client.Employee() # Employee | employee object

try:
    # Update a specific consultancy employee.
    api_instance.employees_employee_id_put(employee_id, employee)
except ApiException as e:
    print("Exception when calling EmployeeApi->employees_employee_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| The GUID of an employee. | 
 **employee** | [**Employee**](Employee.md)| employee object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employees_get**
> list[Employee] employees_get(select=select, filter=filter)

Retrieve a list of consultancy employees.

 **Filter** Unless further parameters are entered, the list will contain both active and inactive consultancy employees.<br><br>  **Filter Options**  The number of results can be limited by using the following filters: - name - number - status - timestamp - organization_id - organization_name - organization_number - establishment_id - establishment_name - establishment_number - establishment_short_name - functional_area_id - functional_area_name - functional_area_short_name <br>  **Operators** <br>  *Filter Option: number, timestamp, organization_number, establishment_number*  | Operator          | Description           | |-------------------|-----------------------| | eq                | Equal                 | | gt                | Greater than          | | ge                | Greater than or equal | | lt                | Less than             | | le                | Less than or equal    | <br>   *Filter Option: name, organization_name, establishment_name, establishment_short_name, functional_area_name, functional_area_short_name*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | | contains(property, substring)  | Search for Substring in property's value                       | | startswith(property, substring)| Search for Substring at the beginning of the property's value  | <br>   *Filter Option: status, organization_id, establishment_id, functional_area_id*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal; 'Gleich'                                                | <br>  **Filter Combinations**  Filters can be combined using the operator \"and\".<br><br>  **URI Examples**  *Retrieving an employee with the employee number 20000*        .../employees?filter=number eq 20000<br><br>  *Retrieving all employees whose employee number is greater than or equal to 10000 and less than 70000* .../employees?filter=number ge 20000 and number lt 70000<br><br>  *Retrieving all employees whose name contains the word \"Mustermeier\"*        .../employees?filter=contains(name, Mustermeier)<br><br>  *Retrieving all active employees*        .../employees?filter=status eq active<br><br>            

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmployeeApi()
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)
filter = 'filter_example' # str | Entering a filter expression influences the number of results.  (optional)

try:
    # Retrieve a list of consultancy employees.
    api_response = api_instance.employees_get(select=select, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeeApi->employees_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 
 **filter** | **str**| Entering a filter expression influences the number of results.  | [optional] 

### Return type

[**list[Employee]**](Employee.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employees_post**
> employees_post(new_employee)

Creating a new consultancy employee.

 When creating a new consultancy employee, please note that the addressee of the type \"natural_person\" (POST /addressees) has to be created first, followed by the consultancy employee (POST /employees). The property \"natural_person_id\" must be completed with the GUID of the created addressee.<br> If the property \"number\" is not specified or completed with 0, then the system assigns the number automatically. In this case the largest assigned number is increased by 1. If  the number 99999 is already assigned, the system fills the gaps. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmployeeApi()
new_employee = swagger_client.Employee() # Employee | 

try:
    # Creating a new consultancy employee.
    api_instance.employees_post(new_employee)
except ApiException as e:
    print("Exception when calling EmployeeApi->employees_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_employee** | [**Employee**](Employee.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

