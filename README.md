<div align="center">

[![Visit Lucca](./header.png)](https://lucca-hr.com)

# Lucca<a id="lucca"></a>

Welcome on the documentation for Timmi Absences API.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`luccatimmiabsences.imports.absence_batch_create`](#luccatimmiabsencesimportsabsence_batch_create)
  * [`luccatimmiabsences.imports.create_absences_batch`](#luccatimmiabsencesimportscreate_absences_batch)
  * [`luccatimmiabsences.imports.entitlements_batch_import`](#luccatimmiabsencesimportsentitlements_batch_import)
  * [`luccatimmiabsences.imports.get_progress`](#luccatimmiabsencesimportsget_progress)
  * [`luccatimmiabsences.imports.import_leave_entitlements`](#luccatimmiabsencesimportsimport_leave_entitlements)
  * [`luccatimmiabsences.imports.replace_entitlements`](#luccatimmiabsencesimportsreplace_entitlements)
  * [`luccatimmiabsences.imports.replace_entitlements_0`](#luccatimmiabsencesimportsreplace_entitlements_0)
  * [`luccatimmiabsences.leave_requests.approve_deny`](#luccatimmiabsencesleave_requestsapprove_deny)
  * [`luccatimmiabsences.leave_requests.cancel_request`](#luccatimmiabsencesleave_requestscancel_request)
  * [`luccatimmiabsences.leave_requests.get_by_id`](#luccatimmiabsencesleave_requestsget_by_id)
  * [`luccatimmiabsences.leave_requests.list`](#luccatimmiabsencesleave_requestslist)
  * [`luccatimmiabsences.leaves.cancel_leave_by_id`](#luccatimmiabsencesleavescancel_leave_by_id)
  * [`luccatimmiabsences.leaves.get_approved_list`](#luccatimmiabsencesleavesget_approved_list)
  * [`luccatimmiabsences.leaves.get_by_id`](#luccatimmiabsencesleavesget_by_id)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Lucca&serviceName=Timmi%20Absences&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from lucca_timmi_absences_python_sdk import LuccaTimmiAbsences, ApiException

luccatimmiabsences = LuccaTimmiAbsences(
    authorization="YOUR_API_KEY",
)

try:
    # Import leaves (deprecated)
    absence_batch_create_response = luccatimmiabsences.imports.absence_batch_create(
        type="csv",
        original_file_name="import.csv",
        create=False,
        recredit=True,
        synchronize=True,
        override_leaves=True,
    )
    print(absence_batch_create_response)
except ApiException as e:
    print("Exception when calling ImportsApi.absence_batch_create: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from lucca_timmi_absences_python_sdk import LuccaTimmiAbsences, ApiException

luccatimmiabsences = LuccaTimmiAbsences(
    authorization="YOUR_API_KEY",
)


async def main():
    try:
        # Import leaves (deprecated)
        absence_batch_create_response = (
            await luccatimmiabsences.imports.aabsence_batch_create(
                type="csv",
                original_file_name="import.csv",
                create=False,
                recredit=True,
                synchronize=True,
                override_leaves=True,
            )
        )
        print(absence_batch_create_response)
    except ApiException as e:
        print("Exception when calling ImportsApi.absence_batch_create: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from lucca_timmi_absences_python_sdk import LuccaTimmiAbsences, ApiException

luccatimmiabsences = LuccaTimmiAbsences(
    authorization="YOUR_API_KEY",
)

try:
    # Import leaves (deprecated)
    absence_batch_create_response = luccatimmiabsences.imports.raw.absence_batch_create(
        type="csv",
        original_file_name="import.csv",
        create=False,
        recredit=True,
        synchronize=True,
        override_leaves=True,
    )
    pprint(absence_batch_create_response.body)
    pprint(absence_batch_create_response.body["data"])
    pprint(absence_batch_create_response.headers)
    pprint(absence_batch_create_response.status)
    pprint(absence_batch_create_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ImportsApi.absence_batch_create: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `luccatimmiabsences.imports.absence_batch_create`<a id="luccatimmiabsencesimportsabsence_batch_create"></a>

Create absences in batch from a CSV file.

**Important notice: Absence imports cannot be cancelled.** 

In case of a mistake absences must be deleted manually through the interface or using the API (see Use cases). **Use import with care!**


**File format**

Type: CSV (with semicolon ";")

Encoding: UTF-8


All the following fields must be present with the field name in the header:

- legalEntity : establishment of the employee
- employeeNumber : employee number
- lastName : last name of the employee
- firstName : firstname of the employee
- accountId : absence account id in Timmi Absences (you can find it in the leave accounts admin page)
- startDate : absence start date (DD/MM/YYYY)
- flagStartDate : AM (if the absences starts in the morning) or PM (if the absence starts in the afternoon)
- endDate : absence end date (DD/MM/YYYY)
- flagEndDate : AM (if the absences ends at noon) or PM (if the absences ends in the afternoon)
- isApproved : yes or no. Compulsory if the absence type is subject to approval, optional otherwise.

**History**
Import history is available in the import module, including imports made using the API.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
absence_batch_create_response = luccatimmiabsences.imports.absence_batch_create(
    type="csv",
    original_file_name="import.csv",
    create=False,
    recredit=True,
    synchronize=True,
    override_leaves=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

Support CSV files only

##### original_file_name: `str`<a id="original_file_name-str"></a>

Filename

##### create: `bool`<a id="create-bool"></a>

Use `false` to simulate the import.

##### recredit: `bool`<a id="recredit-bool"></a>

Use `true` if absences should **not** be deducted from the user balance. Use `false` if absences should be deducted from the user balance. Note: if the absence type doesn’t have balance management, absence won’t impact the balance in any case.

##### synchronize: `bool`<a id="synchronize-bool"></a>

Use `true` to force synchronization of the absences in the sync webservice (sync to Exchange/0365, Google Calendar, Webhook or ADP GXP, depending on configuration). Use `false` to import absences without synchronizing absences.

##### override_leaves: `bool`<a id="override_leaves-bool"></a>

Use `true` to allow replacing existing absences

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`
#### 🔄 Return<a id="🔄-return"></a>

[`ImportsAbsenceBatchCreateResponse`](./lucca_timmi_absences_python_sdk/pydantic/imports_absence_batch_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/services/importLeavePeriods` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmiabsences.imports.create_absences_batch`<a id="luccatimmiabsencesimportscreate_absences_batch"></a>

Create absences in batch from a CSV file.

**Important notice: Absence imports cannot be cancelled.** 

In case of a mistake absences must be deleted manually through the interface or using the API (see Use cases). **Use import with care!**

**File format**

Content-Type: CSV. Column divider is semicolon ";". Line breaks between rows.

Encoding: UTF-8

All the following fields must be present with the field name in the header:

- legalEntity: Name of the establishment the employee belongs to.
- employeeNumber: Employee number.
- lastName: Family (last) name of the employee.
- firstName: Given (first) name of the employee.
- accountId: Identifier of the absence account in Timmi Absences (can be found in the leave accounts admin page).
- startDate: Start date of the absence, formatted as `DD/MM/YYYY`.
- flagStartDate: `"AM"` if the absence starts in the morning or `"PM"` if the absence starts in the afternoon.
- endDate: End date of the absence, formatted as `DD/MM/YYYY`.
- flagEndDate: `"AM"` if the absence ends at noon or `"PM"` if the absence ends in the afternoon.
- isApproved: `true` or `false`. Dictates whether the absence request should be created and already approved. 
  Required if the type of the absence requires approval, optional otherwise.

**History**
Import history is available in the import module. It includes imports made via the API.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_absences_batch_response = luccatimmiabsences.imports.create_absences_batch(
    create=True,
    recredit=True,
    original_file_name="import.csv",
    synchronize=True,
    _async=True,
    files=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### create: `bool`<a id="create-bool"></a>

Use `false` to simulate the import.

##### recredit: `bool`<a id="recredit-bool"></a>

Use `true` if absences should **not** be deducted from the user balance. Use `false` if absences should be deducted from the user balance. Note: if the absence type doesn’t have balance management, absence won’t impact the balance in any case.

##### original_file_name: `str`<a id="original_file_name-str"></a>

Filename

##### synchronize: `bool`<a id="synchronize-bool"></a>

Use `true` to force synchronization of the absences in the sync webservice (sync to Exchange/0365, Google Calendar, Webhook or ADP GXP, depending on configuration). Use `false` to import absences without synchronizing absences.

##### _async: `bool`<a id="_async-bool"></a>

Use `true` if you want to import absences with the asynchronous processing (you have to request figgo/api/imports/v1.0/leavePeriods/{summaryId}/progress API to track the status). Use `false` if you want import absences with the synchronous processing (the response is sent when the file is fully imported).

##### files: [`ImportsCreateAbsencesBatchRequestFiles`](./lucca_timmi_absences_python_sdk/type/imports_create_absences_batch_request_files.py)<a id="files-importscreateabsencesbatchrequestfileslucca_timmi_absences_python_sdktypeimports_create_absences_batch_request_filespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ImportsCreateAbsencesBatchRequest`](./lucca_timmi_absences_python_sdk/type/imports_create_absences_batch_request.py)
Content of the CSV file to import. Each file in its dedicated part of the multipart request. Parts are divided by the 'boundary' string set in the Content-Type HTTP header.  Example of a single file request body: ``` --myBoundary Content-Disposition: form-data; name=\"figgo-import-5875e9dd-0b1f-4a9f-8756-0f25fb0a2946.csv\"; filename=\"figgo-import-5875e9dd-0b1f-4a9f-8756-0f25fb0a2946.csv\" Content-Type: application/vnd.ms-excel  legalEntity;employeeNumber;lastName;firstName;accountId;startDate;flagStartDate;endDate;flagEndDate;isApproved Lucca FR;M0029;Bart;Maurice;1322;16/08/2022;am;17/08/2022;pm;true Lucca FR;M0029;Bart;Maurice;1322;22/08/2022;am;23/08/2022;pm;false Lucca FR;M0029;Bart;Maurice;8;29/08/2022;am;30/08/2022;pm;true --myBoundary-- ``` 

#### 🔄 Return<a id="🔄-return"></a>

[`ImportsCreateAbsencesBatchResponse`](./lucca_timmi_absences_python_sdk/pydantic/imports_create_absences_batch_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timmi-absences/api/imports/v1.0/leavePeriods` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmiabsences.imports.entitlements_batch_import`<a id="luccatimmiabsencesimportsentitlements_batch_import"></a>

**Supported file formats:**
- CSV
  - "UTF-8" encoding
  - separator “;”
- XSLX

**Columns to fill in:**

Column name | Description
--- | ---
LegalEntityCode | Employee legal entity code
EmployeeNumber | Employee payroll number
LastName | Last name
FirstName | First name
Account number or name (one column per account) | Value to import for the account defined in the header.


*Remark:
A template file can be downloaded from the import page (Credit / Debit> A group of collaborators> File import).*

In the event of a malformed (or unrecognized) file, no data will be imported; the problems detected will be specified in the `globalErrors` field.

If successful, the number of imported lines is indicated by the “successLinesCount” field; the lines in error are detailed in the `lineErrors` field.


*Remarks:
Any import made by the API is of course available in the import history.
A simulation returns the same level of information, but does not trigger an import*

**List of errors handled**

Here is the list of fatal errors, which can be returned in the `globalErrors`:
- Unauthorized
- FileEmpty,
- FileExtensionNotSupported,
- ColumnsFormatNotSupported,
- AccountColumnMissing,
- ColumnNamesDistinct,
- LineErrorForbiddenInStrictMode,

The list of line processing errors, which can be restored in the `lineErrors`:
- AccountNotFound,
- AccountsNotFound,
- AccountColumnsProcessing,
- LegalEntityCodesNotFound,
- MissingValuesForAccount,
- AccountNotAvailableForUser,
- LegalEntityCodeRequired,
- EmployeeNumberRequired,
- LoginRequired,
- LoginNotFound,
- AccountNumberRequired,
- LegalEntityNotFound,
- EmployeeNumberNotExist,
- EmployeeNumberNotInLegalEntity,
- FistNameAndLastNameNotMatching,
- FistNameNotMatching,
- LastLameNotMatching,
- FistNameAndLastNameNotMatchingEmployeeNumber,
- FistNameNotMatchingEmployeeNumber,
- LastLameNotMatchingEmployeeNumber,
- FistNameAndLastNameNotMatchingLogin,
- FistNameNotMatchingLogin,
- LastLameNotMatchingLogin,
- DuplicatedLine,
- AmbiguousLegalEntity,
- ColumnNotExists,
- LegalEntityNameNotAvailable,
- AccountNameNotUnique

The list of import generation errors:
- UnableToCreditAccount


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
entitlements_batch_import_response = (
    luccatimmiabsences.imports.entitlements_batch_import(
        strict=False,
        simulate=False,
        file="string_example",
        description="string_example",
        reference_date="1970-01-01T00:00:00.00Z",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### strict: `bool`<a id="strict-bool"></a>

In strict mode, if the import has errors, nothing is imported. Without strict mode, the lines in error are ignored and those in success are imported.

##### simulate: `bool`<a id="simulate-bool"></a>

Allows you to simulate the import. In this case, the response indicates the theoretical result of the import without any data being recorded.

##### file: `str`<a id="file-str"></a>

##### description: `str`<a id="description-str"></a>

Description of the entries generated by the import (visible to users in the account details).

##### reference_date: `datetime`<a id="reference_date-datetime"></a>

Reference date (text mode). Respect the format: yyyy-MM-ddThh: mm: ss

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ImportsEntitlementsBatchImportRequest`](./lucca_timmi_absences_python_sdk/type/imports_entitlements_batch_import_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ImportsEntitlementsBatchImportResponse`](./lucca_timmi_absences_python_sdk/pydantic/imports_entitlements_batch_import_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/figgo/api/public/services/v1.0/leaveEntitlementsImport` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmiabsences.imports.get_progress`<a id="luccatimmiabsencesimportsget_progress"></a>

Retrieve the progress of Import leaves API request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_progress_response = luccatimmiabsences.imports.get_progress(
    summary_id="summaryId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### summary_id: `str`<a id="summary_id-str"></a>

Identifier of the import

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timmi-absences/api/imports/v1.0/leavePeriods/{summaryId}/progress` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmiabsences.imports.import_leave_entitlements`<a id="luccatimmiabsencesimportsimport_leave_entitlements"></a>

**Supported file formats:**
- CSV
  - "UTF-8" encoding
  - separator “;”
- XSLX

**Columns to fill in:**

Column name | Description
--- | ---
LegalEntityCode | Employee legal entity code
EmployeeNumber | Employee payroll number
LastName | Last name
FirstName | First name
Account number or name (one column per account) | Value to import for the account defined in the header.


*Remark:
A template file can be downloaded from the import page (Credit / Debit> A group of collaborators> File import).*

In the event of a malformed (or unrecognized) file, no data will be imported; the problems detected will be specified in the `globalErrors` field.

If successful, the number of imported lines is indicated by the “successLinesCount” field; the lines in error are detailed in the `lineErrors` field.


*Remarks:
Any import made by the API is of course available in the import history.
A simulation returns the same level of information, but does not trigger an import*

**List of errors handled**

Here is the list of fatal errors, which can be returned in the `globalErrors`:
- Unauthorized
- FileEmpty,
- FileExtensionNotSupported,
- ColumnsFormatNotSupported,
- AccountColumnMissing,
- ColumnNamesDistinct,
- LineErrorForbiddenInStrictMode,

The list of line processing errors, which can be restored in the `lineErrors`:
- AccountNotFound,
- AccountsNotFound,
- AccountColumnsProcessing,
- LegalEntityCodesNotFound,
- MissingValuesForAccount,
- AccountNotAvailableForUser,
- LegalEntityCodeRequired,
- EmployeeNumberRequired,
- LoginRequired,
- LoginNotFound,
- AccountNumberRequired,
- LegalEntityNotFound,
- EmployeeNumberNotExist,
- EmployeeNumberNotInLegalEntity,
- FistNameAndLastNameNotMatching,
- FistNameNotMatching,
- LastLameNotMatching,
- FistNameAndLastNameNotMatchingEmployeeNumber,
- FistNameNotMatchingEmployeeNumber,
- LastLameNotMatchingEmployeeNumber,
- FistNameAndLastNameNotMatchingLogin,
- FistNameNotMatchingLogin,
- LastLameNotMatchingLogin,
- DuplicatedLine,
- AmbiguousLegalEntity,
- ColumnNotExists,
- LegalEntityNameNotAvailable,
- AccountNameNotUnique

The list of import generation errors:
- UnableToCreditAccount


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
import_leave_entitlements_response = (
    luccatimmiabsences.imports.import_leave_entitlements(
        strict=False,
        simulate=False,
        file="string_example",
        description="string_example",
        reference_date="1970-01-01T00:00:00.00Z",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### strict: `bool`<a id="strict-bool"></a>

In strict mode, if the import has errors, nothing is imported. Without strict mode, the lines in error are ignored and those in success are imported.

##### simulate: `bool`<a id="simulate-bool"></a>

Allows you to simulate the import. In this case, the response indicates the theoretical result of the import without any data being recorded.

##### file: `str`<a id="file-str"></a>

##### description: `str`<a id="description-str"></a>

Description of the entries generated by the import (visible to users in the account details).

##### reference_date: `datetime`<a id="reference_date-datetime"></a>

Reference date (text mode). Respect the format: yyyy-MM-ddThh: mm: ss

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ImportsImportLeaveEntitlementsRequest`](./lucca_timmi_absences_python_sdk/type/imports_import_leave_entitlements_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ImportsEntitlementsBatchImportResponse`](./lucca_timmi_absences_python_sdk/pydantic/imports_entitlements_batch_import_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timmi-absences/api/public/services/v1.0/leaveEntitlementsImport` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmiabsences.imports.replace_entitlements`<a id="luccatimmiabsencesimportsreplace_entitlements"></a>

**Supported file formats:**
- CSV
  - "UTF-8" encoding
  - separator “;”
- XSLX

**Columns to fill in:**

Column name | Description
--- | ---
LegalEntityCode | Employee legal entity code
EmployeeNumber | Employee payroll number
LastName | Last name
FirstName | First name
Account number or name (one column per account) | Value to import for the account defined in the header.


*Remark:
A template file can be downloaded from the import page (Credit / Debit> A group of collaborators> File import).*

In the event of a malformed (or unrecognized) file, no data will be imported; the problems detected will be specified in the `globalErrors` field.

If successful, the number of imported lines is indicated by the “successLinesCount” field; the lines in error are detailed in the `lineErrors` field.


*Remarks:
Any import made by the API is of course available in the import history.
A simulation returns the same level of information, but does not trigger an import*

**List of errors handled**

Here is the list of fatal errors, which can be returned in the `globalErrors`:
- Unauthorized
- FileEmpty,
- FileExtensionNotSupported,
- ColumnsFormatNotSupported,
- AccountColumnMissing,
- ColumnNamesDistinct,
- LineErrorForbiddenInStrictMode,

The list of line processing errors, which can be restored in the `lineErrors`:
- AccountNotFound,
- AccountsNotFound,
- AccountColumnsProcessing,
- LegalEntityCodesNotFound,
- MissingValuesForAccount,
- AccountNotAvailableForUser,
- LegalEntityCodeRequired,
- EmployeeNumberRequired,
- LoginRequired,
- LoginNotFound,
- AccountNumberRequired,
- LegalEntityNotFound,
- EmployeeNumberNotExist,
- EmployeeNumberNotInLegalEntity,
- FistNameAndLastNameNotMatching,
- FistNameNotMatching,
- LastLameNotMatching,
- FistNameAndLastNameNotMatchingEmployeeNumber,
- FistNameNotMatchingEmployeeNumber,
- LastLameNotMatchingEmployeeNumber,
- FistNameAndLastNameNotMatchingLogin,
- FistNameNotMatchingLogin,
- LastLameNotMatchingLogin,
- DuplicatedLine,
- AmbiguousLegalEntity,
- ColumnNotExists,
- LegalEntityNameNotAvailable,
- AccountNameNotUnique

The list of import generation errors:
- UnableToCreditAccount


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
replace_entitlements_response = luccatimmiabsences.imports.replace_entitlements(
    strict=False,
    simulate=False,
    file="string_example",
    description="string_example",
    reference_date="1970-01-01T00:00:00.00Z",
    entry_types="AutoAccruals,ManualAccruals,Regularizations",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### strict: `bool`<a id="strict-bool"></a>

In strict mode, if the import has errors, nothing is imported. Without strict mode, the lines in error are ignored and those in success are imported.

##### simulate: `bool`<a id="simulate-bool"></a>

Allows you to simulate the import. In this case, the response indicates the theoretical result of the import without any data being recorded.

##### file: `str`<a id="file-str"></a>

##### description: `str`<a id="description-str"></a>

Description of the entries generated by the import (visible to users in the account details).

##### reference_date: `datetime`<a id="reference_date-datetime"></a>

Reference date (text mode). Respect the format: yyyy-MM-ddThh: mm: ss

##### entry_types: `str`<a id="entry_types-str"></a>

Types of entries to take into account, separated by commas, from the following list: AutoAccruals, ManualAccruals, Regularisations, EntitlementsImport, Seniority, Fractionnement, TimeSavings, Comp  By default: `AutoAccruals, ManualAccruals, Regularizations` which correspond to the main cases of acquisition (automatic acquisition, manual adjustments, regularisations).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ImportsReplaceEntitlementsRequest`](./lucca_timmi_absences_python_sdk/type/imports_replace_entitlements_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ImportsEntitlementsBatchImportResponse`](./lucca_timmi_absences_python_sdk/pydantic/imports_entitlements_batch_import_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/figgo/api/public/services/v1.0/leaveEntitlementsReplace` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmiabsences.imports.replace_entitlements_0`<a id="luccatimmiabsencesimportsreplace_entitlements_0"></a>

**Supported file formats:**
- CSV
  - "UTF-8" encoding
  - separator “;”
- XSLX

**Columns to fill in:**

Column name | Description
--- | ---
LegalEntityCode | Employee legal entity code
EmployeeNumber | Employee payroll number
LastName | Last name
FirstName | First name
Account number or name (one column per account) | Value to import for the account defined in the header.


*Remark:
A template file can be downloaded from the import page (Credit / Debit> A group of collaborators> File import).*

In the event of a malformed (or unrecognized) file, no data will be imported; the problems detected will be specified in the `globalErrors` field.

If successful, the number of imported lines is indicated by the “successLinesCount” field; the lines in error are detailed in the `lineErrors` field.


*Remarks:
Any import made by the API is of course available in the import history.
A simulation returns the same level of information, but does not trigger an import*

**List of errors handled**

Here is the list of fatal errors, which can be returned in the `globalErrors`:
- Unauthorized
- FileEmpty,
- FileExtensionNotSupported,
- ColumnsFormatNotSupported,
- AccountColumnMissing,
- ColumnNamesDistinct,
- LineErrorForbiddenInStrictMode,

The list of line processing errors, which can be restored in the `lineErrors`:
- AccountNotFound,
- AccountsNotFound,
- AccountColumnsProcessing,
- LegalEntityCodesNotFound,
- MissingValuesForAccount,
- AccountNotAvailableForUser,
- LegalEntityCodeRequired,
- EmployeeNumberRequired,
- LoginRequired,
- LoginNotFound,
- AccountNumberRequired,
- LegalEntityNotFound,
- EmployeeNumberNotExist,
- EmployeeNumberNotInLegalEntity,
- FistNameAndLastNameNotMatching,
- FistNameNotMatching,
- LastLameNotMatching,
- FistNameAndLastNameNotMatchingEmployeeNumber,
- FistNameNotMatchingEmployeeNumber,
- LastLameNotMatchingEmployeeNumber,
- FistNameAndLastNameNotMatchingLogin,
- FistNameNotMatchingLogin,
- LastLameNotMatchingLogin,
- DuplicatedLine,
- AmbiguousLegalEntity,
- ColumnNotExists,
- LegalEntityNameNotAvailable,
- AccountNameNotUnique

The list of import generation errors:
- UnableToCreditAccount


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
replace_entitlements_0_response = luccatimmiabsences.imports.replace_entitlements_0(
    strict=False,
    simulate=False,
    file="string_example",
    description="string_example",
    reference_date="1970-01-01T00:00:00.00Z",
    entry_types="AutoAccruals,ManualAccruals,Regularizations",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### strict: `bool`<a id="strict-bool"></a>

In strict mode, if the import has errors, nothing is imported. Without strict mode, the lines in error are ignored and those in success are imported.

##### simulate: `bool`<a id="simulate-bool"></a>

Allows you to simulate the import. In this case, the response indicates the theoretical result of the import without any data being recorded.

##### file: `str`<a id="file-str"></a>

##### description: `str`<a id="description-str"></a>

Description of the entries generated by the import (visible to users in the account details).

##### reference_date: `datetime`<a id="reference_date-datetime"></a>

Reference date (text mode). Respect the format: yyyy-MM-ddThh: mm: ss

##### entry_types: `str`<a id="entry_types-str"></a>

Types of entries to take into account, separated by commas, from the following list: AutoAccruals, ManualAccruals, Regularisations, EntitlementsImport, Seniority, Fractionnement, TimeSavings, Comp  By default: `AutoAccruals, ManualAccruals, Regularizations` which correspond to the main cases of acquisition (automatic acquisition, manual adjustments, regularisations).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ImportsReplaceEntitlementsRequest1`](./lucca_timmi_absences_python_sdk/type/imports_replace_entitlements_request1.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ImportsEntitlementsBatchImportResponse`](./lucca_timmi_absences_python_sdk/pydantic/imports_entitlements_batch_import_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timmi-absences/api/public/services/v1.0/leaveEntitlementsReplace` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmiabsences.leave_requests.approve_deny`<a id="luccatimmiabsencesleave_requestsapprove_deny"></a>

Approve or deny a single Leave Request by its unique identifier

Only the Leave Requests pending approval can be approved or denied.

A comment is required to deny a Leave Request.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
luccatimmiabsences.leave_requests.approve_deny(
    leave_request_id="leaveRequestId_example",
    approved=True,
    comment=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### leave_request_id: `str`<a id="leave_request_id-str"></a>

##### approved: `bool`<a id="approved-bool"></a>

##### comment: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_timmi_absences_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="comment-unionbool-date-datetime-dict-float-int-list-str-nonelucca_timmi_absences_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LeaveRequestsApproveDenyRequest`](./lucca_timmi_absences_python_sdk/type/leave_requests_approve_deny_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/leaveRequests/{leaveRequestId}/approvals` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmiabsences.leave_requests.cancel_request`<a id="luccatimmiabsencesleave_requestscancel_request"></a>

Request to cancel a single Leave Request by its unique identifier

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
luccatimmiabsences.leave_requests.cancel_request(
    leave_request_id="leaveRequestId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### leave_request_id: `str`<a id="leave_request_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/leaveRequests/{leaveRequestId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmiabsences.leave_requests.get_by_id`<a id="luccatimmiabsencesleave_requestsget_by_id"></a>

Retrieve a single Leave Request by its unique identifier

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = luccatimmiabsences.leave_requests.get_by_id(
    leave_request_id="leaveRequestId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### leave_request_id: `str`<a id="leave_request_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`LeaveRequestsGetByIdResponse`](./lucca_timmi_absences_python_sdk/pydantic/leave_requests_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/leaveRequests/{leaveRequestId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmiabsences.leave_requests.list`<a id="luccatimmiabsencesleave_requestslist"></a>

Retrieve a list of Leave Requests

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = luccatimmiabsences.leave_requests.list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`LeaveRequestsListResponse`](./lucca_timmi_absences_python_sdk/pydantic/leave_requests_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/leaveRequests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmiabsences.leaves.cancel_leave_by_id`<a id="luccatimmiabsencesleavescancel_leave_by_id"></a>

Cancel a single Leave by its unique identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
luccatimmiabsences.leaves.cancel_leave_by_id(
    leave_id="leaveId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### leave_id: `str`<a id="leave_id-str"></a>

Identifier of the leave.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/leaves/{leaveId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmiabsences.leaves.get_approved_list`<a id="luccatimmiabsencesleavesget_approved_list"></a>

Retrieve a list of approved leaves for one or several users on a given period.

The `leavePeriod.ownerId` query parameter is required ans is used to: 

- retrieve Leaves of a specific user: `?leavePeriod.ownerId=5`
- retrieve Leaves of several users: `?leavePeriod.ownerId=5,6`
- retrieve Leaves of a specific group of users: `?leavePeriod.owner.departmentId=3`

The `date` query parameter can operate comparisons with a given date-time value:

- `?date=2021-01-01`: strict equality.
- `?date=since,2021-01-01`: greater than or equal.
- `?date=until,2021-01-01`: lower than or equal.
- `?date=between,2021-01-01,2021-01-31`: comprised between two dates.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_approved_list_response = luccatimmiabsences.leaves.get_approved_list(
    paging="100,0",
    leave_period_owner_id=[None],
    date="date_example",
    leave_account_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### paging: `str`<a id="paging-str"></a>

{offset},{limit}. Defaults to 0,1000.

##### leave_period_owner_id: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_timmi_absences_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="leave_period_owner_id-listunionbool-date-datetime-dict-float-int-list-str-nonelucca_timmi_absences_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Employee's identifier

##### date: `str`<a id="date-str"></a>

{comparator},{date-time}

##### leave_account_id: `str`<a id="leave_account_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`LeavesGetApprovedListResponse`](./lucca_timmi_absences_python_sdk/pydantic/leaves_get_approved_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/leaves` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmiabsences.leaves.get_by_id`<a id="luccatimmiabsencesleavesget_by_id"></a>

Retrieve a single Leave by its unique identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = luccatimmiabsences.leaves.get_by_id(
    leave_id="leaveId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### leave_id: `str`<a id="leave_id-str"></a>

Identifier of the leave.

#### 🔄 Return<a id="🔄-return"></a>

[`LeavesGetByIdResponse`](./lucca_timmi_absences_python_sdk/pydantic/leaves_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/leaves/{leaveId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
