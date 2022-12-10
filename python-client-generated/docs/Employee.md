# Employee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | GUID of an employee – internal identifier. The ID may not be entered with POST (it is issued by the system); with PUT, however, the ID is a mandatory field.  | [optional] 
**display_name** | **str** | Display name comprising a last and a first name. | [optional] 
**email** | **str** | E-mail address at which the employee can be contacted in their position at the consultancy. | [optional] 
**entry_date** | **date** | Employment start date of the employee. | [optional] 
**fax** | **str** | Fax number on which the employee can be contacted in their position at the consultancy. | [optional] 
**initials** | **str** | Indicates the initials of the employee; these should be unique throughout the consultancy. The initials may, for example, be stated on the invoice. | [optional] 
**name** | **str** | Name of the employee. | 
**natural_person_id** | **str** | GUID of a person – internal identifier. Reference to the person (addressee) who is an employee.  | 
**note** | **str** | Note about an employee (free text). | [optional] 
**number** | **int** | Number of the employee (personnel number).&lt;br&gt;If number 0 entered with POST, the number is issued by the system.  | [optional] 
**phone_extension** | **str** | Phone extension on which the employee can be contacted in their position at the consultancy. | [optional] 
**separation_date** | **date** | Employment end date of the employee. | [optional] 
**status** | **str** | Indicates whether the employee is active or inactive. | [optional] 
**timestamp** | **date** | Indicates when the employee was last edited. | [optional] 
**organization_id** | **str** | GUID of an organization - internal identifier.  Indicates the GUID of the organization to which the employee is assigned. This property may not be changed. The assignment can only be changed via the property &#39;establishment_id&#39;. Only relevant if the package &#39;Unternehmensstrukturen&#39; is installed.  | [optional] 
**organization_name** | **str** | Indicates the name of the organization to which the employee is assigned. Only relevant if the package &#39;Unternehmensstrukturen&#39; is installed.  | [optional] 
**organization_number** | **int** | Indicates the number of the organization to which the employee is assigned. Only relevant if the package &#39;Unternehmensstrukturen&#39; is installed.  | [optional] 
**establishment_id** | **str** | GUID of an establishment - internal identifier. Indicates the GUID of the establishment to which the employee is assigned. Only relevant if the package &#39;Unternehmensstrukturen&#39; is installed.  | [optional] 
**establishment_name** | **str** | Indicates the name of the establishment to which the employee is assigned. Only relevant if the package &#39;Unternehmensstrukturen&#39; is installed.  | [optional] 
**establishment_number** | **int** | Indicates the number of the establishment to which the employee is assigned. Only relevant if the package &#39;Unternehmensstrukturen&#39; is installed.  | [optional] 
**establishment_short_name** | **str** | Indicates the short name of the establishment to which the employee is assigned. Only relevant if the package &#39;Unternehmensstrukturen&#39; is installed.  | [optional] 
**functional_area_id** | **str** | GUID of a functional area - internal identifier. Indicates the GUID of the functional area to which the employee is assigned. Only relevant if the package &#39;Eigenorganisation comfort&#39; is installed.  | [optional] 
**functional_area_name** | **str** | Indicates the name of the functional area to which the employee is assigned. Only relevant if the package &#39;Eigenorganisation comfort&#39; is installed.  | [optional] 
**functional_area_short_name** | **str** | Indicates the short name of the functional area to which the employee is assigned. Only relevant if the package &#39;Eigenorganisation comfort&#39; is installed.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


