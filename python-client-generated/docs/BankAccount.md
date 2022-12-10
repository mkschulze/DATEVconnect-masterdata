# BankAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | GUID - internal ID of a bank account. | [optional] 
**bank_account_number** | **str** | Number of the bank account. The maximum length depends on the country in which the bank account is located (property country_code). For &#39;DE&#39; 10 digits; for &#39;AT&#39; 11 digits; for &#39;PL&#39; 16 digits; for &#39;IT&#39; 20 digits; for &#39;CZ&#39; 17 digits. For any other country 30 digits are permissible. | [optional] 
**bank_code** | **str** | Code number for identification all banks within a country. Bank branches are not identified. The maximum length depends on the country in which the bank is located (property country_code). For &#39;DE&#39; 8 digits; for &#39;AT&#39; 5 digits; for &#39;PL&#39; 8 digits. For any other country 10 digits are permissible. | [optional] 
**bank_name** | **str** | Name of the bank. | [optional] 
**bic** | **str** | Unique identifier for a SWIFT-participant (BIC - Bank Identifier Code). SWIFT is the abbreviation for \&quot;Society for Worldwide Interbank Financial Telecommunications\&quot;. | [optional] 
**country_code** | **str** | Indicates the country in which the bank is located. The following values are permissible (see “country_of_birth” definition). | [optional] 
**differing_account_holder** | **str** | Name of the account holder, if is not the associated addressee. | [optional] 
**iban** | **str** | Identifies a bank account worldwide (ISO 13616). | [optional] 
**note** | **str** | Field for notes about the bank account. | [optional] 
**valid_from** | **date** | Indicates the date from which a bank account is valid. | [optional] 
**valid_to** | **date** | Indicates the date until which a bank account is valid. | [optional] 
**currently_valid** | **bool** | Indicates whether or not the bank account is currently valid. | [optional] 
**is_main_bank_account** | **bool** | Indicates whether this is the main bank account. Among all valid bank accounts of an addressee, this property must be marked with &#39;true&#39; exactly once. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


