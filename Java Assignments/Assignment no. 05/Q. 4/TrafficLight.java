// Q4) Write an enum type TrafficLight, whose constants (RED, 
// GREEN, YELLOW) take one parameter—the duration of the 
// light.Write a program to test the TrafficLight enum so that it 
// displays the enum constants and their durations. 


public enum TrafficLight {
    RED(60),    // 60 seconds
    GREEN(120), // 120 seconds
    YELLOW(5);  // 5 seconds

    private final int duration;

    // Constructor to set the duration
    TrafficLight(int duration) {
        this.duration = duration;
    }

    // Getter method to retrieve the duration
    public int getDuration() {
        return duration;
    }
}
