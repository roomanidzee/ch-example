CREATE DATABASE test_db;

CREATE TABLE test_db.football_table(

   match_date Date,
   record_time DateTime,
   home_country String,
   guest_country String,
   home_score Int64,
   guest_score Int64,
   match_type Enum('friendly' = 1, 'uefa' = 2, 'fifa' = 3),
   match_city String,
   match_country String

)
ENGINE = MergeTree
PARTITION BY record_time
ORDER BY (match_type, record_time)
TTL match_date + INTERVAL 3 DAY;