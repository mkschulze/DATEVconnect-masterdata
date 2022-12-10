# Bank

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal identifier of a bank.  | [optional] 
**bank_code** | **str** | Code number for identification all banks within a country. Bank branches are not identified. The maximum length depends on the country in which the bank is located (property country_code). For &#39;DE&#39; 8 digits; for &#39;AT&#39; 5 digits; for &#39;PL&#39; 8 digits. For any other country 10 digits are permissible. | [optional] 
**bic** | **str** | Unique identifier for a SWIFT-participant (BIC - Bank Identifier Code). SWIFT is the abbreviation for \&quot;Society for Worldwide Interbank Financial Telecommunications\&quot;. | [optional] 
**city** | **str** | Indicates the location of the bank. | [optional] 
**country_code** | **str** | Indicates the country in which the bank is located. The following values are permissible (see \&quot;country_of_birth\&quot; definition). | [optional] 
**name** | **str** | Name of the bank. | [optional] 
**standard** | **bool** | Indicates whether the bank is a standard institution (to be supplied) or an individual institution. | [optional] 
**timestamp** | **date** | Indicates when the bank was last edited. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


