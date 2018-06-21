UPDATE flights
    /* WHAT WE UPDATE **/
    SET duration = 430
    /* WHERE WE UPDATE **/
    WHERE origin = 'New York'
    ANd duration = 'LONDON'

/* Delete everything from table which match the condition **/
DELETE FROM flights
    WHERE destionation= 'Tokyo';