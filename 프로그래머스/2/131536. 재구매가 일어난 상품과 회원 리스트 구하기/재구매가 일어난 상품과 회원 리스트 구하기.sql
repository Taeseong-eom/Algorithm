SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING count(*) > 1
ORDER BY USER_ID ASC, PRODUCT_ID DESC