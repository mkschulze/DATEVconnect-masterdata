# Communication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | GUID - internal ID of a communication link. | [optional] 
**type** | **str** | Indicates the type of communication medium to which a certain number/address relates. Can only be selected when creating a new communication link. Otherwise, this field will be read-only. | 
**data_content** | **str** | Indicates the number (e.g. telephone number) or address (e.g. e-mail address) of the communication medium concerned. | [optional] 
**number_standardized** | **str** | Indicates the telephone number/fax number without special characters (purely as a sequence of digits). | [optional] 
**note** | **str** | Field for notes about the communication link. | [optional] 
**is_main_communication** | **bool** | Indicates the standard communication link for each means of communication. If communication_type is &#39;other&#39;, then this property may not be set to &#39;true&#39;. Apart from this, exactly one of the communication links for the means of communication must be marked as &#39;true&#39;. | [optional] 
**is_management_phone** | **bool** | Indicates the management phone. Only relevant if the communication type is &#39;phone&#39; and the associated addressee is of the type &#39;legal_person&#39;. Exactly one telephone line of the corresponding addressee must be marked as &#39;true&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


