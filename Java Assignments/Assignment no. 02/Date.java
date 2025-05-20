public class Date {
    private int month;
    private int day;
    private int year;

    public Date(int month, int day, int year) {
        this.month = month;
        this.day = day;
        this.year = year;
    }

    public int getMonth() {
        return month;
    }

    public void setMonth(int month) {
        this.month = month;
    }

    public int getDay() {
        return day;
    }

    public void setDay(int day) {
        this.day = day;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public void displayDate() {
        System.out.println(month + "/" + day + "/" + year);
    }

    public static void main(String[] args) {

        Date date = new Date(5, 21, 2025);

        System.out.print("Original date: ");
        date.displayDate();

        date.setMonth(12);
        date.setDay(31);
        date.setYear(2024);

        System.out.print("Updated date: ");
        date.displayDate();
    }
}
