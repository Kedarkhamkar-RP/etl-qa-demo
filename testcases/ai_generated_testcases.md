# Data Quality Test Cases for dbviews.vw_provider_rad_roster

This file contains the test cases for the Provider Rad Roster view based on the requested validation rules.

## Test Cases

### TC-001: Person_first_Name cannot be null
- **Description:** Verify that `person_first_name` is present for every row in `dbviews.vw_provider_rad_roster`.
- **Expected Result:** Zero rows where `person_first_name` is NULL or blank.
- **SQL file:** `sql/null_check_person_first_name.sql`
- **Test:** `tests/test_provider_rad_roster_view.py::test_person_first_name_not_null`

### TC-002: Person_Last_Name cannot be null
- **Description:** Verify that `person_last_name` is present for every row in `dbviews.vw_provider_rad_roster`.
- **Expected Result:** Zero rows where `person_last_name` is NULL or blank.
- **SQL file:** `sql/null_check_person_last_name.sql`
- **Test:** `tests/test_provider_rad_roster_view.py::test_person_last_name_not_null`

### TC-003: NPI cannot be null
- **Description:** Verify that `NPI` is present for every row in `dbviews.vw_provider_rad_roster`.
- **Expected Result:** Zero rows where `NPI` is NULL or blank.
- **SQL file:** `sql/null_check_npi.sql`
- **Test:** `tests/test_provider_rad_roster_view.py::test_npi_not_null`

### TC-004: No duplicate NPIs allowed
- **Description:** Verify `NPI` values are unique in `dbviews.vw_provider_rad_roster`.
- **Expected Result:** Zero duplicate `NPI` values.
- **SQL file:** `sql/duplicate_check_npi.sql`
- **Test:** `tests/test_provider_rad_roster_view.py::test_no_duplicate_npi`

### TC-005: hire_date cannot be greater than termination_date
- **Description:** Validate that `hire_date` is not after `termination_date`.
- **Expected Result:** Zero rows where `hire_date > termination_date`.
- **SQL file:** `sql/date_range_check_hire_termination.sql`
- **Test:** `tests/test_provider_rad_roster_view.py::test_hire_date_not_greater_than_termination_date`

### TC-006: FTE_percentage should be between 0 and 1
- **Description:** Verify that `fte_percentage` values are within the inclusive range [0, 1].
- **Expected Result:** Zero rows where `fte_percentage` is NULL, < 0, or > 1.
- **SQL file:** `sql/fte_percentage_check.sql`
- **Test:** `tests/test_provider_rad_roster_view.py::test_fte_percentage_in_range`

### TC-007: Local_practice_Name cannot be null
- **Description:** Verify that `local_practice_name` is present for every row.
- **Expected Result:** Zero rows where `local_practice_name` is NULL or blank.
- **SQL file:** `sql/null_check_local_practice_name.sql`
- **Test:** `tests/test_provider_rad_roster_view.py::test_local_practice_name_not_null`

## Notes
- These tests assume `dbviews.vw_provider_rad_roster` is available and the column names are exactly as specified.
- If the pipeline runs in CI, make sure the database credentials are configured as environment variables or via a `.env` file.
- Run the tests with:
  ```bash
  pytest tests/test_provider_rad_roster_view.py -v
  ```
