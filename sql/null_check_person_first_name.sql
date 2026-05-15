-- TC-001: Person_first_Name cannot be null
-- Expected Result: Count should be 0

SELECT COUNT(*) AS null_first_name_count
FROM dbviews.vw_provider_rad_roster
WHERE person_first_name IS NULL
   OR LTRIM(RTRIM(person_first_name)) = '';
