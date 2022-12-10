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


class Responsibility(object):
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
        'area_of_responsibility_id': 'str',
        'area_of_responsibility_name': 'str',
        'employee_id': 'str',
        'employee_display_name': 'str',
        'employee_number': 'int',
        'employee_status': 'str',
        'client_id': 'str',
        'client_name': 'str',
        'client_number': 'int',
        'client_status': 'str',
        'id': 'int'
    }

    attribute_map = {
        'area_of_responsibility_id': 'area_of_responsibility_id',
        'area_of_responsibility_name': 'area_of_responsibility_name',
        'employee_id': 'employee_id',
        'employee_display_name': 'employee_display_name',
        'employee_number': 'employee_number',
        'employee_status': 'employee_status',
        'client_id': 'client_id',
        'client_name': 'client_name',
        'client_number': 'client_number',
        'client_status': 'client_status',
        'id': 'id'
    }

    def __init__(self, area_of_responsibility_id=None, area_of_responsibility_name=None, employee_id=None, employee_display_name=None, employee_number=None, employee_status=None, client_id=None, client_name=None, client_number=None, client_status=None, id=None, _configuration=None):  # noqa: E501
        """Responsibility - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._area_of_responsibility_id = None
        self._area_of_responsibility_name = None
        self._employee_id = None
        self._employee_display_name = None
        self._employee_number = None
        self._employee_status = None
        self._client_id = None
        self._client_name = None
        self._client_number = None
        self._client_status = None
        self._id = None
        self.discriminator = None

        if area_of_responsibility_id is not None:
            self.area_of_responsibility_id = area_of_responsibility_id
        if area_of_responsibility_name is not None:
            self.area_of_responsibility_name = area_of_responsibility_name
        if employee_id is not None:
            self.employee_id = employee_id
        if employee_display_name is not None:
            self.employee_display_name = employee_display_name
        if employee_number is not None:
            self.employee_number = employee_number
        if employee_status is not None:
            self.employee_status = employee_status
        if client_id is not None:
            self.client_id = client_id
        if client_name is not None:
            self.client_name = client_name
        if client_number is not None:
            self.client_number = client_number
        if client_status is not None:
            self.client_status = client_status
        if id is not None:
            self.id = id

    @property
    def area_of_responsibility_id(self):
        """Gets the area_of_responsibility_id of this Responsibility.  # noqa: E501

        Code for the area of responsibility – identifies an area of responsibility.   # noqa: E501

        :return: The area_of_responsibility_id of this Responsibility.  # noqa: E501
        :rtype: str
        """
        return self._area_of_responsibility_id

    @area_of_responsibility_id.setter
    def area_of_responsibility_id(self, area_of_responsibility_id):
        """Sets the area_of_responsibility_id of this Responsibility.

        Code for the area of responsibility – identifies an area of responsibility.   # noqa: E501

        :param area_of_responsibility_id: The area_of_responsibility_id of this Responsibility.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                area_of_responsibility_id is not None and len(area_of_responsibility_id) > 10):
            raise ValueError("Invalid value for `area_of_responsibility_id`, length must be less than or equal to `10`")  # noqa: E501

        self._area_of_responsibility_id = area_of_responsibility_id

    @property
    def area_of_responsibility_name(self):
        """Gets the area_of_responsibility_name of this Responsibility.  # noqa: E501

        Name of the area of responsibility.   # noqa: E501

        :return: The area_of_responsibility_name of this Responsibility.  # noqa: E501
        :rtype: str
        """
        return self._area_of_responsibility_name

    @area_of_responsibility_name.setter
    def area_of_responsibility_name(self, area_of_responsibility_name):
        """Sets the area_of_responsibility_name of this Responsibility.

        Name of the area of responsibility.   # noqa: E501

        :param area_of_responsibility_name: The area_of_responsibility_name of this Responsibility.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                area_of_responsibility_name is not None and len(area_of_responsibility_name) > 100):
            raise ValueError("Invalid value for `area_of_responsibility_name`, length must be less than or equal to `100`")  # noqa: E501

        self._area_of_responsibility_name = area_of_responsibility_name

    @property
    def employee_id(self):
        """Gets the employee_id of this Responsibility.  # noqa: E501

        The GUID of an employee – identifies an employee.   # noqa: E501

        :return: The employee_id of this Responsibility.  # noqa: E501
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """Sets the employee_id of this Responsibility.

        The GUID of an employee – identifies an employee.   # noqa: E501

        :param employee_id: The employee_id of this Responsibility.  # noqa: E501
        :type: str
        """

        self._employee_id = employee_id

    @property
    def employee_display_name(self):
        """Gets the employee_display_name of this Responsibility.  # noqa: E501

        Employee display name comprising a last and a first name.   # noqa: E501

        :return: The employee_display_name of this Responsibility.  # noqa: E501
        :rtype: str
        """
        return self._employee_display_name

    @employee_display_name.setter
    def employee_display_name(self, employee_display_name):
        """Sets the employee_display_name of this Responsibility.

        Employee display name comprising a last and a first name.   # noqa: E501

        :param employee_display_name: The employee_display_name of this Responsibility.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                employee_display_name is not None and len(employee_display_name) > 72):
            raise ValueError("Invalid value for `employee_display_name`, length must be less than or equal to `72`")  # noqa: E501

        self._employee_display_name = employee_display_name

    @property
    def employee_number(self):
        """Gets the employee_number of this Responsibility.  # noqa: E501

        Number of the employee (personnel number).   # noqa: E501

        :return: The employee_number of this Responsibility.  # noqa: E501
        :rtype: int
        """
        return self._employee_number

    @employee_number.setter
    def employee_number(self, employee_number):
        """Sets the employee_number of this Responsibility.

        Number of the employee (personnel number).   # noqa: E501

        :param employee_number: The employee_number of this Responsibility.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                employee_number is not None and employee_number > 99999):  # noqa: E501
            raise ValueError("Invalid value for `employee_number`, must be a value less than or equal to `99999`")  # noqa: E501
        if (self._configuration.client_side_validation and
                employee_number is not None and employee_number < 1):  # noqa: E501
            raise ValueError("Invalid value for `employee_number`, must be a value greater than or equal to `1`")  # noqa: E501

        self._employee_number = employee_number

    @property
    def employee_status(self):
        """Gets the employee_status of this Responsibility.  # noqa: E501

        Indicates whether the employee is active or inactive.   # noqa: E501

        :return: The employee_status of this Responsibility.  # noqa: E501
        :rtype: str
        """
        return self._employee_status

    @employee_status.setter
    def employee_status(self, employee_status):
        """Sets the employee_status of this Responsibility.

        Indicates whether the employee is active or inactive.   # noqa: E501

        :param employee_status: The employee_status of this Responsibility.  # noqa: E501
        :type: str
        """
        allowed_values = ["inactive", "active"]  # noqa: E501
        if (self._configuration.client_side_validation and
                employee_status not in allowed_values):
            raise ValueError(
                "Invalid value for `employee_status` ({0}), must be one of {1}"  # noqa: E501
                .format(employee_status, allowed_values)
            )

        self._employee_status = employee_status

    @property
    def client_id(self):
        """Gets the client_id of this Responsibility.  # noqa: E501

        The GUID of a client – identifies a client.   # noqa: E501

        :return: The client_id of this Responsibility.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this Responsibility.

        The GUID of a client – identifies a client.   # noqa: E501

        :param client_id: The client_id of this Responsibility.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def client_name(self):
        """Gets the client_name of this Responsibility.  # noqa: E501

        Name of the client.   # noqa: E501

        :return: The client_name of this Responsibility.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this Responsibility.

        Name of the client.   # noqa: E501

        :param client_name: The client_name of this Responsibility.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                client_name is not None and len(client_name) > 30):
            raise ValueError("Invalid value for `client_name`, length must be less than or equal to `30`")  # noqa: E501

        self._client_name = client_name

    @property
    def client_number(self):
        """Gets the client_number of this Responsibility.  # noqa: E501

        Central client number.   # noqa: E501

        :return: The client_number of this Responsibility.  # noqa: E501
        :rtype: int
        """
        return self._client_number

    @client_number.setter
    def client_number(self, client_number):
        """Sets the client_number of this Responsibility.

        Central client number.   # noqa: E501

        :param client_number: The client_number of this Responsibility.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                client_number is not None and client_number > 999999999):  # noqa: E501
            raise ValueError("Invalid value for `client_number`, must be a value less than or equal to `999999999`")  # noqa: E501
        if (self._configuration.client_side_validation and
                client_number is not None and client_number < 1):  # noqa: E501
            raise ValueError("Invalid value for `client_number`, must be a value greater than or equal to `1`")  # noqa: E501

        self._client_number = client_number

    @property
    def client_status(self):
        """Gets the client_status of this Responsibility.  # noqa: E501

        Indicates whether the client relationship is active or inactive.   # noqa: E501

        :return: The client_status of this Responsibility.  # noqa: E501
        :rtype: str
        """
        return self._client_status

    @client_status.setter
    def client_status(self, client_status):
        """Sets the client_status of this Responsibility.

        Indicates whether the client relationship is active or inactive.   # noqa: E501

        :param client_status: The client_status of this Responsibility.  # noqa: E501
        :type: str
        """
        allowed_values = ["inactive", "active"]  # noqa: E501
        if (self._configuration.client_side_validation and
                client_status not in allowed_values):
            raise ValueError(
                "Invalid value for `client_status` ({0}), must be one of {1}"  # noqa: E501
                .format(client_status, allowed_values)
            )

        self._client_status = client_status

    @property
    def id(self):
        """Gets the id of this Responsibility.  # noqa: E501

        Unique identifier of the responsibility.   # noqa: E501

        :return: The id of this Responsibility.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Responsibility.

        Unique identifier of the responsibility.   # noqa: E501

        :param id: The id of this Responsibility.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(Responsibility, dict):
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
        if not isinstance(other, Responsibility):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Responsibility):
            return True

        return self.to_dict() != other.to_dict()