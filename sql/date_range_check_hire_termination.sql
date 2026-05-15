-- TC-005: Hire_date cannot be greater than termination_date
-- Expected Result: Count should be 0

SELECT COUNT(*) AS invalid_date_range_count
FROM dbviews.vw_provider_rad_roster
WHERE hire_date IS NOT NULL
  AND termination_date IS NOT NULL
  AND hire_date > termination_date;
