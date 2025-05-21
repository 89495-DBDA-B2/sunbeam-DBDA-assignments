package com.app.fruits;

public class Mango extends Fruit {
    public Mango(double weight, String color) {
        super("Mango", weight, color);
    }

    @Override
    public String taste() {
        return "Sweet";
    }
}
