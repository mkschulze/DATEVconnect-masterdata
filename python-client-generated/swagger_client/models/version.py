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


class Version(object):
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
        'adress_country': 'str',
        'client_number_maximum_number_of_digits': 'int',
        'client_number_start': 'int',
        'client_categories_groups_supported': 'bool',
        'db_build': 'str',
        'db_version': 'str',
        'db_version_date': 'str',
        'id': 'int',
        'resource_revision': 'str',
        'resource_version': 'str',
        'version': 'str',
        'version_name': 'str'
    }

    attribute_map = {
        'adress_country': 'adress_country',
        'client_number_maximum_number_of_digits': 'client_number_maximum_number_of_digits',
        'client_number_start': 'client_number_start',
        'client_categories_groups_supported': 'client_categories_groups_supported',
        'db_build': 'db_build',
        'db_version': 'db_version',
        'db_version_date': 'db_version_date',
        'id': 'id',
        'resource_revision': 'resource_revision',
        'resource_version': 'resource_version',
        'version': 'version',
        'version_name': 'version_name'
    }

    def __init__(self, adress_country=None, client_number_maximum_number_of_digits=None, client_number_start=None, client_categories_groups_supported=None, db_build=None, db_version=None, db_version_date=None, id=None, resource_revision=None, resource_version=None, version=None, version_name=None, _configuration=None):  # noqa: E501
        """Version - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._adress_country = None
        self._client_number_maximum_number_of_digits = None
        self._client_number_start = None
        self._client_categories_groups_supported = None
        self._db_build = None
        self._db_version = None
        self._db_version_date = None
        self._id = None
        self._resource_revision = None
        self._resource_version = None
        self._version = None
        self._version_name = None
        self.discriminator = None

        if adress_country is not None:
            self.adress_country = adress_country
        if client_number_maximum_number_of_digits is not None:
            self.client_number_maximum_number_of_digits = client_number_maximum_number_of_digits
        if client_number_start is not None:
            self.client_number_start = client_number_start
        if client_categories_groups_supported is not None:
            self.client_categories_groups_supported = client_categories_groups_supported
        if db_build is not None:
            self.db_build = db_build
        if db_version is not None:
            self.db_version = db_version
        if db_version_date is not None:
            self.db_version_date = db_version_date
        if id is not None:
            self.id = id
        if resource_revision is not None:
            self.resource_revision = resource_revision
        if resource_version is not None:
            self.resource_version = resource_version
        if version is not None:
            self.version = version
        if version_name is not None:
            self.version_name = version_name

    @property
    def adress_country(self):
        """Gets the adress_country of this Version.  # noqa: E501

        Indicates which package is installed - 'DATEV Basis' or 'DATEV Basis für Unternehmen' (DE) or 'DATEV Basis für Österreich' (AT). Depending on this information, the property 'national_right' will be filled with the default option when the addressee is created.  # noqa: E501

        :return: The adress_country of this Version.  # noqa: E501
        :rtype: str
        """
        return self._adress_country

    @adress_country.setter
    def adress_country(self, adress_country):
        """Sets the adress_country of this Version.

        Indicates which package is installed - 'DATEV Basis' or 'DATEV Basis für Unternehmen' (DE) or 'DATEV Basis für Österreich' (AT). Depending on this information, the property 'national_right' will be filled with the default option when the addressee is created.  # noqa: E501

        :param adress_country: The adress_country of this Version.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                adress_country is not None and len(adress_country) > 2):
            raise ValueError("Invalid value for `adress_country`, length must be less than or equal to `2`")  # noqa: E501
        if (self._configuration.client_side_validation and
                adress_country is not None and len(adress_country) < 2):
            raise ValueError("Invalid value for `adress_country`, length must be greater than or equal to `2`")  # noqa: E501

        self._adress_country = adress_country

    @property
    def client_number_maximum_number_of_digits(self):
        """Gets the client_number_maximum_number_of_digits of this Version.  # noqa: E501

        Potential maximum length of the central client number.  # noqa: E501

        :return: The client_number_maximum_number_of_digits of this Version.  # noqa: E501
        :rtype: int
        """
        return self._client_number_maximum_number_of_digits

    @client_number_maximum_number_of_digits.setter
    def client_number_maximum_number_of_digits(self, client_number_maximum_number_of_digits):
        """Sets the client_number_maximum_number_of_digits of this Version.

        Potential maximum length of the central client number.  # noqa: E501

        :param client_number_maximum_number_of_digits: The client_number_maximum_number_of_digits of this Version.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                client_number_maximum_number_of_digits is not None and client_number_maximum_number_of_digits > 9):  # noqa: E501
            raise ValueError("Invalid value for `client_number_maximum_number_of_digits`, must be a value less than or equal to `9`")  # noqa: E501
        if (self._configuration.client_side_validation and
                client_number_maximum_number_of_digits is not None and client_number_maximum_number_of_digits < 5):  # noqa: E501
            raise ValueError("Invalid value for `client_number_maximum_number_of_digits`, must be a value greater than or equal to `5`")  # noqa: E501

        self._client_number_maximum_number_of_digits = client_number_maximum_number_of_digits

    @property
    def client_number_start(self):
        """Gets the client_number_start of this Version.  # noqa: E501

        Indicates the first client number saved at the consultancy.  # noqa: E501

        :return: The client_number_start of this Version.  # noqa: E501
        :rtype: int
        """
        return self._client_number_start

    @client_number_start.setter
    def client_number_start(self, client_number_start):
        """Sets the client_number_start of this Version.

        Indicates the first client number saved at the consultancy.  # noqa: E501

        :param client_number_start: The client_number_start of this Version.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                client_number_start is not None and client_number_start > 999999999):  # noqa: E501
            raise ValueError("Invalid value for `client_number_start`, must be a value less than or equal to `999999999`")  # noqa: E501
        if (self._configuration.client_side_validation and
                client_number_start is not None and client_number_start < 1):  # noqa: E501
            raise ValueError("Invalid value for `client_number_start`, must be a value greater than or equal to `1`")  # noqa: E501

        self._client_number_start = client_number_start

    @property
    def client_categories_groups_supported(self):
        """Gets the client_categories_groups_supported of this Version.  # noqa: E501

        Indicates whether client categories und client groups are supported. This is the case if the package 'Eigenorganisation comfort' is installed.  # noqa: E501

        :return: The client_categories_groups_supported of this Version.  # noqa: E501
        :rtype: bool
        """
        return self._client_categories_groups_supported

    @client_categories_groups_supported.setter
    def client_categories_groups_supported(self, client_categories_groups_supported):
        """Sets the client_categories_groups_supported of this Version.

        Indicates whether client categories und client groups are supported. This is the case if the package 'Eigenorganisation comfort' is installed.  # noqa: E501

        :param client_categories_groups_supported: The client_categories_groups_supported of this Version.  # noqa: E501
        :type: bool
        """

        self._client_categories_groups_supported = client_categories_groups_supported

    @property
    def db_build(self):
        """Gets the db_build of this Version.  # noqa: E501

        Build status of the EODB database.  # noqa: E501

        :return: The db_build of this Version.  # noqa: E501
        :rtype: str
        """
        return self._db_build

    @db_build.setter
    def db_build(self, db_build):
        """Sets the db_build of this Version.

        Build status of the EODB database.  # noqa: E501

        :param db_build: The db_build of this Version.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                db_build is not None and len(db_build) > 10):
            raise ValueError("Invalid value for `db_build`, length must be less than or equal to `10`")  # noqa: E501

        self._db_build = db_build

    @property
    def db_version(self):
        """Gets the db_version of this Version.  # noqa: E501

        Version number of the EODB database.  # noqa: E501

        :return: The db_version of this Version.  # noqa: E501
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """Sets the db_version of this Version.

        Version number of the EODB database.  # noqa: E501

        :param db_version: The db_version of this Version.  # noqa: E501
        :type: str
        """

        self._db_version = db_version

    @property
    def db_version_date(self):
        """Gets the db_version_date of this Version.  # noqa: E501

        Version date of the EODB database (German date format).  # noqa: E501

        :return: The db_version_date of this Version.  # noqa: E501
        :rtype: str
        """
        return self._db_version_date

    @db_version_date.setter
    def db_version_date(self, db_version_date):
        """Sets the db_version_date of this Version.

        Version date of the EODB database (German date format).  # noqa: E501

        :param db_version_date: The db_version_date of this Version.  # noqa: E501
        :type: str
        """

        self._db_version_date = db_version_date

    @property
    def id(self):
        """Gets the id of this Version.  # noqa: E501

        Unique identifier of the version (always 1).  # noqa: E501

        :return: The id of this Version.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Version.

        Unique identifier of the version (always 1).  # noqa: E501

        :param id: The id of this Version.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def resource_revision(self):
        """Gets the resource_revision of this Version.  # noqa: E501

        Indicates the revision status of the API Master Data.  # noqa: E501

        :return: The resource_revision of this Version.  # noqa: E501
        :rtype: str
        """
        return self._resource_revision

    @resource_revision.setter
    def resource_revision(self, resource_revision):
        """Sets the resource_revision of this Version.

        Indicates the revision status of the API Master Data.  # noqa: E501

        :param resource_revision: The resource_revision of this Version.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                resource_revision is not None and len(resource_revision) > 10):
            raise ValueError("Invalid value for `resource_revision`, length must be less than or equal to `10`")  # noqa: E501

        self._resource_revision = resource_revision

    @property
    def resource_version(self):
        """Gets the resource_version of this Version.  # noqa: E501

        Indicates the version of the API Master Data (component of the base path).  # noqa: E501

        :return: The resource_version of this Version.  # noqa: E501
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        """Sets the resource_version of this Version.

        Indicates the version of the API Master Data (component of the base path).  # noqa: E501

        :param resource_version: The resource_version of this Version.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                resource_version is not None and len(resource_version) > 10):
            raise ValueError("Invalid value for `resource_version`, length must be less than or equal to `10`")  # noqa: E501

        self._resource_version = resource_version

    @property
    def version(self):
        """Gets the version of this Version.  # noqa: E501

        Indicates the version of the component K0005004.  # noqa: E501

        :return: The version of this Version.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Version.

        Indicates the version of the component K0005004.  # noqa: E501

        :param version: The version of this Version.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                version is not None and len(version) > 10):
            raise ValueError("Invalid value for `version`, length must be less than or equal to `10`")  # noqa: E501

        self._version = version

    @property
    def version_name(self):
        """Gets the version_name of this Version.  # noqa: E501

        Indicates the name (incl. version) of the component K0005004.  # noqa: E501

        :return: The version_name of this Version.  # noqa: E501
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this Version.

        Indicates the name (incl. version) of the component K0005004.  # noqa: E501

        :param version_name: The version_name of this Version.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                version_name is not None and len(version_name) > 50):
            raise ValueError("Invalid value for `version_name`, length must be less than or equal to `50`")  # noqa: E501

        self._version_name = version_name

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
        if issubclass(Version, dict):
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
        if not isinstance(other, Version):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Version):
            return True

        return self.to_dict() != other.to_dict()
