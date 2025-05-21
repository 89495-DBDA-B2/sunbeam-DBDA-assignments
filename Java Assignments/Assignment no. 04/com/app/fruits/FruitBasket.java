package com.app.fruits;


import java.util.Scanner;

public class FruitBasket {
    private static Fruit[] basket;
    private static int counter = 0;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter basket size: ");
        int size = scanner.nextInt();
        basket = new Fruit[size];

        while (true) {
            System.out.println("\nMenu:");
            System.out.println("1. Add Mango");
            System.out.println("2. Add Orange");
            System.out.println("3. Add Apple");
            System.out.println("4. Display all fruit names");
            System.out.println("5. Display details of all fresh fruits");
            System.out.println("6. Display tastes of all stale fruits");
            System.out.println("7. Mark a fruit as stale");
            System.out.println("8. Mark all sour fruits stale");
            System.out.println("0. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 0:
                    System.out.println("Exiting...");
                    return;
                case 1:
                    if (counter < size) {
                        System.out.print("Enter weight: ");
                        double weight = scanner.nextDouble();
                        System.out.print("Enter color: ");
                        String color = scanner.next();
                        basket[counter++] = new Mango(weight, color);
                    } else {
                        System.out.println("Basket is full!");
                    }
                    break;
                case 2:
                    if (counter < size) {
                        System.out.print("Enter weight: ");
                        double weight = scanner.nextDouble();
                        System.out.print("Enter color: ");
                        String color = scanner.next();
                        basket[counter++] = new Orange(weight, color);
                    } else {
                        System.out.println("Basket is full!");
                    }
                    break;
                case 3:
                    if (counter < size) {
                        System.out.print("Enter weight: ");
                        double weight = scanner.nextDouble();
                        System.out.print("Enter color: ");
                        String color = scanner.next();
                        basket[counter++] = new Apple(weight, color);
                    } else {
                        System.out.println("Basket is full!");
                    }
                    break;
                case 4:
                    for (Fruit fruit : basket) {
                        if (fruit != null) {
                            System.out.println(fruit.getName());
                        }
                    }
                    break;
                case 5:
                    for (Fruit fruit : basket) {
                        if (fruit != null && fruit.isFresh()) {
                            System.out.println(fruit + ", Taste: " + fruit.taste());
                        }
                    }
                    break;
                case 6:
                    for (Fruit fruit : basket) {
                        if (fruit != null && !fruit.isFresh()) {
                            System.out.println(fruit.taste());
                        }
                    }
                    break;
                case 7:
                    System.out.print("Enter index to mark as stale: ");
                    int index = scanner.nextInt();
                    if (index >= 0 && index < counter) {
                        basket[index].setFresh(false);
                        System.out.println("Fruit at index " + index + " is now stale.");
                    } else {
                        System.out.println("Invalid index!");
                    }
                    break;
                case 8:
                    for (Fruit fruit : basket) {
                        if (fruit != null && fruit.taste().equals("Sour")) {
                            fruit.setFresh(false);
                        }
                    }
                    System.out.println("All sour fruits are now stale.");
                    break;
                default:
                    System.out.println("Invalid choice!");
            }
        }
    }
}
