function pizzaOven(crust, sauce, cheeses, toppings) {
    var pizza = {};
    pizza.crust = crust;
    pizza.sauce = sauce;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

var pizza1 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]);
var pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
var pizza3 = pizzaOven("gluten free", "pesto", ["parmesan"], ["mushrooms", "chicken", "olives"]);
var pizza4 = pizzaOven("stuffed crust", "bbq", ["feta", "cheddar"], ["onions", "tomatoes"]);

console.log(pizza1);
console.log(pizza2);
console.log(pizza3);
console.log(pizza4);
