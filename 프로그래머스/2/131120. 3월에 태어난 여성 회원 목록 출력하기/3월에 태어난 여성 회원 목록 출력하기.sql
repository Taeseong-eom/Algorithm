SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
from MEMBER_PROFILE
where MONTH(DATE_OF_BIRTH) = 3
AND TLNO is not null 
AND GENDER = 'W'
order by MEMBER_ID ASC