# coding: utf-8

"""
    Client Master Data

    In the documentation below, you will receive detailed functional and technical specifications on the API DATEVconnect for Master Data.  **General information on dealing with fields administered as historical** A number of fields in the  master data are administered as \"historical\". This means that the existing content is not overwritten when the field is updated, but that the existing value remains in place, with a new value added that is valid from a date entered by the user.  Specifically, the following fields are administered as historical:  *Ressource 'addressees'* - short_names, - surnames, - company_names, - legal_form_ids  *Subordinate object 'detail'* - considerations, - denominations, - federal_states_of_natural_person, - job_titles, - marital_statuses, - codes_of_classification_of_economic_activities_2008, - descriptions_of_classification_of_economic_activities_2008, - mad_codes_of_classification_of_economic_activities_2008, - codes_of_classification_of_economic_activities_2003, - descriptions_of_classification_of_economic_activities_2003, - mad_codes_of_classification_of_economic_activities_2003, - countries_of_head_office, - distributions_of_profit, - enterprise_purposes, - federal_states_mad_of_legal_person, - federal_states_of_legal_person, - fiscal_years, - kind_of_register_courts, - locations_of_head_office, - names_of_register_court, - registered_company_names, - registration_numbers, - three_lined_company_names_first_line, - three_lined_company_names_second_line, - three_lined_company_names_third_line, - two_lined_company_names_first_line, - two_lined_company_names_second_line  These fields are shown as arrays, with their elements exhibiting the following structure: - value, - valid_from  This structure makes it possible to generate periods that indicate the validity date of a particular value in a value range.  This is illustrated by the following examples:  \"job_titles\": [   {\"value\":\"Müller\"},   {\"value\":\"Bäcker\", \"valid_from\":\"1995-04-01T00:00:00.000\"},   {\"value\":\"Metzger\", \"valid_from\":\"2001-07-01T00:00:00.000\"} ] In this example, the profession \"Müller\" (\"miller\") was valid until 03/31/1995. \"Bäcker\" (\"baker\") was valid from 04/01/1995 to 06/30/2001. The value \"Metzger\" (\"butcher\") is valid starting 07/01/2001.  For all the historically administered fields listed above, there is an additional field that indicates the current value of the value range (the value that is valid today/as of the system time). The syntactic structure of the property name is as follows: current_<*Property name of the historically administered field in the singular*>.  In the example above, the property name is \"current_job_title\" with the value \"Metzger\" (\"current_job_title\": \"Metzger\").  When writing fields administered as historical, please note that both properties have to be entered to prevent content from being lost. This can once again be illustrated using the example above:  Starting on 01/01/2010, the person is no longer employed as a butcher (\"Metzger\"), but now works as a landlord (\"Wirt\") in the hospitality industry. In order to save this information in the master data, the request has to be as follows:  ...  \"job_titles\": [   {\"value\":\"Müller\"},   {\"value\":\"Bäcker\", \"valid_from\":\"1995-04-01T00:00:00.000\"},   {\"value\":\"Metzger\", \"valid_from\":\"2001-07-01T00:00:00.000\"},   {\"value\": \"Wirt\", \"valid_from\": \"2010-01-01T00:00:00.000\"} ],  \"current_job_title\": \"Wirt\",  ...  If the property \"current_job_title\" had not been entered, but only the property \"job_titles\", then the current value (\"landlord\" in this example) would have been overwritten by a NULL value, as there would have been no explicit entry for the current value.  If, however, only the property \"current_job_title\" had been entered (i.e. without entering the property \"job_titles\"), then all historical values would have been overwritten. The result would have been the sole value of \"landlord\" without any time period set.  In summary, it can be said that the content of the property \"current_job_title\" overwrites the content of the valid array element of the property \"job_titles\".   # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: schnittstellenberatung@datev.de
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Addressee(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'eu_vat_id_country_code': 'str',
        'eu_vat_id_number': 'str',
        'short_names': 'list[ShortName]',
        'current_short_name': 'str',
        'status': 'str',
        'surrogate_name': 'str',
        'timestamp': 'date',
        'type': 'str',
        'date_of_birth': 'date',
        'etin': 'str',
        'firstname': 'str',
        'sex': 'str',
        'surnames': 'list[Surname]',
        'current_surname': 'str',
        'tax_identification_number': 'str',
        'company_names': 'list[CompanyName]',
        'current_company_name': 'str',
        'date_of_foundation': 'date',
        'legal_form_ids': 'list[LegalFormId]',
        'current_legal_form_id': 'str',
        'detail': 'Detail',
        'addresses': 'list[Address]',
        'communications': 'list[Communication]',
        'bank_accounts': 'list[BankAccount]',
        'tax_offices': 'list[TaxOffice]',
        'contact_persons': 'list[ContactPerson]'
    }

    attribute_map = {
        'id': 'id',
        'eu_vat_id_country_code': 'eu_vat_id_country_code',
        'eu_vat_id_number': 'eu_vat_id_number',
        'short_names': 'short_names',
        'current_short_name': 'current_short_name',
        'status': 'status',
        'surrogate_name': 'surrogate_name',
        'timestamp': 'timestamp',
        'type': 'type',
        'date_of_birth': 'date_of_birth',
        'etin': 'etin',
        'firstname': 'firstname',
        'sex': 'sex',
        'surnames': 'surnames',
        'current_surname': 'current_surname',
        'tax_identification_number': 'tax_identification_number',
        'company_names': 'company_names',
        'current_company_name': 'current_company_name',
        'date_of_foundation': 'date_of_foundation',
        'legal_form_ids': 'legal_form_ids',
        'current_legal_form_id': 'current_legal_form_id',
        'detail': 'detail',
        'addresses': 'addresses',
        'communications': 'communications',
        'bank_accounts': 'bank_accounts',
        'tax_offices': 'tax_offices',
        'contact_persons': 'contact_persons'
    }

    def __init__(self, id=None, eu_vat_id_country_code=None, eu_vat_id_number=None, short_names=None, current_short_name=None, status=None, surrogate_name=None, timestamp=None, type=None, date_of_birth=None, etin=None, firstname=None, sex=None, surnames=None, current_surname=None, tax_identification_number=None, company_names=None, current_company_name=None, date_of_foundation=None, legal_form_ids=None, current_legal_form_id=None, detail=None, addresses=None, communications=None, bank_accounts=None, tax_offices=None, contact_persons=None, _configuration=None):  # noqa: E501
        """Addressee - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._eu_vat_id_country_code = None
        self._eu_vat_id_number = None
        self._short_names = None
        self._current_short_name = None
        self._status = None
        self._surrogate_name = None
        self._timestamp = None
        self._type = None
        self._date_of_birth = None
        self._etin = None
        self._firstname = None
        self._sex = None
        self._surnames = None
        self._current_surname = None
        self._tax_identification_number = None
        self._company_names = None
        self._current_company_name = None
        self._date_of_foundation = None
        self._legal_form_ids = None
        self._current_legal_form_id = None
        self._detail = None
        self._addresses = None
        self._communications = None
        self._bank_accounts = None
        self._tax_offices = None
        self._contact_persons = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if eu_vat_id_country_code is not None:
            self.eu_vat_id_country_code = eu_vat_id_country_code
        if eu_vat_id_number is not None:
            self.eu_vat_id_number = eu_vat_id_number
        if short_names is not None:
            self.short_names = short_names
        if current_short_name is not None:
            self.current_short_name = current_short_name
        if status is not None:
            self.status = status
        if surrogate_name is not None:
            self.surrogate_name = surrogate_name
        if timestamp is not None:
            self.timestamp = timestamp
        self.type = type
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if etin is not None:
            self.etin = etin
        if firstname is not None:
            self.firstname = firstname
        if sex is not None:
            self.sex = sex
        if surnames is not None:
            self.surnames = surnames
        if current_surname is not None:
            self.current_surname = current_surname
        if tax_identification_number is not None:
            self.tax_identification_number = tax_identification_number
        if company_names is not None:
            self.company_names = company_names
        if current_company_name is not None:
            self.current_company_name = current_company_name
        if date_of_foundation is not None:
            self.date_of_foundation = date_of_foundation
        if legal_form_ids is not None:
            self.legal_form_ids = legal_form_ids
        if current_legal_form_id is not None:
            self.current_legal_form_id = current_legal_form_id
        if detail is not None:
            self.detail = detail
        if addresses is not None:
            self.addresses = addresses
        if communications is not None:
            self.communications = communications
        if bank_accounts is not None:
            self.bank_accounts = bank_accounts
        if tax_offices is not None:
            self.tax_offices = tax_offices
        if contact_persons is not None:
            self.contact_persons = contact_persons

    @property
    def id(self):
        """Gets the id of this Addressee.  # noqa: E501

        GUID of an addressee – internal identifier. The ID may not be entered with POST (it is issued by the system); with PUT, however, the ID is a mandatory field.   # noqa: E501

        :return: The id of this Addressee.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Addressee.

        GUID of an addressee – internal identifier. The ID may not be entered with POST (it is issued by the system); with PUT, however, the ID is a mandatory field.   # noqa: E501

        :param id: The id of this Addressee.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def eu_vat_id_country_code(self):
        """Gets the eu_vat_id_country_code of this Addressee.  # noqa: E501

        VAT ID country codes (AT = Österreich, BE = Belgien, BG = Bulgarien, CY = Zypern, CZ = Tschechische Republik, DE = Deutschland, DK = Dänemark, EE = Estland, EL = Griechenland, ES = Spanien, EU = Europäische Union, FI = Finnland, FR = Frankreich, GB = Großbritannien, HR = Kroatien, HU = Ungarn, IE = Irland, IT = Italien, LT = Litauen, LU = Luxemburg, LV = Lettland, MT = Malta, NL = Niederlande, PL = Polen, PT = Portugal, RO = Rumänien, SE = Schweden, SI = Slowenien, SK = Slowakei, XI = Nordirland).  # noqa: E501

        :return: The eu_vat_id_country_code of this Addressee.  # noqa: E501
        :rtype: str
        """
        return self._eu_vat_id_country_code

    @eu_vat_id_country_code.setter
    def eu_vat_id_country_code(self, eu_vat_id_country_code):
        """Sets the eu_vat_id_country_code of this Addressee.

        VAT ID country codes (AT = Österreich, BE = Belgien, BG = Bulgarien, CY = Zypern, CZ = Tschechische Republik, DE = Deutschland, DK = Dänemark, EE = Estland, EL = Griechenland, ES = Spanien, EU = Europäische Union, FI = Finnland, FR = Frankreich, GB = Großbritannien, HR = Kroatien, HU = Ungarn, IE = Irland, IT = Italien, LT = Litauen, LU = Luxemburg, LV = Lettland, MT = Malta, NL = Niederlande, PL = Polen, PT = Portugal, RO = Rumänien, SE = Schweden, SI = Slowenien, SK = Slowakei, XI = Nordirland).  # noqa: E501

        :param eu_vat_id_country_code: The eu_vat_id_country_code of this Addressee.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                eu_vat_id_country_code is not None and len(eu_vat_id_country_code) > 2):
            raise ValueError("Invalid value for `eu_vat_id_country_code`, length must be less than or equal to `2`")  # noqa: E501

        self._eu_vat_id_country_code = eu_vat_id_country_code

    @property
    def eu_vat_id_number(self):
        """Gets the eu_vat_id_number of this Addressee.  # noqa: E501

        VAT ID without country code.  # noqa: E501

        :return: The eu_vat_id_number of this Addressee.  # noqa: E501
        :rtype: str
        """
        return self._eu_vat_id_number

    @eu_vat_id_number.setter
    def eu_vat_id_number(self, eu_vat_id_number):
        """Sets the eu_vat_id_number of this Addressee.

        VAT ID without country code.  # noqa: E501

        :param eu_vat_id_number: The eu_vat_id_number of this Addressee.  # noqa: E501
        :type: str
        """

        self._eu_vat_id_number = eu_vat_id_number

    @property
    def short_names(self):
        """Gets the short_names of this Addressee.  # noqa: E501


        :return: The short_names of this Addressee.  # noqa: E501
        :rtype: list[ShortName]
        """
        return self._short_names

    @short_names.setter
    def short_names(self, short_names):
        """Sets the short_names of this Addressee.


        :param short_names: The short_names of this Addressee.  # noqa: E501
        :type: list[ShortName]
        """

        self._short_names = short_names

    @property
    def current_short_name(self):
        """Gets the current_short_name of this Addressee.  # noqa: E501

        Current short name of the addressee (= value as at system date).  # noqa: E501

        :return: The current_short_name of this Addressee.  # noqa: E501
        :rtype: str
        """
        return self._current_short_name

    @current_short_name.setter
    def current_short_name(self, current_short_name):
        """Sets the current_short_name of this Addressee.

        Current short name of the addressee (= value as at system date).  # noqa: E501

        :param current_short_name: The current_short_name of this Addressee.  # noqa: E501
        :type: str
        """

        self._current_short_name = current_short_name

    @property
    def status(self):
        """Gets the status of this Addressee.  # noqa: E501

        Indicates whether the addressee is active or inactive.   # noqa: E501

        :return: The status of this Addressee.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Addressee.

        Indicates whether the addressee is active or inactive.   # noqa: E501

        :param status: The status of this Addressee.  # noqa: E501
        :type: str
        """
        allowed_values = ["inactive", "active"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def surrogate_name(self):
        """Gets the surrogate_name of this Addressee.  # noqa: E501

        Alias of an addressee for search purposes.  # noqa: E501

        :return: The surrogate_name of this Addressee.  # noqa: E501
        :rtype: str
        """
        return self._surrogate_name

    @surrogate_name.setter
    def surrogate_name(self, surrogate_name):
        """Sets the surrogate_name of this Addressee.

        Alias of an addressee for search purposes.  # noqa: E501

        :param surrogate_name: The surrogate_name of this Addressee.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                surrogate_name is not None and len(surrogate_name) > 50):
            raise ValueError("Invalid value for `surrogate_name`, length must be less than or equal to `50`")  # noqa: E501

        self._surrogate_name = surrogate_name

    @property
    def timestamp(self):
        """Gets the timestamp of this Addressee.  # noqa: E501

        Indicates when the addressee was last edited.  # noqa: E501

        :return: The timestamp of this Addressee.  # noqa: E501
        :rtype: date
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Addressee.

        Indicates when the addressee was last edited.  # noqa: E501

        :param timestamp: The timestamp of this Addressee.  # noqa: E501
        :type: date
        """

        self._timestamp = timestamp

    @property
    def type(self):
        """Gets the type of this Addressee.  # noqa: E501

        Indicates whether the addressee is a person or an enterprise. With PUT, the content of this property may not be changed.  # noqa: E501

        :return: The type of this Addressee.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Addressee.

        Indicates whether the addressee is a person or an enterprise. With PUT, the content of this property may not be changed.  # noqa: E501

        :param type: The type of this Addressee.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["natural_person", "legal_person"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this Addressee.  # noqa: E501

        Date of birth of a natural person.<br><br>The property may only be filled if the addressee is of the type 'natural_person'.  # noqa: E501

        :return: The date_of_birth of this Addressee.  # noqa: E501
        :rtype: date
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this Addressee.

        Date of birth of a natural person.<br><br>The property may only be filled if the addressee is of the type 'natural_person'.  # noqa: E501

        :param date_of_birth: The date_of_birth of this Addressee.  # noqa: E501
        :type: date
        """

        self._date_of_birth = date_of_birth

    @property
    def etin(self):
        """Gets the etin of this Addressee.  # noqa: E501

        The eTIN is an income tax-related identification number given to every employee in Germany; the legal basis is Section 41b (2) of the German Income Tax Act (EStG). However, the calculation method does not exclude the possibility that the same eTIN might be assigned to more than one person. As it is sufficiently unlikely, however, that two different people with the same eTIN fall within the jurisdiction of the same tax authority, this is acceptable for the purposes of the eTIN. The eTIN is a 14-character code that is made up of the following personal data; last name, first name, and date of birth; it comprises the upper-case letters A to Z, as well as the digits 0 to 9. As long as this personal data does not change (e.g. a change of name upon marriage), the eTIN will remain valid; otherwise, it has to be amended to reflect the change in name.<br><br>The property may only be filled if the addressee is of the type 'natural_person'.  # noqa: E501

        :return: The etin of this Addressee.  # noqa: E501
        :rtype: str
        """
        return self._etin

    @etin.setter
    def etin(self, etin):
        """Sets the etin of this Addressee.

        The eTIN is an income tax-related identification number given to every employee in Germany; the legal basis is Section 41b (2) of the German Income Tax Act (EStG). However, the calculation method does not exclude the possibility that the same eTIN might be assigned to more than one person. As it is sufficiently unlikely, however, that two different people with the same eTIN fall within the jurisdiction of the same tax authority, this is acceptable for the purposes of the eTIN. The eTIN is a 14-character code that is made up of the following personal data; last name, first name, and date of birth; it comprises the upper-case letters A to Z, as well as the digits 0 to 9. As long as this personal data does not change (e.g. a change of name upon marriage), the eTIN will remain valid; otherwise, it has to be amended to reflect the change in name.<br><br>The property may only be filled if the addressee is of the type 'natural_person'.  # noqa: E501

        :param etin: The etin of this Addressee.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                etin is not None and not re.search(r'^[A-Z]{8}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}$', etin)):  # noqa: E501
            raise ValueError(r"Invalid value for `etin`, must be a follow pattern or equal to `/^[A-Z]{8}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}$/`")  # noqa: E501

        self._etin = etin

    @property
    def firstname(self):
        """Gets the firstname of this Addressee.  # noqa: E501

        First name of a natural person.<br><br>The property may only be filled if the addressee is of the type 'natural_person'.  # noqa: E501

        :return: The firstname of this Addressee.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this Addressee.

        First name of a natural person.<br><br>The property may only be filled if the addressee is of the type 'natural_person'.  # noqa: E501

        :param firstname: The firstname of this Addressee.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                firstname is not None and len(firstname) > 30):
            raise ValueError("Invalid value for `firstname`, length must be less than or equal to `30`")  # noqa: E501

        self._firstname = firstname

    @property
    def sex(self):
        """Gets the sex of this Addressee.  # noqa: E501

        Gender of a natural person.<br><br>The property may only be filled if the addressee is of the type 'natural_person'.  # noqa: E501

        :return: The sex of this Addressee.  # noqa: E501
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this Addressee.

        Gender of a natural person.<br><br>The property may only be filled if the addressee is of the type 'natural_person'.  # noqa: E501

        :param sex: The sex of this Addressee.  # noqa: E501
        :type: str
        """
        allowed_values = ["male", "female", "diverse"]  # noqa: E501
        if (self._configuration.client_side_validation and
                sex not in allowed_values):
            raise ValueError(
                "Invalid value for `sex` ({0}), must be one of {1}"  # noqa: E501
                .format(sex, allowed_values)
            )

        self._sex = sex

    @property
    def surnames(self):
        """Gets the surnames of this Addressee.  # noqa: E501

        The property may only be filled if the addressee is of the type 'natural_person'.  # noqa: E501

        :return: The surnames of this Addressee.  # noqa: E501
        :rtype: list[Surname]
        """
        return self._surnames

    @surnames.setter
    def surnames(self, surnames):
        """Sets the surnames of this Addressee.

        The property may only be filled if the addressee is of the type 'natural_person'.  # noqa: E501

        :param surnames: The surnames of this Addressee.  # noqa: E501
        :type: list[Surname]
        """

        self._surnames = surnames

    @property
    def current_surname(self):
        """Gets the current_surname of this Addressee.  # noqa: E501

        Current last name of a natural person (= value as at system date). Mandatory field if you wish to create an addressee of the type \"natural_person\".<br><br>The property may only be filled if the addressee is of the type 'natural_person'.  # noqa: E501

        :return: The current_surname of this Addressee.  # noqa: E501
        :rtype: str
        """
        return self._current_surname

    @current_surname.setter
    def current_surname(self, current_surname):
        """Sets the current_surname of this Addressee.

        Current last name of a natural person (= value as at system date). Mandatory field if you wish to create an addressee of the type \"natural_person\".<br><br>The property may only be filled if the addressee is of the type 'natural_person'.  # noqa: E501

        :param current_surname: The current_surname of this Addressee.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                current_surname is not None and len(current_surname) > 30):
            raise ValueError("Invalid value for `current_surname`, length must be less than or equal to `30`")  # noqa: E501

        self._current_surname = current_surname

    @property
    def tax_identification_number(self):
        """Gets the tax_identification_number of this Addressee.  # noqa: E501

        Unique tax identification number for natural persons as per Section 139b of the German Fiscal Code (AO).<br><br>The property may only be filled if the addressee is of the type 'natural_person'.  # noqa: E501

        :return: The tax_identification_number of this Addressee.  # noqa: E501
        :rtype: str
        """
        return self._tax_identification_number

    @tax_identification_number.setter
    def tax_identification_number(self, tax_identification_number):
        """Sets the tax_identification_number of this Addressee.

        Unique tax identification number for natural persons as per Section 139b of the German Fiscal Code (AO).<br><br>The property may only be filled if the addressee is of the type 'natural_person'.  # noqa: E501

        :param tax_identification_number: The tax_identification_number of this Addressee.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                tax_identification_number is not None and not re.search(r'^([1-9]\\d{10})$', tax_identification_number)):  # noqa: E501
            raise ValueError(r"Invalid value for `tax_identification_number`, must be a follow pattern or equal to `/^([1-9]\\d{10})$/`")  # noqa: E501

        self._tax_identification_number = tax_identification_number

    @property
    def company_names(self):
        """Gets the company_names of this Addressee.  # noqa: E501

        The property may only be filled if the addressee is of the type 'legal_person'.  # noqa: E501

        :return: The company_names of this Addressee.  # noqa: E501
        :rtype: list[CompanyName]
        """
        return self._company_names

    @company_names.setter
    def company_names(self, company_names):
        """Sets the company_names of this Addressee.

        The property may only be filled if the addressee is of the type 'legal_person'.  # noqa: E501

        :param company_names: The company_names of this Addressee.  # noqa: E501
        :type: list[CompanyName]
        """

        self._company_names = company_names

    @property
    def current_company_name(self):
        """Gets the current_company_name of this Addressee.  # noqa: E501

        Current company name (= value as at system date). Mandatory field if you wish to create an addressee of the type \"legal_person\".<br><br>The property may only be filled if the addressee is of the type 'legal_person'.  # noqa: E501

        :return: The current_company_name of this Addressee.  # noqa: E501
        :rtype: str
        """
        return self._current_company_name

    @current_company_name.setter
    def current_company_name(self, current_company_name):
        """Sets the current_company_name of this Addressee.

        Current company name (= value as at system date). Mandatory field if you wish to create an addressee of the type \"legal_person\".<br><br>The property may only be filled if the addressee is of the type 'legal_person'.  # noqa: E501

        :param current_company_name: The current_company_name of this Addressee.  # noqa: E501
        :type: str
        """

        self._current_company_name = current_company_name

    @property
    def date_of_foundation(self):
        """Gets the date_of_foundation of this Addressee.  # noqa: E501

        Date on which an operational commercial enterprise is established (date of foundation).<br><br>The property may only be filled if the addressee is of the type 'legal_person'.  # noqa: E501

        :return: The date_of_foundation of this Addressee.  # noqa: E501
        :rtype: date
        """
        return self._date_of_foundation

    @date_of_foundation.setter
    def date_of_foundation(self, date_of_foundation):
        """Sets the date_of_foundation of this Addressee.

        Date on which an operational commercial enterprise is established (date of foundation).<br><br>The property may only be filled if the addressee is of the type 'legal_person'.  # noqa: E501

        :param date_of_foundation: The date_of_foundation of this Addressee.  # noqa: E501
        :type: date
        """

        self._date_of_foundation = date_of_foundation

    @property
    def legal_form_ids(self):
        """Gets the legal_form_ids of this Addressee.  # noqa: E501

        The property may only be filled if the addressee is of the type 'legal_person'.  # noqa: E501

        :return: The legal_form_ids of this Addressee.  # noqa: E501
        :rtype: list[LegalFormId]
        """
        return self._legal_form_ids

    @legal_form_ids.setter
    def legal_form_ids(self, legal_form_ids):
        """Sets the legal_form_ids of this Addressee.

        The property may only be filled if the addressee is of the type 'legal_person'.  # noqa: E501

        :param legal_form_ids: The legal_form_ids of this Addressee.  # noqa: E501
        :type: list[LegalFormId]
        """

        self._legal_form_ids = legal_form_ids

    @property
    def current_legal_form_id(self):
        """Gets the current_legal_form_id of this Addressee.  # noqa: E501

        Current legal form of the enterprise (= value as at system date).<br><br>The property may only be filled if the addressee is of the type 'legal_person'.  # noqa: E501

        :return: The current_legal_form_id of this Addressee.  # noqa: E501
        :rtype: str
        """
        return self._current_legal_form_id

    @current_legal_form_id.setter
    def current_legal_form_id(self, current_legal_form_id):
        """Sets the current_legal_form_id of this Addressee.

        Current legal form of the enterprise (= value as at system date).<br><br>The property may only be filled if the addressee is of the type 'legal_person'.  # noqa: E501

        :param current_legal_form_id: The current_legal_form_id of this Addressee.  # noqa: E501
        :type: str
        """

        self._current_legal_form_id = current_legal_form_id

    @property
    def detail(self):
        """Gets the detail of this Addressee.  # noqa: E501


        :return: The detail of this Addressee.  # noqa: E501
        :rtype: Detail
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this Addressee.


        :param detail: The detail of this Addressee.  # noqa: E501
        :type: Detail
        """

        self._detail = detail

    @property
    def addresses(self):
        """Gets the addresses of this Addressee.  # noqa: E501


        :return: The addresses of this Addressee.  # noqa: E501
        :rtype: list[Address]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this Addressee.


        :param addresses: The addresses of this Addressee.  # noqa: E501
        :type: list[Address]
        """

        self._addresses = addresses

    @property
    def communications(self):
        """Gets the communications of this Addressee.  # noqa: E501


        :return: The communications of this Addressee.  # noqa: E501
        :rtype: list[Communication]
        """
        return self._communications

    @communications.setter
    def communications(self, communications):
        """Sets the communications of this Addressee.


        :param communications: The communications of this Addressee.  # noqa: E501
        :type: list[Communication]
        """

        self._communications = communications

    @property
    def bank_accounts(self):
        """Gets the bank_accounts of this Addressee.  # noqa: E501


        :return: The bank_accounts of this Addressee.  # noqa: E501
        :rtype: list[BankAccount]
        """
        return self._bank_accounts

    @bank_accounts.setter
    def bank_accounts(self, bank_accounts):
        """Sets the bank_accounts of this Addressee.


        :param bank_accounts: The bank_accounts of this Addressee.  # noqa: E501
        :type: list[BankAccount]
        """

        self._bank_accounts = bank_accounts

    @property
    def tax_offices(self):
        """Gets the tax_offices of this Addressee.  # noqa: E501


        :return: The tax_offices of this Addressee.  # noqa: E501
        :rtype: list[TaxOffice]
        """
        return self._tax_offices

    @tax_offices.setter
    def tax_offices(self, tax_offices):
        """Sets the tax_offices of this Addressee.


        :param tax_offices: The tax_offices of this Addressee.  # noqa: E501
        :type: list[TaxOffice]
        """

        self._tax_offices = tax_offices

    @property
    def contact_persons(self):
        """Gets the contact_persons of this Addressee.  # noqa: E501


        :return: The contact_persons of this Addressee.  # noqa: E501
        :rtype: list[ContactPerson]
        """
        return self._contact_persons

    @contact_persons.setter
    def contact_persons(self, contact_persons):
        """Sets the contact_persons of this Addressee.


        :param contact_persons: The contact_persons of this Addressee.  # noqa: E501
        :type: list[ContactPerson]
        """

        self._contact_persons = contact_persons

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Addressee, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Addressee):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Addressee):
            return True

        return self.to_dict() != other.to_dict()