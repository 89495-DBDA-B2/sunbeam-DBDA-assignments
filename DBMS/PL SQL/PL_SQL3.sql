-- Q.3 Create a procedure to Convert a temperature in Fahrenheit (F) to its equivalent in Celsius (C) and vice versa. The required formulae are:- 
-- C= (F-32)*5/9 F= 9/5*C + 32
-- Ans.

 
DROP PROCEDURE IF EXISTS t_f;
DELIMITER $$

CREATE PROCEDURE t_f()

BEGIN
	DECLARE C FLOAT DEFAULT 90;
	DECLARE F FLOAT DEFAULT 50;
	DECLARE result_c FLOAT;
	DECLARE result_f FLOAT;
	
	SET result_c=(F-32)*5/9;
	
	SET result_f= (9/5) *C + 32;
	
	SELECT CONCAT("Fahrenheit: ",result_f);
	SELECT CONCAT("Celsius : ",result_c);
END $$


DELIMITER ;
