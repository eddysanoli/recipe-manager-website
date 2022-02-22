// Initial number of ingredients on the form
let numIngredients = document.getElementById("ingredient-inputs").children.length;
console.log("Number of initial ingredients:", numIngredients);

// =============================
// FUNCTIONS
// =============================

// Function: Delete an ingredient entry
const ingredientDeleteFcn = (deleteBtn) => {

    // Log the button pressed
    console.log(deleteBtn.name);

    // Remove the parent element of the button ("ingredient-inputs__element" div)
    deleteBtn.parentElement.remove();

    // Decrease the number of ingredients
    numIngredients --;

    // Get the "input elements" for each ingredient
    let inputElements = document.getElementsByClassName("ingredient-inputs__element");

    // Re-index all the "ingredient-inputs" elements (0 - N)
    Array.from(inputElements).forEach((inputElement, idx) => {

        // Change the list number on each numbered input in the element
        for (let i = 0; i < inputElement.children.length; i++) {

            switch (inputElement.children[i].id) {
                case `ingredient-name`:
                    inputElement.children[i].name = `ingredient-name-${idx}`;
                    break;
                case "ingredient-amount":
                    inputElement.children[i].name = `ingredient-amount-${idx}`;
                    break;
                case "ingredient-unit":
                    inputElement.children[i].name = `ingredient-unit-${idx}`;
                    break;
                case "ingredient-delete":
                    inputElement.children[i].name = `ingredient-delete-${idx}`;
                    break;
            }

        }
    })
}

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
                ingredientInputsElement.children[i].addEventListener("click", () => ingredientDeleteFcn(ingredientInputsElement.children[i]));
                break;
        }
    }

    // Add new empty input at the end of the block
    ingredientInputs.append(ingredientInputsElement);

});

// =============================
// DELETE BUTTONS LOGIC
// =============================

// Get all delete buttons
const deleteBtns = document.getElementsByClassName("ingredient-delete");

// Enable the delete function on all buttons
Array.from(deleteBtns).forEach( deleteBtn => {
    deleteBtn.addEventListener("click", () => ingredientDeleteFcn(deleteBtn));
})

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

        // Steps: 
        // 1. Get the group of inputs for the first ingredient
        // 2. Retrieve a list of all the inputs and select the last one (delete button)
        // 3. Disable the button
        ingredientInputs[0].children[numElemIngredient - 1].disabled = true;
    }
    else {

        // Steps: 
        // 1. Get the group of inputs for the ith ingredient
        // 2. Retrieve a list of all the inputs and select the last one (delete button)
        // 3. Enable the button
        for (let i = 0; i < ingredientInputs.length; i++) {
            ingredientInputs[i].children[numElemIngredient - 1].disabled = false;
        }
    }

}, 100);