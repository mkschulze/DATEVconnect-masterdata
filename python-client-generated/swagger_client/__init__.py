# coding: utf-8

# flake8: noqa

"""
    Client Master Data

    In the documentation below, you will receive detailed functional and technical specifications on the API DATEVconnect for Master Data.  **General information on dealing with fields administered as historical** A number of fields in the  master data are administered as \"historical\". This means that the existing content is not overwritten when the field is updated, but that the existing value remains in place, with a new value added that is valid from a date entered by the user.  Specifically, the following fields are administered as historical:  *Ressource 'addressees'* - short_names, - surnames, - company_names, - legal_form_ids  *Subordinate object 'detail'* - considerations, - denominations, - federal_states_of_natural_person, - job_titles, - marital_statuses, - codes_of_classification_of_economic_activities_2008, - descriptions_of_classification_of_economic_activities_2008, - mad_codes_of_classification_of_economic_activities_2008, - codes_of_classification_of_economic_activities_2003, - descriptions_of_classification_of_economic_activities_2003, - mad_codes_of_classification_of_economic_activities_2003, - countries_of_head_office, - distributions_of_profit, - enterprise_purposes, - federal_states_mad_of_legal_person, - federal_states_of_legal_person, - fiscal_years, - kind_of_register_courts, - locations_of_head_office, - names_of_register_court, - registered_company_names, - registration_numbers, - three_lined_company_names_first_line, - three_lined_company_names_second_line, - three_lined_company_names_third_line, - two_lined_company_names_first_line, - two_lined_company_names_second_line  These fields are shown as arrays, with their elements exhibiting the following structure: - value, - valid_from  This structure makes it possible to generate periods that indicate the validity date of a particular value in a value range.  This is illustrated by the following examples:  \"job_titles\": [   {\"value\":\"Müller\"},   {\"value\":\"Bäcker\", \"valid_from\":\"1995-04-01T00:00:00.000\"},   {\"value\":\"Metzger\", \"valid_from\":\"2001-07-01T00:00:00.000\"} ] In this example, the profession \"Müller\" (\"miller\") was valid until 03/31/1995. \"Bäcker\" (\"baker\") was valid from 04/01/1995 to 06/30/2001. The value \"Metzger\" (\"butcher\") is valid starting 07/01/2001.  For all the historically administered fields listed above, there is an additional field that indicates the current value of the value range (the value that is valid today/as of the system time). The syntactic structure of the property name is as follows: current_<*Property name of the historically administered field in the singular*>.  In the example above, the property name is \"current_job_title\" with the value \"Metzger\" (\"current_job_title\": \"Metzger\").  When writing fields administered as historical, please note that both properties have to be entered to prevent content from being lost. This can once again be illustrated using the example above:  Starting on 01/01/2010, the person is no longer employed as a butcher (\"Metzger\"), but now works as a landlord (\"Wirt\") in the hospitality industry. In order to save this information in the master data, the request has to be as follows:  ...  \"job_titles\": [   {\"value\":\"Müller\"},   {\"value\":\"Bäcker\", \"valid_from\":\"1995-04-01T00:00:00.000\"},   {\"value\":\"Metzger\", \"valid_from\":\"2001-07-01T00:00:00.000\"},   {\"value\": \"Wirt\", \"valid_from\": \"2010-01-01T00:00:00.000\"} ],  \"current_job_title\": \"Wirt\",  ...  If the property \"current_job_title\" had not been entered, but only the property \"job_titles\", then the current value (\"landlord\" in this example) would have been overwritten by a NULL value, as there would have been no explicit entry for the current value.  If, however, only the property \"current_job_title\" had been entered (i.e. without entering the property \"job_titles\"), then all historical values would have been overwritten. The result would have been the sole value of \"landlord\" without any time period set.  In summary, it can be said that the content of the property \"current_job_title\" overwrites the content of the valid array element of the property \"job_titles\".   # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: schnittstellenberatung@datev.de
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.addressee_api import AddresseeApi
from swagger_client.api.client_api import ClientApi
from swagger_client.api.client_category_api import ClientCategoryApi
from swagger_client.api.client_group_api import ClientGroupApi
from swagger_client.api.corporate_structure_api import CorporateStructureApi
from swagger_client.api.country_code_api import CountryCodeApi
from swagger_client.api.employee_api import EmployeeApi
from swagger_client.api.institution_api import InstitutionApi
from swagger_client.api.legal_form_api import LegalFormApi
from swagger_client.api.relationship_api import RelationshipApi
from swagger_client.api.responsibility_api import ResponsibilityApi
from swagger_client.api.version_api import VersionApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.additional_message import AdditionalMessage
from swagger_client.models.address import Address
from swagger_client.models.addressee import Addressee
from swagger_client.models.area_of_responsibility import AreaOfResponsibility
from swagger_client.models.bank import Bank
from swagger_client.models.bank_account import BankAccount
from swagger_client.models.client import Client
from swagger_client.models.client_category import ClientCategory
from swagger_client.models.client_category_type import ClientCategoryType
from swagger_client.models.client_group import ClientGroup
from swagger_client.models.client_group_type import ClientGroupType
from swagger_client.models.code_of_classification_of_economic_activities2003 import CodeOfClassificationOfEconomicActivities2003
from swagger_client.models.code_of_classification_of_economic_activities2008 import CodeOfClassificationOfEconomicActivities2008
from swagger_client.models.communication import Communication
from swagger_client.models.company_name import CompanyName
from swagger_client.models.consideration import Consideration
from swagger_client.models.contact_person import ContactPerson
from swagger_client.models.corporate_structure import CorporateStructure
from swagger_client.models.country_code import CountryCode
from swagger_client.models.country_of_head_office import CountryOfHeadOffice
from swagger_client.models.deletion_log import DeletionLog
from swagger_client.models.denomination import Denomination
from swagger_client.models.description_of_classification_of_economic_activities2003 import DescriptionOfClassificationOfEconomicActivities2003
from swagger_client.models.description_of_classification_of_economic_activities2008 import DescriptionOfClassificationOfEconomicActivities2008
from swagger_client.models.detail import Detail
from swagger_client.models.distribution_of_profit import DistributionOfProfit
from swagger_client.models.employee import Employee
from swagger_client.models.enterprise_purpose import EnterprisePurpose
from swagger_client.models.error import Error
from swagger_client.models.establishment import Establishment
from swagger_client.models.federal_state import FederalState
from swagger_client.models.federal_state_mad import FederalStateMAD
from swagger_client.models.fiscal_year import FiscalYear
from swagger_client.models.functional_area import FunctionalArea
from swagger_client.models.job_title import JobTitle
from swagger_client.models.kind_of_register_court import KindOfRegisterCourt
from swagger_client.models.legal_form import LegalForm
from swagger_client.models.legal_form_id import LegalFormId
from swagger_client.models.location_of_head_office import LocationOfHeadOffice
from swagger_client.models.mad_code_of_classification_of_economic_activities2003 import MADCodeOfClassificationOfEconomicActivities2003
from swagger_client.models.mad_code_of_classification_of_economic_activities2008 import MADCodeOfClassificationOfEconomicActivities2008
from swagger_client.models.marital_status import MaritalStatus
from swagger_client.models.name_of_register_court import NameOfRegisterCourt
from swagger_client.models.next_free_number import NextFreeNumber
from swagger_client.models.registered_company_name import RegisteredCompanyName
from swagger_client.models.registration_number import RegistrationNumber
from swagger_client.models.relationship import Relationship
from swagger_client.models.relationship_type import RelationshipType
from swagger_client.models.responsibility import Responsibility
from swagger_client.models.short_name import ShortName
from swagger_client.models.surname import Surname
from swagger_client.models.tax_authority import TaxAuthority
from swagger_client.models.tax_office import TaxOffice
from swagger_client.models.version import Version
