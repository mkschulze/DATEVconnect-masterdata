# Address

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | GUID - internal ID of an address. | [optional] 
**type** | **str** | Address type (street address, PO box address, corporate client address). One of these must be selected when creating a new address. Otherwise, this field will be read-only. | 
**city** | **str** | Indicates the location. The maximum length depends on the country in which the address is located (for &#39;DE&#39; and &#39;AT&#39; 30 characters; for &#39;PL&#39; 41 characters; for any other country or if no country has been defined 62 characters are permissible). | [optional] 
**country_code** | **str** | Indicates the country in which the address is located. The following values are permissible (see “country_of_birth” definition). | [optional] 
**postal_code** | **str** | Indicates the postal code. The maximum length depends on the country in which the address is located (&#39;DE&#39; 5 digits, &#39;AT&#39; 4 digits, &#39;IT&#39; 5 digits, &#39;CZ&#39; 6 digits, &#39;PL&#39; 6 digits.  For &#39;DE&#39; and &#39;AT&#39;, the maximum and minimum lengths are the same. For any other country or if no country has been defined 10 digits are permissible). | [optional] 
**post_office_box** | **str** | Indicates the post office box.&lt;br&gt;&lt;br&gt;The property may only be filled if the address is of the type &#39;post_office_box&#39;. | [optional] 
**street** | **str** | Indicates the street. The maximum length depends on the country in which the address is located (for &#39;DE&#39; and &#39;AT&#39; 36 characters; for any other country or if no country has been defined 41 characters are permissible).&lt;br&gt;The property may only be filled if the address is of the type &#39;street&#39;. | [optional] 
**additional_correspondence_title** | **str** | Indicates a differing title in correspondence. | [optional] 
**additional_delivery_text1** | **str** | Indicates the first part of the name of the differing delivery addressee. | [optional] 
**additional_delivery_text2** | **str** | Indicates the second part of the name of the differing delivery addressee. | [optional] 
**additional_shipping_information** | **str** | Indicates additional shipping information in correspondence, e.g. private/confidential or a shipment. | [optional] 
**address_appendix** | **str** | Indicates an address appendix in correspondence, e.g. \&quot;c/o\&quot;. | [optional] 
**address_manually_edited** | **str** | Indicates a manually edited address. | [optional] 
**is_address_manually_edited** | **bool** | Indicates whether the address has been manually edited. | [optional] 
**note** | **str** | Field for notes about the address. | [optional] 
**valid_from** | **date** | Indicates the date from which an address is valid. | [optional] 
**valid_to** | **date** | Indicates the date until which an address is valid. | [optional] 
**currently_valid** | **bool** | Indicates whether or not the address is currently valid. | [optional] 
**is_correspondence_address** | **bool** | Indicates whether this is the correspondence address. Among all valid addresses  of an addressee, this property must be marked with &#39;true&#39; exactly once. | [optional] 
**is_debitor_address** | **bool** | Indicates whether this is the debtor address. Among all valid addresses of an addressee, this property must be marked with &#39;true&#39; no more than once. | [optional] 
**is_main_post_office_box_address** | **bool** | Indicates whether this is the main post office box address. Only relevant if the address is a post office box address (type&#x3D;post_office_box). Among all valid post office box addresses of an addressee, this property must be marked with &#39;true&#39; exactly once. | [optional] 
**is_main_street_address** | **bool** | Indicates whether this is the main street address. Only relevant if the address is a street address (type&#x3D;street). Among all valid street addresses of an addressee, this property must be marked with &#39;true&#39; exactly once. | [optional] 
**is_management_address** | **bool** | Indicates whether this is the management address. Only relevant if the associated addressee is of the type &#39;legal_person&#39;. Among all valid addresses of an addressee (legal_person), this property must be marked with &#39;true&#39; exactly once. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


