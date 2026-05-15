-- TC-007: Local_practice_Name cannot be null
-- Expected Result: Count should be 0

SELECT COUNT(*) AS null_local_practice_name_count
FROM dbviews.vw_provider_rad_roster
WHERE local_practice_name IS NULL
   OR LTRIM(RTRIM(local_practice_name)) = '';
