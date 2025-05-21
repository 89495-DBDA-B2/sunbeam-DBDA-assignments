package com.app.fruits;

public class Apple extends Fruit {
    public Apple(double weight, String color) {
        super("Apple", weight, color);
    }

    @Override
    public String taste() {
        return "Sweet and sour";
    }
}
