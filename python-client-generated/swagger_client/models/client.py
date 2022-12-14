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


class Client(object):
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
        'client_since': 'date',
        'client_to': 'date',
        'differing_name': 'str',
        'legal_person_id': 'str',
        'name': 'str',
        'natural_person_id': 'str',
        'note': 'str',
        'number': 'int',
        'status': 'str',
        'timestamp': 'date',
        'type': 'str',
        'organization_id': 'str',
        'organization_name': 'str',
        'organization_number': 'int',
        'establishment_id': 'str',
        'establishment_name': 'str',
        'establishment_number': 'int',
        'establishment_short_name': 'str',
        'functional_area_id': 'str',
        'functional_area_name': 'str',
        'functional_area_short_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'client_since': 'client_since',
        'client_to': 'client_to',
        'differing_name': 'differing_name',
        'legal_person_id': 'legal_person_id',
        'name': 'name',
        'natural_person_id': 'natural_person_id',
        'note': 'note',
        'number': 'number',
        'status': 'status',
        'timestamp': 'timestamp',
        'type': 'type',
        'organization_id': 'organization_id',
        'organization_name': 'organization_name',
        'organization_number': 'organization_number',
        'establishment_id': 'establishment_id',
        'establishment_name': 'establishment_name',
        'establishment_number': 'establishment_number',
        'establishment_short_name': 'establishment_short_name',
        'functional_area_id': 'functional_area_id',
        'functional_area_name': 'functional_area_name',
        'functional_area_short_name': 'functional_area_short_name'
    }

    def __init__(self, id=None, client_since=None, client_to=None, differing_name=None, legal_person_id=None, name=None, natural_person_id=None, note=None, number=None, status=None, timestamp=None, type=None, organization_id=None, organization_name=None, organization_number=None, establishment_id=None, establishment_name=None, establishment_number=None, establishment_short_name=None, functional_area_id=None, functional_area_name=None, functional_area_short_name=None, _configuration=None):  # noqa: E501
        """Client - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._client_since = None
        self._client_to = None
        self._differing_name = None
        self._legal_person_id = None
        self._name = None
        self._natural_person_id = None
        self._note = None
        self._number = None
        self._status = None
        self._timestamp = None
        self._type = None
        self._organization_id = None
        self._organization_name = None
        self._organization_number = None
        self._establishment_id = None
        self._establishment_name = None
        self._establishment_number = None
        self._establishment_short_name = None
        self._functional_area_id = None
        self._functional_area_name = None
        self._functional_area_short_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if client_since is not None:
            self.client_since = client_since
        if client_to is not None:
            self.client_to = client_to
        if differing_name is not None:
            self.differing_name = differing_name
        if legal_person_id is not None:
            self.legal_person_id = legal_person_id
        self.name = name
        if natural_person_id is not None:
            self.natural_person_id = natural_person_id
        if note is not None:
            self.note = note
        self.number = number
        if status is not None:
            self.status = status
        if timestamp is not None:
            self.timestamp = timestamp
        self.type = type
        if organization_id is not None:
            self.organization_id = organization_id
        if organization_name is not None:
            self.organization_name = organization_name
        if organization_number is not None:
            self.organization_number = organization_number
        if establishment_id is not None:
            self.establishment_id = establishment_id
        if establishment_name is not None:
            self.establishment_name = establishment_name
        if establishment_number is not None:
            self.establishment_number = establishment_number
        if establishment_short_name is not None:
            self.establishment_short_name = establishment_short_name
        if functional_area_id is not None:
            self.functional_area_id = functional_area_id
        if functional_area_name is not None:
            self.functional_area_name = functional_area_name
        if functional_area_short_name is not None:
            self.functional_area_short_name = functional_area_short_name

    @property
    def id(self):
        """Gets the id of this Client.  # noqa: E501

        GUID of a client – internal identifier. The ID may not be entered with POST (it is issued by the system); with PUT, however, the ID is a mandatory field.   # noqa: E501

        :return: The id of this Client.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Client.

        GUID of a client – internal identifier. The ID may not be entered with POST (it is issued by the system); with PUT, however, the ID is a mandatory field.   # noqa: E501

        :param id: The id of this Client.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def client_since(self):
        """Gets the client_since of this Client.  # noqa: E501

        Indicates the start date of a client relationship.  # noqa: E501

        :return: The client_since of this Client.  # noqa: E501
        :rtype: date
        """
        return self._client_since

    @client_since.setter
    def client_since(self, client_since):
        """Sets the client_since of this Client.

        Indicates the start date of a client relationship.  # noqa: E501

        :param client_since: The client_since of this Client.  # noqa: E501
        :type: date
        """

        self._client_since = client_since

    @property
    def client_to(self):
        """Gets the client_to of this Client.  # noqa: E501

        Indicates the end date of a client relationship.  # noqa: E501

        :return: The client_to of this Client.  # noqa: E501
        :rtype: date
        """
        return self._client_to

    @client_to.setter
    def client_to(self, client_to):
        """Sets the client_to of this Client.

        Indicates the end date of a client relationship.  # noqa: E501

        :param client_to: The client_to of this Client.  # noqa: E501
        :type: date
        """

        self._client_to = client_to

    @property
    def differing_name(self):
        """Gets the differing_name of this Client.  # noqa: E501

        Differing client name.  # noqa: E501

        :return: The differing_name of this Client.  # noqa: E501
        :rtype: str
        """
        return self._differing_name

    @differing_name.setter
    def differing_name(self, differing_name):
        """Sets the differing_name of this Client.

        Differing client name.  # noqa: E501

        :param differing_name: The differing_name of this Client.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                differing_name is not None and len(differing_name) > 30):
            raise ValueError("Invalid value for `differing_name`, length must be less than or equal to `30`")  # noqa: E501

        self._differing_name = differing_name

    @property
    def legal_person_id(self):
        """Gets the legal_person_id of this Client.  # noqa: E501

        GUID of an enterprise - internal identifier. Reference to the enterprise that is a client (client addressee).   # noqa: E501

        :return: The legal_person_id of this Client.  # noqa: E501
        :rtype: str
        """
        return self._legal_person_id

    @legal_person_id.setter
    def legal_person_id(self, legal_person_id):
        """Sets the legal_person_id of this Client.

        GUID of an enterprise - internal identifier. Reference to the enterprise that is a client (client addressee).   # noqa: E501

        :param legal_person_id: The legal_person_id of this Client.  # noqa: E501
        :type: str
        """

        self._legal_person_id = legal_person_id

    @property
    def name(self):
        """Gets the name of this Client.  # noqa: E501

        Name of the client.  # noqa: E501

        :return: The name of this Client.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Client.

        Name of the client.  # noqa: E501

        :param name: The name of this Client.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 30):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `30`")  # noqa: E501

        self._name = name

    @property
    def natural_person_id(self):
        """Gets the natural_person_id of this Client.  # noqa: E501

        GUID of a person – internal identifier. Reference to the person who is a client (client addressee).   # noqa: E501

        :return: The natural_person_id of this Client.  # noqa: E501
        :rtype: str
        """
        return self._natural_person_id

    @natural_person_id.setter
    def natural_person_id(self, natural_person_id):
        """Sets the natural_person_id of this Client.

        GUID of a person – internal identifier. Reference to the person who is a client (client addressee).   # noqa: E501

        :param natural_person_id: The natural_person_id of this Client.  # noqa: E501
        :type: str
        """

        self._natural_person_id = natural_person_id

    @property
    def note(self):
        """Gets the note of this Client.  # noqa: E501

        Note about a client relationship (free text).  # noqa: E501

        :return: The note of this Client.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this Client.

        Note about a client relationship (free text).  # noqa: E501

        :param note: The note of this Client.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                note is not None and len(note) > 65535):
            raise ValueError("Invalid value for `note`, length must be less than or equal to `65535`")  # noqa: E501

        self._note = note

    @property
    def number(self):
        """Gets the number of this Client.  # noqa: E501

        Central client number. If the client number is issued automatically (by the server), the query parameter \"max-number\" also has to be used. The central client number then represents the smallest available client number; the value entered in the parameter represents the largest possible client number. Within this range (central client number/max-number), the server will automatically issue the client number. If there are no available client numbers left, error code 400 will be returned.   # noqa: E501

        :return: The number of this Client.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Client.

        Central client number. If the client number is issued automatically (by the server), the query parameter \"max-number\" also has to be used. The central client number then represents the smallest available client number; the value entered in the parameter represents the largest possible client number. Within this range (central client number/max-number), the server will automatically issue the client number. If there are no available client numbers left, error code 400 will be returned.   # noqa: E501

        :param number: The number of this Client.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                number is not None and number > 999999999):  # noqa: E501
            raise ValueError("Invalid value for `number`, must be a value less than or equal to `999999999`")  # noqa: E501
        if (self._configuration.client_side_validation and
                number is not None and number < 1):  # noqa: E501
            raise ValueError("Invalid value for `number`, must be a value greater than or equal to `1`")  # noqa: E501

        self._number = number

    @property
    def status(self):
        """Gets the status of this Client.  # noqa: E501

        Indicates whether the client relationship is active or inactive.  # noqa: E501

        :return: The status of this Client.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Client.

        Indicates whether the client relationship is active or inactive.  # noqa: E501

        :param status: The status of this Client.  # noqa: E501
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
    def timestamp(self):
        """Gets the timestamp of this Client.  # noqa: E501

        Indicates when the client was last edited.  # noqa: E501

        :return: The timestamp of this Client.  # noqa: E501
        :rtype: date
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Client.

        Indicates when the client was last edited.  # noqa: E501

        :param timestamp: The timestamp of this Client.  # noqa: E501
        :type: date
        """

        self._timestamp = timestamp

    @property
    def type(self):
        """Gets the type of this Client.  # noqa: E501

        Key that describes the type of client.  # noqa: E501

        :return: The type of this Client.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Client.

        Key that describes the type of client.  # noqa: E501

        :param type: The type of this Client.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["natural_person", "individual_enterprise", "legal_person"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def organization_id(self):
        """Gets the organization_id of this Client.  # noqa: E501

        GUID of an organization - internal identifier.  Indicates the GUID of the organization to which the client is assigned. This property may not be changed. The assignment can only be changed via the property 'establishment_id'. Only relevant if the package 'Unternehmensstrukturen' is installed.   # noqa: E501

        :return: The organization_id of this Client.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Client.

        GUID of an organization - internal identifier.  Indicates the GUID of the organization to which the client is assigned. This property may not be changed. The assignment can only be changed via the property 'establishment_id'. Only relevant if the package 'Unternehmensstrukturen' is installed.   # noqa: E501

        :param organization_id: The organization_id of this Client.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def organization_name(self):
        """Gets the organization_name of this Client.  # noqa: E501

        Indicates the name of the organization to which the client is assigned. Only relevant if the package 'Unternehmensstrukturen' is installed.   # noqa: E501

        :return: The organization_name of this Client.  # noqa: E501
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """Sets the organization_name of this Client.

        Indicates the name of the organization to which the client is assigned. Only relevant if the package 'Unternehmensstrukturen' is installed.   # noqa: E501

        :param organization_name: The organization_name of this Client.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                organization_name is not None and len(organization_name) > 30):
            raise ValueError("Invalid value for `organization_name`, length must be less than or equal to `30`")  # noqa: E501

        self._organization_name = organization_name

    @property
    def organization_number(self):
        """Gets the organization_number of this Client.  # noqa: E501

        Indicates the number of the organization to which the client is assigned. Only relevant if the package 'Unternehmensstrukturen' is installed.   # noqa: E501

        :return: The organization_number of this Client.  # noqa: E501
        :rtype: int
        """
        return self._organization_number

    @organization_number.setter
    def organization_number(self, organization_number):
        """Sets the organization_number of this Client.

        Indicates the number of the organization to which the client is assigned. Only relevant if the package 'Unternehmensstrukturen' is installed.   # noqa: E501

        :param organization_number: The organization_number of this Client.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                organization_number is not None and organization_number > 999999999):  # noqa: E501
            raise ValueError("Invalid value for `organization_number`, must be a value less than or equal to `999999999`")  # noqa: E501
        if (self._configuration.client_side_validation and
                organization_number is not None and organization_number < 1):  # noqa: E501
            raise ValueError("Invalid value for `organization_number`, must be a value greater than or equal to `1`")  # noqa: E501

        self._organization_number = organization_number

    @property
    def establishment_id(self):
        """Gets the establishment_id of this Client.  # noqa: E501

        GUID of an establishment - internal identifier. Indicates the GUID of the establishment to which the client is assigned. Only relevant if the package 'Unternehmensstrukturen' is installed.   # noqa: E501

        :return: The establishment_id of this Client.  # noqa: E501
        :rtype: str
        """
        return self._establishment_id

    @establishment_id.setter
    def establishment_id(self, establishment_id):
        """Sets the establishment_id of this Client.

        GUID of an establishment - internal identifier. Indicates the GUID of the establishment to which the client is assigned. Only relevant if the package 'Unternehmensstrukturen' is installed.   # noqa: E501

        :param establishment_id: The establishment_id of this Client.  # noqa: E501
        :type: str
        """

        self._establishment_id = establishment_id

    @property
    def establishment_name(self):
        """Gets the establishment_name of this Client.  # noqa: E501

        Indicates the name of the establishment to which the client is assigned. Only relevant if the package 'Unternehmensstrukturen' is installed.   # noqa: E501

        :return: The establishment_name of this Client.  # noqa: E501
        :rtype: str
        """
        return self._establishment_name

    @establishment_name.setter
    def establishment_name(self, establishment_name):
        """Sets the establishment_name of this Client.

        Indicates the name of the establishment to which the client is assigned. Only relevant if the package 'Unternehmensstrukturen' is installed.   # noqa: E501

        :param establishment_name: The establishment_name of this Client.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                establishment_name is not None and len(establishment_name) > 30):
            raise ValueError("Invalid value for `establishment_name`, length must be less than or equal to `30`")  # noqa: E501

        self._establishment_name = establishment_name

    @property
    def establishment_number(self):
        """Gets the establishment_number of this Client.  # noqa: E501

        Indicates the number of the establishment to which the client is assigned. Only relevant if the package 'Unternehmensstrukturen' is installed.   # noqa: E501

        :return: The establishment_number of this Client.  # noqa: E501
        :rtype: int
        """
        return self._establishment_number

    @establishment_number.setter
    def establishment_number(self, establishment_number):
        """Sets the establishment_number of this Client.

        Indicates the number of the establishment to which the client is assigned. Only relevant if the package 'Unternehmensstrukturen' is installed.   # noqa: E501

        :param establishment_number: The establishment_number of this Client.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                establishment_number is not None and establishment_number > 999):  # noqa: E501
            raise ValueError("Invalid value for `establishment_number`, must be a value less than or equal to `999`")  # noqa: E501
        if (self._configuration.client_side_validation and
                establishment_number is not None and establishment_number < 1):  # noqa: E501
            raise ValueError("Invalid value for `establishment_number`, must be a value greater than or equal to `1`")  # noqa: E501

        self._establishment_number = establishment_number

    @property
    def establishment_short_name(self):
        """Gets the establishment_short_name of this Client.  # noqa: E501

        Indicates the short name of the establishment to which the client is assigned. Only relevant if the package 'Unternehmensstrukturen' is installed.   # noqa: E501

        :return: The establishment_short_name of this Client.  # noqa: E501
        :rtype: str
        """
        return self._establishment_short_name

    @establishment_short_name.setter
    def establishment_short_name(self, establishment_short_name):
        """Sets the establishment_short_name of this Client.

        Indicates the short name of the establishment to which the client is assigned. Only relevant if the package 'Unternehmensstrukturen' is installed.   # noqa: E501

        :param establishment_short_name: The establishment_short_name of this Client.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                establishment_short_name is not None and len(establishment_short_name) > 10):
            raise ValueError("Invalid value for `establishment_short_name`, length must be less than or equal to `10`")  # noqa: E501

        self._establishment_short_name = establishment_short_name

    @property
    def functional_area_id(self):
        """Gets the functional_area_id of this Client.  # noqa: E501

        GUID of a functional area - internal identifier. Indicates the GUID of the functional area to which the client is assigned. Only relevant if the package 'Eigenorganisation comfort' is installed.   # noqa: E501

        :return: The functional_area_id of this Client.  # noqa: E501
        :rtype: str
        """
        return self._functional_area_id

    @functional_area_id.setter
    def functional_area_id(self, functional_area_id):
        """Sets the functional_area_id of this Client.

        GUID of a functional area - internal identifier. Indicates the GUID of the functional area to which the client is assigned. Only relevant if the package 'Eigenorganisation comfort' is installed.   # noqa: E501

        :param functional_area_id: The functional_area_id of this Client.  # noqa: E501
        :type: str
        """

        self._functional_area_id = functional_area_id

    @property
    def functional_area_name(self):
        """Gets the functional_area_name of this Client.  # noqa: E501

        Indicates the name of the functional area to which the client is assigned. Only relevant if the package 'Eigenorganisation comfort' is installed.   # noqa: E501

        :return: The functional_area_name of this Client.  # noqa: E501
        :rtype: str
        """
        return self._functional_area_name

    @functional_area_name.setter
    def functional_area_name(self, functional_area_name):
        """Sets the functional_area_name of this Client.

        Indicates the name of the functional area to which the client is assigned. Only relevant if the package 'Eigenorganisation comfort' is installed.   # noqa: E501

        :param functional_area_name: The functional_area_name of this Client.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                functional_area_name is not None and len(functional_area_name) > 30):
            raise ValueError("Invalid value for `functional_area_name`, length must be less than or equal to `30`")  # noqa: E501

        self._functional_area_name = functional_area_name

    @property
    def functional_area_short_name(self):
        """Gets the functional_area_short_name of this Client.  # noqa: E501

        Indicates the short name of the functional area to which the client is assigned. Only relevant if the package 'Eigenorganisation comfort' is installed.   # noqa: E501

        :return: The functional_area_short_name of this Client.  # noqa: E501
        :rtype: str
        """
        return self._functional_area_short_name

    @functional_area_short_name.setter
    def functional_area_short_name(self, functional_area_short_name):
        """Sets the functional_area_short_name of this Client.

        Indicates the short name of the functional area to which the client is assigned. Only relevant if the package 'Eigenorganisation comfort' is installed.   # noqa: E501

        :param functional_area_short_name: The functional_area_short_name of this Client.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                functional_area_short_name is not None and len(functional_area_short_name) > 10):
            raise ValueError("Invalid value for `functional_area_short_name`, length must be less than or equal to `10`")  # noqa: E501

        self._functional_area_short_name = functional_area_short_name

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
        if issubclass(Client, dict):
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
        if not isinstance(other, Client):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Client):
            return True

        return self.to_dict() != other.to_dict()
