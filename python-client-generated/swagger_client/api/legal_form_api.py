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


class LegalFormApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def legal_forms_get(self, **kwargs):  # noqa: E501
        """Retrieve a list of company legal forms.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.legal_forms_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str select: Enter relevant attributes to which the results will then be limited.      
        :param str national_right: This parameter serves a dual purpose:<br><br> **A: Ressource 'legal-forms'**<br> Parameter that controls the display of company legal forms depending on national law.<br><br>If 'national-right=german' is entered, then all company legal forms will be listed that are relevant to addressees subject to German law.<br>If 'national-right=austrian' is entered, then all company legal forms will be listed that are relevant to addressees subject to Austrian law.<br><br> **B: Ressource 'addressees'**<br> Parameter defines the national law that will be saved with the addressee. If the parameter is not entered, the national law that corresponds to the product installed will be entered as the default option:<br><br>If the package 'DATEV Basis für Österreich' is installed, then \"Austrian\" will be set as the applicable national law for the addressee.<br>If the package 'DATEV Basis' is installed, then \"German\" will be set as the applicable national law for the addressee. 
        :return: list[LegalForm]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.legal_forms_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.legal_forms_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def legal_forms_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a list of company legal forms.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.legal_forms_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str select: Enter relevant attributes to which the results will then be limited.      
        :param str national_right: This parameter serves a dual purpose:<br><br> **A: Ressource 'legal-forms'**<br> Parameter that controls the display of company legal forms depending on national law.<br><br>If 'national-right=german' is entered, then all company legal forms will be listed that are relevant to addressees subject to German law.<br>If 'national-right=austrian' is entered, then all company legal forms will be listed that are relevant to addressees subject to Austrian law.<br><br> **B: Ressource 'addressees'**<br> Parameter defines the national law that will be saved with the addressee. If the parameter is not entered, the national law that corresponds to the product installed will be entered as the default option:<br><br>If the package 'DATEV Basis für Österreich' is installed, then \"Austrian\" will be set as the applicable national law for the addressee.<br>If the package 'DATEV Basis' is installed, then \"German\" will be set as the applicable national law for the addressee. 
        :return: list[LegalForm]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['select', 'national_right']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method legal_forms_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'select' in params:
            query_params.append(('select', params['select']))  # noqa: E501
        if 'national_right' in params:
            query_params.append(('national-right', params['national_right']))  # noqa: E501

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
            '/legal-forms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[LegalForm]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
