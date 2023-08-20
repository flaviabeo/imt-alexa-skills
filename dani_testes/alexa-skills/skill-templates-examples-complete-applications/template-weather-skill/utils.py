import logging
from ask_sdk_core.handler_input import HandlerInput
import ask_sdk_core.utils as ask_utils

"""
Helper method to find if a request is for a certain apiName.
"""
def isApiRequest(handler_input, api_name):
    try:
        return ask_utils.request_util.get_request_type(handler_input) == 'Dialog.API.Invoked' and handler_input.request_envelope.request.api_request.name == api_name
    except Exception as ex:
        logging.error(ex)
        return False


"""
Helper method to get API arguments from the request envelope.
"""
def getApiArguments(handler_input):
    try:
        return handler_input.request_envelope.request.api_request.arguments
    except Exception as ex:
        logging.error(ex)
        return False


"""
Helper method to get API slots from the request envelope.
"""
def getSlots(handler_input):
    try:
        return handler_input.request_envelope.request.api_request.slots
    except Exception as ex:
        logging.error(ex)
        return False


def getCityNameWithIdFromApiRequestSlots(handler_input):
    slots = getSlots(handler_input)

    resolvedCityName = slots['cityName']

    if(
        resolvedCityName and
        resolvedCityName.resolutions and
        resolvedCityName.resolutions.resolutions_per_authority and
        resolvedCityName.resolutions.resolutions_per_authority[0] and
        resolvedCityName.resolutions.resolutions_per_authority[0].status and
        resolvedCityName.resolutions.resolutions_per_authority[0].status.code.value == 'ER_SUCCESS_MATCH'
    ):

        return resolvedCityName.resolutions.resolutions_per_authority[0].values[0].value

    else:
        return None
