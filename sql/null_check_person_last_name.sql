-- TC-002: Person_Last_Name cannot be null
-- Expected Result: Count should be 0

SELECT COUNT(*) AS null_last_name_count
FROM dbviews.vw_provider_rad_roster
WHERE person_last_name IS NULL
   OR LTRIM(RTRIM(person_last_name)) = '';
