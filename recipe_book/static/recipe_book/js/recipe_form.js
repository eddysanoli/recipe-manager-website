// Initial number of ingredients on the form
let numIngredients = document.getElementById("ingredient-inputs").children.length;
console.log("Number of initial ingredients:", numIngredients);

// =============================
// CREATE NEW INGREDIENT ENTRY
// =============================

// Get "Add Ingredient" button
const addIngredientBtn = document.getElementById("add-ingredient");

// "Add Ingredient" is clicked
addIngredientBtn.addEventListener("click", () => {

    // Increase the number of ingredients
    numIngredients ++;
    
    // Get "Ingredient Inputs" block and element
    let ingredientInputs = document.getElementById("ingredient-inputs");
    let ingredientInputsElement = document.getElementById("ingredient-inputs__element").cloneNode(true);

    // Go through every children of the element
    for (let i = 0; i < ingredientInputsElement.children.length; i++) {
        
        // Clear previously filled parameters
        switch (ingredientInputsElement.children[i].id) {
            case `ingredient-name`:
                ingredientInputsElement.children[i].value = "";
                ingredientInputsElement.children[i].name = `ingredient-name-${numIngredients - 1}`;
                break;
            case "ingredient-amount":
                ingredientInputsElement.children[i].value = "";
                ingredientInputsElement.children[i].name = `ingredient-amount-${numIngredients - 1}`;
                break;
            case "ingredient-unit":
                ingredientInputsElement.children[i].name = `ingredient-unit-${numIngredients - 1}`;
                break;
            case "ingredient-delete":
                ingredientInputsElement.children[i].name = `ingredient-delete-${numIngredients - 1}`;
                break;
        }
    }

    // Add new empty input at the end of the block
    ingredientInputs.append(ingredientInputsElement);

});

// =============================
// TOGGLE INGREDIENT DELETE 
// =============================

setInterval(() => {

    // Get array-like element of ingredient inputs
    const ingredientInputs = document.getElementById("ingredient-inputs").children;

    // Number of elements in each group of ingredient inputs
    const numElemIngredient = ingredientInputs[0].children.length;

    // Disable ingredient deletion if there is only one ingredient.
    // If there are more than 1, the deletion is re-enabled.
    if ((ingredientInputs.length) < 2) {
        ingredientInputs[0].children[numElemIngredient - 1].disabled = true;
    }
    else {
        for (let i = 0; i < ingredientInputs.length; i++) {
            ingredientInputs[i].children[numElemIngredient - 1].disabled = false;
        }
    }

}, 300);