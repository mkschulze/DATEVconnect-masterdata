# Client

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | GUID of a client – internal identifier. The ID may not be entered with POST (it is issued by the system); with PUT, however, the ID is a mandatory field.  | [optional] 
**client_since** | **date** | Indicates the start date of a client relationship. | [optional] 
**client_to** | **date** | Indicates the end date of a client relationship. | [optional] 
**differing_name** | **str** | Differing client name. | [optional] 
**legal_person_id** | **str** | GUID of an enterprise - internal identifier. Reference to the enterprise that is a client (client addressee).  | [optional] 
**name** | **str** | Name of the client. | 
**natural_person_id** | **str** | GUID of a person – internal identifier. Reference to the person who is a client (client addressee).  | [optional] 
**note** | **str** | Note about a client relationship (free text). | [optional] 
**number** | **int** | Central client number. If the client number is issued automatically (by the server), the query parameter \&quot;max-number\&quot; also has to be used. The central client number then represents the smallest available client number; the value entered in the parameter represents the largest possible client number. Within this range (central client number/max-number), the server will automatically issue the client number. If there are no available client numbers left, error code 400 will be returned.  | 
**status** | **str** | Indicates whether the client relationship is active or inactive. | [optional] 
**timestamp** | **date** | Indicates when the client was last edited. | [optional] 
**type** | **str** | Key that describes the type of client. | 
**organization_id** | **str** | GUID of an organization - internal identifier.  Indicates the GUID of the organization to which the client is assigned. This property may not be changed. The assignment can only be changed via the property &#39;establishment_id&#39;. Only relevant if the package &#39;Unternehmensstrukturen&#39; is installed.  | [optional] 
**organization_name** | **str** | Indicates the name of the organization to which the client is assigned. Only relevant if the package &#39;Unternehmensstrukturen&#39; is installed.  | [optional] 
**organization_number** | **int** | Indicates the number of the organization to which the client is assigned. Only relevant if the package &#39;Unternehmensstrukturen&#39; is installed.  | [optional] 
**establishment_id** | **str** | GUID of an establishment - internal identifier. Indicates the GUID of the establishment to which the client is assigned. Only relevant if the package &#39;Unternehmensstrukturen&#39; is installed.  | [optional] 
**establishment_name** | **str** | Indicates the name of the establishment to which the client is assigned. Only relevant if the package &#39;Unternehmensstrukturen&#39; is installed.  | [optional] 
**establishment_number** | **int** | Indicates the number of the establishment to which the client is assigned. Only relevant if the package &#39;Unternehmensstrukturen&#39; is installed.  | [optional] 
**establishment_short_name** | **str** | Indicates the short name of the establishment to which the client is assigned. Only relevant if the package &#39;Unternehmensstrukturen&#39; is installed.  | [optional] 
**functional_area_id** | **str** | GUID of a functional area - internal identifier. Indicates the GUID of the functional area to which the client is assigned. Only relevant if the package &#39;Eigenorganisation comfort&#39; is installed.  | [optional] 
**functional_area_name** | **str** | Indicates the name of the functional area to which the client is assigned. Only relevant if the package &#39;Eigenorganisation comfort&#39; is installed.  | [optional] 
**functional_area_short_name** | **str** | Indicates the short name of the functional area to which the client is assigned. Only relevant if the package &#39;Eigenorganisation comfort&#39; is installed.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


