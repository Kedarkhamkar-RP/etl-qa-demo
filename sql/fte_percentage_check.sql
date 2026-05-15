-- TC-006: FTE_percentage should be between 0 and 1
-- Expected Result: Count should be 0

SELECT COUNT(*) AS invalid_fte_percentage_count
FROM dbviews.vw_provider_rad_roster
WHERE fte_percentage IS NOT NULL
    AND (fte_percentage < 0 OR fte_percentage > 1);
