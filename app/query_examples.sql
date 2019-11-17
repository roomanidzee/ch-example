SELECT
    match_type,
    record_time,
    home_country,
    guest_country
FROM test_db.football_table
WHERE match_type IN ('friendly', 'fifa')
GROUP BY
    match_type,
    record_time,
    home_country,
    guest_country;

SELECT
    home_country,
    guest_country,
    home_score,
    guest_score,
    CASE
       WHEN home_score > guest_score THEN 'home_country'
       WHEN home_score < guest_score THEN 'guest_country'
       WHEN home_score = guest_score THEN 'draw'
    END as match_result
FROM test_db.football_table
WHERE match_type = 'friendly';