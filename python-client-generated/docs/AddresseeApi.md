# swagger_client.AddresseeApi

All URIs are relative to *http://localhost:58454/datev/api/master-data/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addressees_addressee_id_get**](AddresseeApi.md#addressees_addressee_id_get) | **GET** /addressees/{addressee-id} | Retrieve an addressee.
[**addressees_addressee_id_put**](AddresseeApi.md#addressees_addressee_id_put) | **PUT** /addressees/{addressee-id} | Update a specific addressee.
[**addressees_deletion_log_get**](AddresseeApi.md#addressees_deletion_log_get) | **GET** /addressees/deletion-log | Retrieve a list of deleted addressees.
[**addressees_get**](AddresseeApi.md#addressees_get) | **GET** /addressees | Retrieve a list of addressees.
[**addressees_post**](AddresseeApi.md#addressees_post) | **POST** /addressees | Create a new addressee.


# **addressees_addressee_id_get**
> Addressee addressees_addressee_id_get(addressee_id, select=select, expand=expand)

Retrieve an addressee.

 **Retrieving an addressee with subordinate objects**  By including the parameter expand=* in the URI, the full scope of the addressee object will be requested. If, instead of the asterisk (*), the property name of the subordinate object is entered, the addressee object will be requested with the stated subordinate object (e.g. \"expand=detail, addresses\" retrieves the addressee object along with the addressee details and addresses).<br> In the standard case, without the expand parameter, the addressee object will be requested without subordinate objects (addressee details, addresses, communication details, bank_accounts and tax_offices). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddresseeApi()
addressee_id = 'addressee_id_example' # str | The GUID of an addressee.
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)
expand = 'expand_example' # str | A parameter that makes it possible to read a resource along with all subordinate objects.  If an asterisk (*) is entered, all subordinate objects will be loaded with the resource.  (optional)

try:
    # Retrieve an addressee.
    api_response = api_instance.addressees_addressee_id_get(addressee_id, select=select, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddresseeApi->addressees_addressee_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addressee_id** | **str**| The GUID of an addressee. | 
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 
 **expand** | **str**| A parameter that makes it possible to read a resource along with all subordinate objects.  If an asterisk (*) is entered, all subordinate objects will be loaded with the resource.  | [optional] 

### Return type

[**Addressee**](Addressee.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addressees_addressee_id_put**
> addressees_addressee_id_put(addressee_id, addressee)

Update a specific addressee.

With the PUT command, the addressee will be completely overwritten (addressee incl. subordinate objects).<br> We therefore recommend that you perform a request, with the parameter expand=*, of the addressee being updated beforehand in order to prevent master data from being overwritten.<br> The following properties may not be changed: - id - type 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddresseeApi()
addressee_id = 'addressee_id_example' # str | The GUID of an addressee.
addressee = swagger_client.Addressee() # Addressee | Addressee object

try:
    # Update a specific addressee.
    api_instance.addressees_addressee_id_put(addressee_id, addressee)
except ApiException as e:
    print("Exception when calling AddresseeApi->addressees_addressee_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addressee_id** | **str**| The GUID of an addressee. | 
 **addressee** | [**Addressee**](Addressee.md)| Addressee object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addressees_deletion_log_get**
> list[DeletionLog] addressees_deletion_log_get(select=select, filter=filter)

Retrieve a list of deleted addressees.

**Filter** Unless a filter is entered, the list will contain all deleted addressees. The \"timestamp\" filter option can be used to limit the results to a specific time period.<br><br>  **Filter Options**  The number of results can be limited by using the following filters: - id - timestamp <br>  **Operators** <br>  *Filter Option: timestamp*  | Operator          | Description           | |-------------------|-----------------------| | eq                | Equal                 | | gt                | Greater than          | | ge                | Greater than or equal | | lt                | Less than             | | le                | Less than or equal    |  <br>  *Filter Option: id*  | Operator          | Description           | |-------------------|-----------------------| | eq                | Equal                 |  <br>  **Filter Combinations**  Filters can be combined using the operator \"and\".<br><br>  **URI Examples**  *Retrieving deleted addressees who were deleted after 03/31/2018.*      .../addressees/deletion-log?filter=timestamp gt 2018-03-31T00:00:00.000<br><br>            

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddresseeApi()
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)
filter = 'filter_example' # str | Entering a filter expression influences the number of results.  (optional)

try:
    # Retrieve a list of deleted addressees.
    api_response = api_instance.addressees_deletion_log_get(select=select, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddresseeApi->addressees_deletion_log_get: %s\n" % e)
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

# **addressees_get**
> list[Addressee] addressees_get(select=select, filter=filter)

Retrieve a list of addressees.

 **Filter**  Unless further parameters are entered, the list will contain both active and inactive addressees.<br><br>  **Filter Options**  The number of results can be limited by using the following filters: - current_short_name - surrogate_name         - current_company_name - current_surname - date_of_birth - date_of_foundation - firstname - eu_vat_id_country_code - eu_vat_id_number - sex - etin - tax_identification_number - current_legal_form_id - status - timestamp - type <br>  **Operators** <br> *Filter Option: timestamp*  | Operator          | Description             | |-------------------|-------------------------| | eq                | Equal                   | | gt                | Greater than            | | ge                | Greater than or equal   | | lt                | Less than               | | le                | Less than or equal      | <br>   *Filter Option: current_short_name, surrogate_name, current_company_name, current_surname, firstname, eu_vat_id_number, etin, tax_identification_number*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | | contains(property, substring)  | Search for Substring in property's value                       | | startswith(property, substring)| Search for Substring at the beginning of the property's value  | <br>  *Filter Option:* date_of_birth, date_of_foundation, eu_vat_id_country_code, sex, current_legal_form_id, status, type  | Operator                       | Description  | |--------------------------------|--------------| | eq                             | Equal        | <br>  **Filter Combinations**  Filters can be combined using the operator \"and\".<br><br> 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddresseeApi()
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)
filter = 'filter_example' # str | Entering a filter expression influences the number of results.  (optional)

try:
    # Retrieve a list of addressees.
    api_response = api_instance.addressees_get(select=select, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddresseeApi->addressees_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 
 **filter** | **str**| Entering a filter expression influences the number of results.  | [optional] 

### Return type

[**list[Addressee]**](Addressee.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addressees_post**
> addressees_post(new_addressee, national_right=national_right)

Create a new addressee.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddresseeApi()
new_addressee = swagger_client.Addressee() # Addressee | 
national_right = 'national_right_example' # str | This parameter serves a dual purpose:<br><br> **A: Ressource 'legal-forms'**<br> Parameter that controls the display of company legal forms depending on national law.<br><br>If 'national-right=german' is entered, then all company legal forms will be listed that are relevant to addressees subject to German law.<br>If 'national-right=austrian' is entered, then all company legal forms will be listed that are relevant to addressees subject to Austrian law.<br><br> **B: Ressource 'addressees'**<br> Parameter defines the national law that will be saved with the addressee. If the parameter is not entered, the national law that corresponds to the product installed will be entered as the default option:<br><br>If the package 'DATEV Basis für Österreich' is installed, then \"Austrian\" will be set as the applicable national law for the addressee.<br>If the package 'DATEV Basis' is installed, then \"German\" will be set as the applicable national law for the addressee.  (optional)

try:
    # Create a new addressee.
    api_instance.addressees_post(new_addressee, national_right=national_right)
except ApiException as e:
    print("Exception when calling AddresseeApi->addressees_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_addressee** | [**Addressee**](Addressee.md)|  | 
 **national_right** | **str**| This parameter serves a dual purpose:&lt;br&gt;&lt;br&gt; **A: Ressource &#39;legal-forms&#39;**&lt;br&gt; Parameter that controls the display of company legal forms depending on national law.&lt;br&gt;&lt;br&gt;If &#39;national-right&#x3D;german&#39; is entered, then all company legal forms will be listed that are relevant to addressees subject to German law.&lt;br&gt;If &#39;national-right&#x3D;austrian&#39; is entered, then all company legal forms will be listed that are relevant to addressees subject to Austrian law.&lt;br&gt;&lt;br&gt; **B: Ressource &#39;addressees&#39;**&lt;br&gt; Parameter defines the national law that will be saved with the addressee. If the parameter is not entered, the national law that corresponds to the product installed will be entered as the default option:&lt;br&gt;&lt;br&gt;If the package &#39;DATEV Basis für Österreich&#39; is installed, then \&quot;Austrian\&quot; will be set as the applicable national law for the addressee.&lt;br&gt;If the package &#39;DATEV Basis&#39; is installed, then \&quot;German\&quot; will be set as the applicable national law for the addressee.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

