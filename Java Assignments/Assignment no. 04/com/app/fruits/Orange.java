package com.app.fruits;

public class Orange extends Fruit {
    public Orange(double weight, String color) {
        super("Orange", weight, color);
    }

    @Override
    public String taste() {
        return "Sour";
    }
}
