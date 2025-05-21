package com.app.fruits;

public abstract class Fruit {
    protected String name;
    protected String color;
    protected double weight;
    protected boolean isFresh;

    public Fruit(String name, double weight, String color) {
        this.name = name;
        this.weight = weight;
        this.color = color;
        this.isFresh = true;
    }

    public String getName() {
        return name;
    }

    public boolean isFresh() {
        return isFresh;
    }

    public void setFresh(boolean isFresh) {
        this.isFresh = isFresh;
    }

    @Override
    public String toString() {
        return "Name: " + name + ", Color: " + color + ", Weight: " + weight;
    }

    public abstract String taste();
}
