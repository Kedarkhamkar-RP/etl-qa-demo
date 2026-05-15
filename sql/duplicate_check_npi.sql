-- TC-004: No duplicate NPI values allowed
-- Expected Result: Count should be 0

SELECT COUNT(*) AS duplicate_npi_count
FROM (
    SELECT NPI
    FROM dbviews.vw_provider_rad_roster
    WHERE NPI IS NOT NULL
    GROUP BY NPI
    HAVING COUNT(*) > 1
) duplicates;
