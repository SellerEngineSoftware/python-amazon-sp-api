# coding: utf-8

"""
    Selling Partner API for Product Fees

    The Selling Partner API for Product Fees lets you programmatically retrieve estimated fees for a product. You can then account for those fees in your pricing.  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class FeesEstimateResult(object):
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
        'status': 'str',
        'fees_estimate_identifier': 'FeesEstimateIdentifier',
        'fees_estimate': 'FeesEstimate',
        'error': 'FeesEstimateError'
    }

    attribute_map = {
        'status': 'Status',
        'fees_estimate_identifier': 'FeesEstimateIdentifier',
        'fees_estimate': 'FeesEstimate',
        'error': 'Error'
    }

    def __init__(self, status=None, fees_estimate_identifier=None, fees_estimate=None, error=None):  # noqa: E501
        """FeesEstimateResult - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._fees_estimate_identifier = None
        self._fees_estimate = None
        self._error = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if fees_estimate_identifier is not None:
            self.fees_estimate_identifier = fees_estimate_identifier
        if fees_estimate is not None:
            self.fees_estimate = fees_estimate
        if error is not None:
            self.error = error

    @property
    def status(self):
        """Gets the status of this FeesEstimateResult.  # noqa: E501

        The status of the fee request. Possible values: Success, ClientError, ServiceError.  # noqa: E501

        :return: The status of this FeesEstimateResult.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FeesEstimateResult.

        The status of the fee request. Possible values: Success, ClientError, ServiceError.  # noqa: E501

        :param status: The status of this FeesEstimateResult.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def fees_estimate_identifier(self):
        """Gets the fees_estimate_identifier of this FeesEstimateResult.  # noqa: E501


        :return: The fees_estimate_identifier of this FeesEstimateResult.  # noqa: E501
        :rtype: FeesEstimateIdentifier
        """
        return self._fees_estimate_identifier

    @fees_estimate_identifier.setter
    def fees_estimate_identifier(self, fees_estimate_identifier):
        """Sets the fees_estimate_identifier of this FeesEstimateResult.


        :param fees_estimate_identifier: The fees_estimate_identifier of this FeesEstimateResult.  # noqa: E501
        :type: FeesEstimateIdentifier
        """

        self._fees_estimate_identifier = fees_estimate_identifier

    @property
    def fees_estimate(self):
        """Gets the fees_estimate of this FeesEstimateResult.  # noqa: E501


        :return: The fees_estimate of this FeesEstimateResult.  # noqa: E501
        :rtype: FeesEstimate
        """
        return self._fees_estimate

    @fees_estimate.setter
    def fees_estimate(self, fees_estimate):
        """Sets the fees_estimate of this FeesEstimateResult.


        :param fees_estimate: The fees_estimate of this FeesEstimateResult.  # noqa: E501
        :type: FeesEstimate
        """

        self._fees_estimate = fees_estimate

    @property
    def error(self):
        """Gets the error of this FeesEstimateResult.  # noqa: E501


        :return: The error of this FeesEstimateResult.  # noqa: E501
        :rtype: FeesEstimateError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this FeesEstimateResult.


        :param error: The error of this FeesEstimateResult.  # noqa: E501
        :type: FeesEstimateError
        """

        self._error = error

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
        if issubclass(FeesEstimateResult, dict):
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
        if not isinstance(other, FeesEstimateResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
