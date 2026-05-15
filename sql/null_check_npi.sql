-- TC-003: NPI cannot be null
-- Expected Result: Count should be 0

SELECT COUNT(*) AS null_npi_count
FROM dbviews.vw_provider_rad_roster
WHERE NPI IS NULL
   OR LTRIM(RTRIM(NPI)) = '';
