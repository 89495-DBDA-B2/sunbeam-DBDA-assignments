-- Q.5 Your block should read in two real numbers and tell whether the product of the two --- numbers is equal to or greater than 100.
-- Ans.


DROP PROCEDURE IF EXISTS pro;
DELIMITER $$

CREATE PROCEDURE pro(IN n1 INT,IN n2 INT)
BEGIN
	DECLARE result FLOAT;
	
	SET result = n1 * n2;
	
	IF result >= 100 THEN
		SELECT 'product is equal to or greater than 100' as Result;
	ELSE
		SELECT 'product is not equal to or greater than 100' as Result;
	END IF;
	
END $$

DELIMITER ;
