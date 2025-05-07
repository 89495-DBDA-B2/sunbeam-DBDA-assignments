--Q.2 Write a procedure that declares an integer variable called num, assigns a value to it, --and computes and inserts into the temp table the value of the variable itself, its square, --and its cube.
--Ans.


DELIMITER $$

DROP PROCEDURE IF EXISTS numsq $$

CREATE PROCEDURE numsq()
BEGIN
    DECLARE n INT DEFAULT 10;
    DECLARE s INT;
    DECLARE c INT;
    
    -- Compute square and cube
    SET s = n * n;
    SET c = n * n * n;
    
    -- Insert values into the temp table
    INSERT INTO temp(num, square, cuben)
    VALUES(n, s, c);
    
END $$

DELIMITER ;

