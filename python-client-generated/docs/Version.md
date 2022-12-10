# Version

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adress_country** | **str** | Indicates which package is installed - &#39;DATEV Basis&#39; or &#39;DATEV Basis für Unternehmen&#39; (DE) or &#39;DATEV Basis für Österreich&#39; (AT). Depending on this information, the property &#39;national_right&#39; will be filled with the default option when the addressee is created. | [optional] 
**client_number_maximum_number_of_digits** | **int** | Potential maximum length of the central client number. | [optional] 
**client_number_start** | **int** | Indicates the first client number saved at the consultancy. | [optional] 
**client_categories_groups_supported** | **bool** | Indicates whether client categories und client groups are supported. This is the case if the package &#39;Eigenorganisation comfort&#39; is installed. | [optional] 
**db_build** | **str** | Build status of the EODB database. | [optional] 
**db_version** | **str** | Version number of the EODB database. | [optional] 
**db_version_date** | **str** | Version date of the EODB database (German date format). | [optional] 
**id** | **int** | Unique identifier of the version (always 1). | [optional] 
**resource_revision** | **str** | Indicates the revision status of the API Master Data. | [optional] 
**resource_version** | **str** | Indicates the version of the API Master Data (component of the base path). | [optional] 
**version** | **str** | Indicates the version of the component K0005004. | [optional] 
**version_name** | **str** | Indicates the name (incl. version) of the component K0005004. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


