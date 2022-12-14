# coding: utf-8

"""
    Client Master Data

    In the documentation below, you will receive detailed functional and technical specifications on the API DATEVconnect for Master Data.  **General information on dealing with fields administered as historical** A number of fields in the  master data are administered as \"historical\". This means that the existing content is not overwritten when the field is updated, but that the existing value remains in place, with a new value added that is valid from a date entered by the user.  Specifically, the following fields are administered as historical:  *Ressource 'addressees'* - short_names, - surnames, - company_names, - legal_form_ids  *Subordinate object 'detail'* - considerations, - denominations, - federal_states_of_natural_person, - job_titles, - marital_statuses, - codes_of_classification_of_economic_activities_2008, - descriptions_of_classification_of_economic_activities_2008, - mad_codes_of_classification_of_economic_activities_2008, - codes_of_classification_of_economic_activities_2003, - descriptions_of_classification_of_economic_activities_2003, - mad_codes_of_classification_of_economic_activities_2003, - countries_of_head_office, - distributions_of_profit, - enterprise_purposes, - federal_states_mad_of_legal_person, - federal_states_of_legal_person, - fiscal_years, - kind_of_register_courts, - locations_of_head_office, - names_of_register_court, - registered_company_names, - registration_numbers, - three_lined_company_names_first_line, - three_lined_company_names_second_line, - three_lined_company_names_third_line, - two_lined_company_names_first_line, - two_lined_company_names_second_line  These fields are shown as arrays, with their elements exhibiting the following structure: - value, - valid_from  This structure makes it possible to generate periods that indicate the validity date of a particular value in a value range.  This is illustrated by the following examples:  \"job_titles\": [   {\"value\":\"Müller\"},   {\"value\":\"Bäcker\", \"valid_from\":\"1995-04-01T00:00:00.000\"},   {\"value\":\"Metzger\", \"valid_from\":\"2001-07-01T00:00:00.000\"} ] In this example, the profession \"Müller\" (\"miller\") was valid until 03/31/1995. \"Bäcker\" (\"baker\") was valid from 04/01/1995 to 06/30/2001. The value \"Metzger\" (\"butcher\") is valid starting 07/01/2001.  For all the historically administered fields listed above, there is an additional field that indicates the current value of the value range (the value that is valid today/as of the system time). The syntactic structure of the property name is as follows: current_<*Property name of the historically administered field in the singular*>.  In the example above, the property name is \"current_job_title\" with the value \"Metzger\" (\"current_job_title\": \"Metzger\").  When writing fields administered as historical, please note that both properties have to be entered to prevent content from being lost. This can once again be illustrated using the example above:  Starting on 01/01/2010, the person is no longer employed as a butcher (\"Metzger\"), but now works as a landlord (\"Wirt\") in the hospitality industry. In order to save this information in the master data, the request has to be as follows:  ...  \"job_titles\": [   {\"value\":\"Müller\"},   {\"value\":\"Bäcker\", \"valid_from\":\"1995-04-01T00:00:00.000\"},   {\"value\":\"Metzger\", \"valid_from\":\"2001-07-01T00:00:00.000\"},   {\"value\": \"Wirt\", \"valid_from\": \"2010-01-01T00:00:00.000\"} ],  \"current_job_title\": \"Wirt\",  ...  If the property \"current_job_title\" had not been entered, but only the property \"job_titles\", then the current value (\"landlord\" in this example) would have been overwritten by a NULL value, as there would have been no explicit entry for the current value.  If, however, only the property \"current_job_title\" had been entered (i.e. without entering the property \"job_titles\"), then all historical values would have been overwritten. The result would have been the sole value of \"landlord\" without any time period set.  In summary, it can be said that the content of the property \"current_job_title\" overwrites the content of the valid array element of the property \"job_titles\".   # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: schnittstellenberatung@datev.de
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class EmployeeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def employees_employee_id_get(self, employee_id, **kwargs):  # noqa: E501
        """Retrieve a specific consultancy employee.  # noqa: E501

         Retrieving a specific consultancy employee.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.employees_employee_id_get(employee_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str employee_id: The GUID of an employee. (required)
        :param str select: Enter relevant attributes to which the results will then be limited.      
        :return: Employee
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.employees_employee_id_get_with_http_info(employee_id, **kwargs)  # noqa: E501
        else:
            (data) = self.employees_employee_id_get_with_http_info(employee_id, **kwargs)  # noqa: E501
            return data

    def employees_employee_id_get_with_http_info(self, employee_id, **kwargs):  # noqa: E501
        """Retrieve a specific consultancy employee.  # noqa: E501

         Retrieving a specific consultancy employee.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.employees_employee_id_get_with_http_info(employee_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str employee_id: The GUID of an employee. (required)
        :param str select: Enter relevant attributes to which the results will then be limited.      
        :return: Employee
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['employee_id', 'select']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method employees_employee_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'employee_id' is set
        if self.api_client.client_side_validation and ('employee_id' not in params or
                                                       params['employee_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `employee_id` when calling `employees_employee_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'employee_id' in params:
            path_params['employee-id'] = params['employee_id']  # noqa: E501

        query_params = []
        if 'select' in params:
            query_params.append(('select', params['select']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/employees/{employee-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Employee',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def employees_employee_id_put(self, employee_id, employee, **kwargs):  # noqa: E501
        """Update a specific consultancy employee.  # noqa: E501

        With the PUT command, the consultancy employee will be completely overwritten. We therefore recommend that you perform a request of the employee being updated beforehand in order to prevent master data from being overwritten.<br><br>  The following properties may not be changed: - id - natural_person_id - number   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.employees_employee_id_put(employee_id, employee, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str employee_id: The GUID of an employee. (required)
        :param Employee employee: employee object (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.employees_employee_id_put_with_http_info(employee_id, employee, **kwargs)  # noqa: E501
        else:
            (data) = self.employees_employee_id_put_with_http_info(employee_id, employee, **kwargs)  # noqa: E501
            return data

    def employees_employee_id_put_with_http_info(self, employee_id, employee, **kwargs):  # noqa: E501
        """Update a specific consultancy employee.  # noqa: E501

        With the PUT command, the consultancy employee will be completely overwritten. We therefore recommend that you perform a request of the employee being updated beforehand in order to prevent master data from being overwritten.<br><br>  The following properties may not be changed: - id - natural_person_id - number   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.employees_employee_id_put_with_http_info(employee_id, employee, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str employee_id: The GUID of an employee. (required)
        :param Employee employee: employee object (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['employee_id', 'employee']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method employees_employee_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'employee_id' is set
        if self.api_client.client_side_validation and ('employee_id' not in params or
                                                       params['employee_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `employee_id` when calling `employees_employee_id_put`")  # noqa: E501
        # verify the required parameter 'employee' is set
        if self.api_client.client_side_validation and ('employee' not in params or
                                                       params['employee'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `employee` when calling `employees_employee_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'employee_id' in params:
            path_params['employee-id'] = params['employee_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'employee' in params:
            body_params = params['employee']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/employees/{employee-id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def employees_get(self, **kwargs):  # noqa: E501
        """Retrieve a list of consultancy employees.  # noqa: E501

         **Filter** Unless further parameters are entered, the list will contain both active and inactive consultancy employees.<br><br>  **Filter Options**  The number of results can be limited by using the following filters: - name - number - status - timestamp - organization_id - organization_name - organization_number - establishment_id - establishment_name - establishment_number - establishment_short_name - functional_area_id - functional_area_name - functional_area_short_name <br>  **Operators** <br>  *Filter Option: number, timestamp, organization_number, establishment_number*  | Operator          | Description           | |-------------------|-----------------------| | eq                | Equal                 | | gt                | Greater than          | | ge                | Greater than or equal | | lt                | Less than             | | le                | Less than or equal    | <br>   *Filter Option: name, organization_name, establishment_name, establishment_short_name, functional_area_name, functional_area_short_name*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | | contains(property, substring)  | Search for Substring in property's value                       | | startswith(property, substring)| Search for Substring at the beginning of the property's value  | <br>   *Filter Option: status, organization_id, establishment_id, functional_area_id*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal; 'Gleich'                                                | <br>  **Filter Combinations**  Filters can be combined using the operator \"and\".<br><br>  **URI Examples**  *Retrieving an employee with the employee number 20000*        .../employees?filter=number eq 20000<br><br>  *Retrieving all employees whose employee number is greater than or equal to 10000 and less than 70000* .../employees?filter=number ge 20000 and number lt 70000<br><br>  *Retrieving all employees whose name contains the word \"Mustermeier\"*        .../employees?filter=contains(name, Mustermeier)<br><br>  *Retrieving all active employees*        .../employees?filter=status eq active<br><br>              # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.employees_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str select: Enter relevant attributes to which the results will then be limited.      
        :param str filter: Entering a filter expression influences the number of results. 
        :return: list[Employee]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.employees_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.employees_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def employees_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a list of consultancy employees.  # noqa: E501

         **Filter** Unless further parameters are entered, the list will contain both active and inactive consultancy employees.<br><br>  **Filter Options**  The number of results can be limited by using the following filters: - name - number - status - timestamp - organization_id - organization_name - organization_number - establishment_id - establishment_name - establishment_number - establishment_short_name - functional_area_id - functional_area_name - functional_area_short_name <br>  **Operators** <br>  *Filter Option: number, timestamp, organization_number, establishment_number*  | Operator          | Description           | |-------------------|-----------------------| | eq                | Equal                 | | gt                | Greater than          | | ge                | Greater than or equal | | lt                | Less than             | | le                | Less than or equal    | <br>   *Filter Option: name, organization_name, establishment_name, establishment_short_name, functional_area_name, functional_area_short_name*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal                                                          | | contains(property, substring)  | Search for Substring in property's value                       | | startswith(property, substring)| Search for Substring at the beginning of the property's value  | <br>   *Filter Option: status, organization_id, establishment_id, functional_area_id*  | Operator                       | Description                                                    | |--------------------------------|----------------------------------------------------------------| | eq                             | Equal; 'Gleich'                                                | <br>  **Filter Combinations**  Filters can be combined using the operator \"and\".<br><br>  **URI Examples**  *Retrieving an employee with the employee number 20000*        .../employees?filter=number eq 20000<br><br>  *Retrieving all employees whose employee number is greater than or equal to 10000 and less than 70000* .../employees?filter=number ge 20000 and number lt 70000<br><br>  *Retrieving all employees whose name contains the word \"Mustermeier\"*        .../employees?filter=contains(name, Mustermeier)<br><br>  *Retrieving all active employees*        .../employees?filter=status eq active<br><br>              # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.employees_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str select: Enter relevant attributes to which the results will then be limited.      
        :param str filter: Entering a filter expression influences the number of results. 
        :return: list[Employee]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['select', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method employees_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'select' in params:
            query_params.append(('select', params['select']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/employees', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Employee]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def employees_post(self, new_employee, **kwargs):  # noqa: E501
        """Creating a new consultancy employee.  # noqa: E501

         When creating a new consultancy employee, please note that the addressee of the type \"natural_person\" (POST /addressees) has to be created first, followed by the consultancy employee (POST /employees). The property \"natural_person_id\" must be completed with the GUID of the created addressee.<br> If the property \"number\" is not specified or completed with 0, then the system assigns the number automatically. In this case the largest assigned number is increased by 1. If  the number 99999 is already assigned, the system fills the gaps.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.employees_post(new_employee, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Employee new_employee: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.employees_post_with_http_info(new_employee, **kwargs)  # noqa: E501
        else:
            (data) = self.employees_post_with_http_info(new_employee, **kwargs)  # noqa: E501
            return data

    def employees_post_with_http_info(self, new_employee, **kwargs):  # noqa: E501
        """Creating a new consultancy employee.  # noqa: E501

         When creating a new consultancy employee, please note that the addressee of the type \"natural_person\" (POST /addressees) has to be created first, followed by the consultancy employee (POST /employees). The property \"natural_person_id\" must be completed with the GUID of the created addressee.<br> If the property \"number\" is not specified or completed with 0, then the system assigns the number automatically. In this case the largest assigned number is increased by 1. If  the number 99999 is already assigned, the system fills the gaps.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.employees_post_with_http_info(new_employee, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Employee new_employee: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['new_employee']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method employees_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'new_employee' is set
        if self.api_client.client_side_validation and ('new_employee' not in params or
                                                       params['new_employee'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `new_employee` when calling `employees_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'new_employee' in params:
            body_params = params['new_employee']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/employees', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
