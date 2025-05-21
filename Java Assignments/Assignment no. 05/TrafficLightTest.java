public class TrafficLightTest {
    public static void main(String[] args) {
        // Iterate over each TrafficLight constant
        for (TrafficLight light : TrafficLight.values()) {
            System.out.printf("%s light duration: %d seconds%n", light, light.getDuration());
        }
    }
}
