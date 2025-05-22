//  Q2) Build a new Circle class with the followingbasic features:
//   Attributes:
//  o Centerpoint-Buildinstancevariablesfor the circle’s centerpoint 
// (myXandmyYrepresentedasdoublevalues).
//  o Diameter-Buildaninstancevariableforthecircle’sdiameter(myDiameteralso 
// represented as a doublevalue).
//   Behaviors
//  o Defaultconstructor- Build a defaultconstructorthatinitializes the circle’s center 
// point to (0, 0) and its diameterto 100.
//  o Accessormethods-Buildaccessormethodsfor thetwocenter coordinatesand the 
// diameter.
//   Invariant
//  o Thecircle’sdiametershouldalwaysbe non-negative.maintainthe integrityofeach 
// circle object by ensuring that the class invariant (that the diametershould be non
// negative) is true at all times.
//  If the diameteris negative then throwuser defined exception.




class NegativeDiameterException extends Exception {
    public NegativeDiameterException(String message) {
        super(message);
    }
}

public class circle {
    private double myX;
    private double myY;
    private double myDiameter;

    public circle() {
        this.myX = 0.0;
        this.myY = 0.0;
        this.myDiameter = 100.0;
    }

    public circle(double x, double y, double diameter) throws NegativeDiameterException {
        if (diameter < 0) {
            throw new NegativeDiameterException("Diameter cannot be negative.");
        }
        this.myX = x;
        this.myY = y;
        this.myDiameter = diameter;
    }

    public double getMyX() {
        return myX;
    }

    public double getMyY() {
        return myY;
    }

    public double getMyDiameter() {
        return myDiameter;
    }
    public static void main(String[] args) {
        try {
          
            circle c1 = new circle(10.0, 20.0, 50.0);
            System.out.println("Circle 1 - X: " + c1.getMyX() + ", Y: " + c1.getMyY() + ", Diameter: " + c1.getMyDiameter());

            circle c2 = new circle(15.0, 25.0, -5.0);
        } catch (NegativeDiameterException e) {
            System.out.println("Error: " + e.getMessage()); 
        }
    }
}
