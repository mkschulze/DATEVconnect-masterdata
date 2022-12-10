# swagger_client.RelationshipApi

All URIs are relative to *http://localhost:58454/datev/api/master-data/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**relationship_types_get**](RelationshipApi.md#relationship_types_get) | **GET** /relationship-types | Retrieve a list of relationship types.
[**relationships_get**](RelationshipApi.md#relationships_get) | **GET** /relationships | Retrieve a list of relationships.


# **relationship_types_get**
> list[RelationshipType] relationship_types_get(select=select, filter=filter)

Retrieve a list of relationship types.

 **Filter** Unless further parameters are entered, the list will contain all relationship types.<br><br>  **Filter Options**  The number of results can be limited  by using the following filters: - id - abbreviation - name - standard - type <br>  **Operators** <br>  *Filter Option: name*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | | contains(property, substring)  | Search for Substring in property's value                       | | startswith(property, substring)| Search for Substring at the beginning of the property's value  | <br>   *Filter Option: id, abbreviation, standard, type*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | <br>  **Filter Combinations**  Filters can be combined using the operator \"and\".<br><br>  **URI Examples**  *Retrieving all standard relationship types.*        .../relationship-types?filter=standard eq true <br><br> 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationshipApi()
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)
filter = 'filter_example' # str | Entering a filter expression influences the number of results.  (optional)

try:
    # Retrieve a list of relationship types.
    api_response = api_instance.relationship_types_get(select=select, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationshipApi->relationship_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 
 **filter** | **str**| Entering a filter expression influences the number of results.  | [optional] 

### Return type

[**list[RelationshipType]**](RelationshipType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relationships_get**
> list[Relationship] relationships_get(select=select, filter=filter)

Retrieve a list of relationships.

 **Filter** Unless further parameters are entered, the list will contain all relationships of addressees.<br><br>  **Filter Options**  The number of results can be limited  by using the following filters: - id - abbreviation - name - standard - type_id - has_addressee_id - has_addressee_display_name - has_addressee_type - is_addressee_id - is_addressee_display_name - is_addressee_type <br>  **Operators** <br>  *Filter Option: name, has_addressee_display_name, is_addressee_dispay_name*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | | contains(property, substring)  | Search for Substring in property's value                       | | startswith(property, substring)| Search for Substring at the beginning of the property's value  | <br>   *Filter Option: id, abbreviation, standard, type_id, has_addresee_id, has_addressee_type, is_addressee_id, is_addressee_type*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | <br>  **Filter Combinations**  Filters can be combined using the operator \"and\".<br><br>  **URI Examples**  *Retrieving all addressees who are member of the company with the Guid 'i94g9c3g-380c-494e-97c8-d12fff738132'.*        .../relationships?filter=has_addresee_id eq i94g9c3g-380c-494e-97c8-d12fff738132 and type_id eq S00058<br><br>  *Retrieving all relationships of the addressee with the Guid 'p52f1c3g-380c-494e-97c8-d12fff738163' (e.g. addressee is member of company X, addressee is child from person Z, addressee is legal representative of company Y).* .../relationships?filter=is_addresee_id eq p52f1c3g-380c-494e-97c8-d12fff738163<br><br> 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationshipApi()
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)
filter = 'filter_example' # str | Entering a filter expression influences the number of results.  (optional)

try:
    # Retrieve a list of relationships.
    api_response = api_instance.relationships_get(select=select, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationshipApi->relationships_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 
 **filter** | **str**| Entering a filter expression influences the number of results.  | [optional] 

### Return type

[**list[Relationship]**](Relationship.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

