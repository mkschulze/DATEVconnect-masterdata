# swagger_client.LegalFormApi

All URIs are relative to *http://localhost:58454/datev/api/master-data/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**legal_forms_get**](LegalFormApi.md#legal_forms_get) | **GET** /legal-forms | Retrieve a list of company legal forms.


# **legal_forms_get**
> list[LegalForm] legal_forms_get(select=select, national_right=national_right)

Retrieve a list of company legal forms.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LegalFormApi()
select = 'select_example' # str | Enter relevant attributes to which the results will then be limited.       (optional)
national_right = 'national_right_example' # str | This parameter serves a dual purpose:<br><br> **A: Ressource 'legal-forms'**<br> Parameter that controls the display of company legal forms depending on national law.<br><br>If 'national-right=german' is entered, then all company legal forms will be listed that are relevant to addressees subject to German law.<br>If 'national-right=austrian' is entered, then all company legal forms will be listed that are relevant to addressees subject to Austrian law.<br><br> **B: Ressource 'addressees'**<br> Parameter defines the national law that will be saved with the addressee. If the parameter is not entered, the national law that corresponds to the product installed will be entered as the default option:<br><br>If the package 'DATEV Basis für Österreich' is installed, then \"Austrian\" will be set as the applicable national law for the addressee.<br>If the package 'DATEV Basis' is installed, then \"German\" will be set as the applicable national law for the addressee.  (optional)

try:
    # Retrieve a list of company legal forms.
    api_response = api_instance.legal_forms_get(select=select, national_right=national_right)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegalFormApi->legal_forms_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Enter relevant attributes to which the results will then be limited.       | [optional] 
 **national_right** | **str**| This parameter serves a dual purpose:&lt;br&gt;&lt;br&gt; **A: Ressource &#39;legal-forms&#39;**&lt;br&gt; Parameter that controls the display of company legal forms depending on national law.&lt;br&gt;&lt;br&gt;If &#39;national-right&#x3D;german&#39; is entered, then all company legal forms will be listed that are relevant to addressees subject to German law.&lt;br&gt;If &#39;national-right&#x3D;austrian&#39; is entered, then all company legal forms will be listed that are relevant to addressees subject to Austrian law.&lt;br&gt;&lt;br&gt; **B: Ressource &#39;addressees&#39;**&lt;br&gt; Parameter defines the national law that will be saved with the addressee. If the parameter is not entered, the national law that corresponds to the product installed will be entered as the default option:&lt;br&gt;&lt;br&gt;If the package &#39;DATEV Basis für Österreich&#39; is installed, then \&quot;Austrian\&quot; will be set as the applicable national law for the addressee.&lt;br&gt;If the package &#39;DATEV Basis&#39; is installed, then \&quot;German\&quot; will be set as the applicable national law for the addressee.  | [optional] 

### Return type

[**list[LegalForm]**](LegalForm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

