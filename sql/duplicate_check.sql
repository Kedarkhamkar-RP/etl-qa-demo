SELECT COUNT(*)
FROM
(
   SELECT NPI
   FROM dbviews.VW_Provider_Rad_Roster
   GROUP BY NPI
   HAVING COUNT(*) > 1
) a