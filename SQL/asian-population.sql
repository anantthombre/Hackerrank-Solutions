# Link to the coding question -  https://www.hackerrank.com/challenges/asian-population

SELECT SUM(CITY.POPULATION)
FROM CITY
INNER JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE COUNTRY.CONTINENT = 'Asia'
