# Addressee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | GUID of an addressee – internal identifier. The ID may not be entered with POST (it is issued by the system); with PUT, however, the ID is a mandatory field.  | [optional] 
**eu_vat_id_country_code** | **str** | VAT ID country codes (AT &#x3D; Österreich, BE &#x3D; Belgien, BG &#x3D; Bulgarien, CY &#x3D; Zypern, CZ &#x3D; Tschechische Republik, DE &#x3D; Deutschland, DK &#x3D; Dänemark, EE &#x3D; Estland, EL &#x3D; Griechenland, ES &#x3D; Spanien, EU &#x3D; Europäische Union, FI &#x3D; Finnland, FR &#x3D; Frankreich, GB &#x3D; Großbritannien, HR &#x3D; Kroatien, HU &#x3D; Ungarn, IE &#x3D; Irland, IT &#x3D; Italien, LT &#x3D; Litauen, LU &#x3D; Luxemburg, LV &#x3D; Lettland, MT &#x3D; Malta, NL &#x3D; Niederlande, PL &#x3D; Polen, PT &#x3D; Portugal, RO &#x3D; Rumänien, SE &#x3D; Schweden, SI &#x3D; Slowenien, SK &#x3D; Slowakei, XI &#x3D; Nordirland). | [optional] 
**eu_vat_id_number** | **str** | VAT ID without country code. | [optional] 
**short_names** | [**list[ShortName]**](ShortName.md) |  | [optional] 
**current_short_name** | **str** | Current short name of the addressee (&#x3D; value as at system date). | [optional] 
**status** | **str** | Indicates whether the addressee is active or inactive.  | [optional] 
**surrogate_name** | **str** | Alias of an addressee for search purposes. | [optional] 
**timestamp** | **date** | Indicates when the addressee was last edited. | [optional] 
**type** | **str** | Indicates whether the addressee is a person or an enterprise. With PUT, the content of this property may not be changed. | 
**date_of_birth** | **date** | Date of birth of a natural person.&lt;br&gt;&lt;br&gt;The property may only be filled if the addressee is of the type &#39;natural_person&#39;. | [optional] 
**etin** | **str** | The eTIN is an income tax-related identification number given to every employee in Germany; the legal basis is Section 41b (2) of the German Income Tax Act (EStG). However, the calculation method does not exclude the possibility that the same eTIN might be assigned to more than one person. As it is sufficiently unlikely, however, that two different people with the same eTIN fall within the jurisdiction of the same tax authority, this is acceptable for the purposes of the eTIN. The eTIN is a 14-character code that is made up of the following personal data; last name, first name, and date of birth; it comprises the upper-case letters A to Z, as well as the digits 0 to 9. As long as this personal data does not change (e.g. a change of name upon marriage), the eTIN will remain valid; otherwise, it has to be amended to reflect the change in name.&lt;br&gt;&lt;br&gt;The property may only be filled if the addressee is of the type &#39;natural_person&#39;. | [optional] 
**firstname** | **str** | First name of a natural person.&lt;br&gt;&lt;br&gt;The property may only be filled if the addressee is of the type &#39;natural_person&#39;. | [optional] 
**sex** | **str** | Gender of a natural person.&lt;br&gt;&lt;br&gt;The property may only be filled if the addressee is of the type &#39;natural_person&#39;. | [optional] 
**surnames** | [**list[Surname]**](Surname.md) | The property may only be filled if the addressee is of the type &#39;natural_person&#39;. | [optional] 
**current_surname** | **str** | Current last name of a natural person (&#x3D; value as at system date). Mandatory field if you wish to create an addressee of the type \&quot;natural_person\&quot;.&lt;br&gt;&lt;br&gt;The property may only be filled if the addressee is of the type &#39;natural_person&#39;. | [optional] 
**tax_identification_number** | **str** | Unique tax identification number for natural persons as per Section 139b of the German Fiscal Code (AO).&lt;br&gt;&lt;br&gt;The property may only be filled if the addressee is of the type &#39;natural_person&#39;. | [optional] 
**company_names** | [**list[CompanyName]**](CompanyName.md) | The property may only be filled if the addressee is of the type &#39;legal_person&#39;. | [optional] 
**current_company_name** | **str** | Current company name (&#x3D; value as at system date). Mandatory field if you wish to create an addressee of the type \&quot;legal_person\&quot;.&lt;br&gt;&lt;br&gt;The property may only be filled if the addressee is of the type &#39;legal_person&#39;. | [optional] 
**date_of_foundation** | **date** | Date on which an operational commercial enterprise is established (date of foundation).&lt;br&gt;&lt;br&gt;The property may only be filled if the addressee is of the type &#39;legal_person&#39;. | [optional] 
**legal_form_ids** | [**list[LegalFormId]**](LegalFormId.md) | The property may only be filled if the addressee is of the type &#39;legal_person&#39;. | [optional] 
**current_legal_form_id** | **str** | Current legal form of the enterprise (&#x3D; value as at system date).&lt;br&gt;&lt;br&gt;The property may only be filled if the addressee is of the type &#39;legal_person&#39;. | [optional] 
**detail** | [**Detail**](Detail.md) |  | [optional] 
**addresses** | [**list[Address]**](Address.md) |  | [optional] 
**communications** | [**list[Communication]**](Communication.md) |  | [optional] 
**bank_accounts** | [**list[BankAccount]**](BankAccount.md) |  | [optional] 
**tax_offices** | [**list[TaxOffice]**](TaxOffice.md) |  | [optional] 
**contact_persons** | [**list[ContactPerson]**](ContactPerson.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


