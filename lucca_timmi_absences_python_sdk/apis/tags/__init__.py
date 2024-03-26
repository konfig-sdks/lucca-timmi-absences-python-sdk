# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from lucca_timmi_absences_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    IMPORTS = "Imports"
    LEAVE_REQUESTS = "Leave Requests"
    LEAVES = "Leaves"
