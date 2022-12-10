# TaxOffice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | GUID - internal ID of a tax office. | [optional] 
**country_code** | **str** | Indicates the country in which the tax office is located. The following values are permissible (see “country_of_birth” definition). | [optional] 
**note** | **str** | Field for notes about the tax office. | [optional] 
**tax_number** | **str** | Indicates the tax number which is assigned to the tax payer. | [optional] 
**tax_number_certificated** | **str** | Indicates the tax number which is certified according to ELSTER guideline. | [optional] 
**tax_number_standardized** | **str** | Indicates the tax number without special characters (purely as a sequence of digits). | [optional] 
**tax_office_name** | **str** | Name of the tax office. | [optional] 
**tax_office_number** | **int** | Indicates the number of the tax office. This number identifies a tax office. | [optional] 
**valid_from** | **date** | Indicates the date from which a tax office is valid. | [optional] 
**valid_to** | **date** | Indicates the date until which a tax office is valid. | [optional] 
**currently_valid** | **bool** | Indicates whether or not the tax office is currently valid. | [optional] 
**is_competent_for_operational_income_tax** | **bool** | Indicates whether the tax office is competent for operating tax respectively income tax. Among all valid tax offices of an addressee, this property must be marked with &#39;true&#39; exactly once. | [optional] 
**is_competent_for_turnover_tax** | **bool** | Indicates whether the tax office is competent for turnover tax. Among all valid tax offices of an addressee, this property must be marked with &#39;true&#39; no more than once. | [optional] 
**is_competent_for_wage_tax** | **bool** | Indicates whether the tax office is competent for wage tax. Among all valid tax offices of an addressee, this property must be marked with &#39;true&#39; no more than once. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


