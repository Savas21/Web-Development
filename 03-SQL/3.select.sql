/* Select all **/
SELECT * FROM flights;

/* Select specific column **/
SELECT origin ,destination FROM flights;

/* Select particular row using  Where Clause**/
SELECT * FROM flights WHERE id = 3;
SELECT * FROM flights WHERE origin  = 'New York';
/* Select  with comparasion **/
SELECT * FROM flights WHERE duration > 500 ;


/* Select  by using lojical operation AND and OR **/
SELECT * FROM flights 
WHERE destionation  = 'Paris' AND duration >500;

SELECT * FROM flights 
WHERE destionation  = 'Paris' OR duration >500;


/* AVG, MIN AND MAX  functions **/

SELECT AVG(duration) FROM flighs;
SELECT AVG(duration) FROM flighs WHERE origin  = 'New York';

SELECT MIN(duration) FROM flighs;
SELECT * FROM flighs WHERE origin  = 245;



/* COUNT ROWS in the table by using Count Function **/
SELECT COUNT(*) FROM flighs;
SELECT COUNT(*) FROM flighs WHERE  origin  = 'New York';

/* using IN key word to select range of rows **/
SELECT * FROM flighs WHERE  origin  IN('New York','Lima');


/* using string methods to select range of rows **/
SELECT * FROM flighs WHERE  origin  LIKE '%a%';

/* lımıt and order . It is useful when there is ordered list  **/
SELECT * FROM flighs LIMIT 2;
SELECT * FROM flighs  ORDER BY duration ASC;
/* SELECT SHORTEST 3 FLIGHTS  **/
SELECT * FROM flighs  ORDER BY duration ASC LIMIT 3;
SELECT * FROM flighs  ORDER BY duration DES LIMIT 3;




