// TypeWriter Effect for herosection

let typingEffect = new Typed(".multitext", {
  strings: [
    "BMI Calculator",
    "1RM Calculator",
    "Water Intake Calculations",
    "Body Composition",
    "And More!",
  ],
  loop: true,
  typeSpeed: 120,
  backSpeed: 100,
  backDelay: 1200,
});

// For tab navigation horizontal scroll buttons

const btnLeft = document.querySelector(".left-btn");
const btnRight = document.querySelector(".right-btn");
const tabMenu = document.querySelector(".tab-menu");

const IconVisibility = () => {
  let scrollLeftValue = Math.ceil(tabMenu.scrollLeft);
  let scrollableWidth = tabMenu.scrollWidth - tabMenu.clientWidth;

  btnLeft.style.display = scrollLeftValue > 0 ? "block" : "none";
  btnRight.style.display = scrollableWidth > scrollLeftValue ? "block" : "none";
};

btnRight.addEventListener("click", () => {
  tabMenu.scrollLeft += 150;
  setTimeout(() => IconVisibility(), 50);
});

btnLeft.addEventListener("click", () => {
  tabMenu.scrollLeft -= 150;
  setTimeout(() => IconVisibility(), 50);
});

window.onload = function () {
  btnRight.style.display =
    tabMenu.scrollWidth > tabMenu.clientWidth ||
    tabMenu.scrollWidth >= window.innerWidth
      ? "block"
      : "none";
  btnLeft.style.display =
    tabMenu.scrollWidth >= window.innerWidth ? "" : "none";
};

window.onresize = function () {
  btnRight.style.display =
    tabMenu.scrollWidth > tabMenu.clientWidth ||
    tabMenu.scrollWidth >= window.innerWidth
      ? "block"
      : "none";
  btnLeft.style.display =
    tabMenu.scrollWidth >= window.innerWidth ? "" : "none";

  let scrollLeftValue = Math.round(tabMenu.scrollLeft);
  btnLeft.style.display = scrollLeftValue > 0 ? "block" : "none";
};

// To make the tab navigation draggable

let activeDrag = false;

tabMenu.addEventListener("mousemove", (drag) => {
  if (!activeDrag) return;
  tabMenu.scrollLeft -= drag.movementX;
  IconVisibility();
  tabMenu.classList.add("dragging");
});

document.addEventListener("mouseup", () => {
  activeDrag = false;
  tabMenu.classList.remove("dragging");
});

tabMenu.addEventListener("mousedown", () => {
  activeDrag = true;
});

// To view tab contents on click tab buttons

const tabs = document.querySelectorAll(".tab");
const tabBtns = document.querySelectorAll(".tab-btn");

const tab_Nav = function (tabBtnClick) {
  tabBtns.forEach((tabBtn) => {
    tabBtn.classList.remove("active");
  });

  tabs.forEach((tab) => {
    tab.classList.remove("active");
  });

  tabBtns[tabBtnClick].classList.add("active");
  tabs[tabBtnClick].classList.add("active");
};

tabBtns.forEach((tabBtn, i) => {
  tabBtn.addEventListener("click", () => {
    tab_Nav(i);
  });
});

//<============== A BMI Calculator ==============>

// Get DOM elements
const ageInput = document.getElementById("fc_age1");
const genderSelect = document.getElementById("gender_dropdown1");
const heightCmInput = document.getElementById("height_cm1");
const weightKgInput = document.getElementById("weight1");
const submit_Bmi_Button = document.getElementById("calc-submit-bmi");
const resultStatement = document.querySelector("#result-statement1");
const resultHeading = resultStatement.querySelector("#result1");
const resultParagraph = resultStatement.querySelector("#result-para1");

function calculateBMI(event) {
  event.preventDefault(); // Prevent form submission

  // Get user inputs
  const age = parseInt(ageInput.value);
  const gender = genderSelect.value;
  const heightCm = parseFloat(heightCmInput.value);
  const weightKg = parseFloat(weightKgInput.value);

  // Calculate BMI
  const bmi = weightKg / (heightCm / 100) ** 2;

  // Determine BMI category
  let category = "";
  if (bmi < 18.5) {
    category = "Underweight";
  } else if (bmi < 25) {
    category = "Normal weight";
  } else if (bmi < 30) {
    category = "Overweight";
  } else {
    category = "Obese";
  }

  // Display result
  resultHeading.textContent = `Your BMI is ${bmi.toFixed(2)}.`;
  resultParagraph.textContent = `This is considered ${category}.`;
  resultStatement.classList.add("show");

}
submit_Bmi_Button.addEventListener("click", calculateBMI);

//<============== A Body Composition Calculator ==============>

// get DOM elements
const form = document.querySelector(".c-2 form");
const ageinput = document.querySelector("#fc_age2");
const gender = document.querySelector("#gender_dropdown2");
const heightinput = document.querySelector("#height_cm2");
const weightinput = document.querySelector("#weight2");
const waistinput = document.querySelector("#waist_cm2");
const neckinput = document.querySelector("#neck_cm2");
const submit_Bc_Button = document.getElementById("calc-submit-bc");
const resultContainer = document.querySelector("#result-statement2");
const resultEl = document.querySelector("#result2");
const resultParaEl = document.querySelector("#result-para2");

// Calculate body fat percentage
function calculateBodyComposition(event) {
  event.preventDefault(); // Prevent form submission

  // Get user inputs
  const age = parseFloat(ageinput.value);
  const gender = genderSelect.value;
  const height = parseFloat(heightinput.value);
  const weight = parseFloat(weightinput.value);
  const waist = parseFloat(waistinput.value);
  const neck = parseFloat(neckinput.value);

  // validate input values
  if (isNaN(age) || isNaN(height) || isNaN(weight) || isNaN(waist) || isNaN(neck)) {
    resultEl.textContent = 'Please enter valid numerical values for all required fields.';
    resultParaEl.textContent = '';
    return;
  }
  
  // Calculate body fat percentage based on gender and input values
  let bodyFat;
  if (gender === "male") {
    bodyFat =
      495 /
        (1.0324 -
          0.19077 * Math.log10(waist - neck) +
          0.15456 * Math.log10(height)) -
      450;
    } else {
    bodyFat =
      495 /
      (1.29579 -
        0.35004 * Math.log10(waist + height - neck) +
        0.221 * Math.log10(height)) -
        450;
      }
      
      
      // calculate body fat in kg
      const bodyFatKg = (weight * bodyFat) / 100;
      
      // Calculate weight loss required to reach target body fat percentage
      const targetBodyFat = 20; // example target body fat percentage
const targetBodyFatKg = (weight * targetBodyFat) / 100;
const weightLossKg = bodyFatKg - targetBodyFatKg;
const weightLossPercent = (weightLossKg / weight) * 100;
      

      // Calculate calories required to burn for target weight loss
      const caloriesPerKg = 7700; // example calories per kg of fat
const caloriesPerPercent = caloriesPerKg / weight; // calculate calories per 1% body fat
const targetCalories = Math.abs(weightLossPercent) * caloriesPerPercent; // calculate target calories
const calories = weightLossKg * caloriesPerKg;
      

      // Display result
      resultEl.textContent = `Your body fat percentage is ${bodyFat.toFixed(2)}%`;
resultParaEl.textContent = `This means you carry ${bodyFatKg.toFixed(2)} kg of body fat. In order to lose ${Math.abs(weightLossPercent).toFixed(2)}% body fat, you need to burn ${targetCalories.toFixed(2)} calories.`;
resultContainer.classList.add("show");

      
}

// Handle form submit
form.addEventListener("submit", calculateBodyComposition);

//<============== A 1RM Calculator ==============>

// select all the necessary HTML elements
const exerciseSelect = document.querySelector('#ex3');
const repInput = document.querySelector('#fc_rep3');
const weightInput = document.querySelector('#weight3');
const resultStatement_rm = document.querySelector('#result-statement3');
const result_rm = document.querySelector('#result3');
const resultPara_rm = document.querySelector('#result-para3');

// create a function to calculate the 1RM based on the user's inputs
function calculate1RM(event) {
  event.preventDefault(); // prevent the form from submitting

  // get the user's inputs
  const exercise = exerciseSelect.value;
  const reps = repInput.value;
  const weight = weightInput.value;

  // calculate the 1RM using the Epley formula
  const oneRM = weight * (1 + (reps / 30));

  // display the result
  result_rm.textContent = `Your 1RM is ${oneRM.toFixed(2)} KG`;
  
  // add some result statement based on the exercise selected
  if (exercise === 'squats') {
    resultPara_rm.textContent = 'Keep squatting heavy and dominate the weight room!';
  } else if (exercise === 'deadlift') {
    resultPara_rm.textContent = 'Great job on the deadlifts, keep up the hard work!';
  } else if (exercise === 'bench_press') {
    resultPara_rm.textContent = 'You are crushing the bench press, keep pushing yourself!';
  } else if (exercise === 'overhead_press') {
    resultPara_rm.textContent = 'You are a beast on the overhead press, keep striving for more!';
  }
  
  // show the result statement
  resultStatement_rm.classList.add("show")
}

// add an event listener to the form submit button
const submitButton = document.querySelector('#calc-submit-rm');
submitButton.addEventListener('click', calculate1RM);

//<============== A Calorie and Macro Calculator ==============>

// Get form elements
const ageInput_cm = document.getElementById('fc_age4');
const genderDropdown = document.getElementById('gender_dropdown4');
const heightInput = document.getElementById('height_cm4');
const weightInput_cm = document.getElementById('weight4');
const goalDropdown = document.getElementById('goal_dropdown4');
const activityLevelDropdown = document.getElementById('al_dropdown4');

// Get result elements
const resultStatement_cm = document.getElementById('result-statement4');
const resultPara = document.getElementById('result-para4');
const resultPro = document.getElementById('result4_pro');
const resultCarb = document.getElementById('result4_carb');
const resultFat = document.getElementById('result4_fat');
const resultTotal = document.getElementById('result4_total');

// Define macros ratios based on goal
const macrosRatio = {
  maintain: { carbs: 50, protein: 25, fat: 25 },
  lose: { carbs: 40, protein: 35, fat: 25 },
  gain: { carbs: 40, protein: 30, fat: 30 },
};

// Define activity level multipliers
const activityLevelMultipliers = {
  sedentary: 1.2,
  lightly: 1.375,
  moderately: 1.55,
  very: 1.725,
  extra: 1.9,
};

// Define calorie constants
const caloriePerGramOfCarb = 4;
const caloriePerGramOfProtein = 4;
const caloriePerGramOfFat = 9;

// Define submit event handler for form
function handleSubmit(event) {
  event.preventDefault();

  // Get user inputs
  const age = parseInt(ageInput_cm.value);
  const gender = genderDropdown.value;
  const height = parseInt(heightInput.value);
  const weight = parseInt(weightInput_cm.value);
  const goal = goalDropdown.value;
  const activityLevel = activityLevelDropdown.value;

  // Calculate BMR
  const bmr = gender === 'male'
    ? 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    : 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age);

  // Calculate TDEE
  const tdee = bmr * activityLevelMultipliers[activityLevel];
  
  // Calculate calorie target based on goal
  const calorieTarget = goal === 'maintain'
    ? tdee
    : goal === 'lose'
      ? tdee - 500
      : tdee + 500;

  // Calculate macros based on ratios and calorie target
  const { carbs, protein, fat } = macrosRatio[goal];
  const carbCalories = calorieTarget * (carbs / 100);
  const proteinCalories = calorieTarget * (protein / 100);
  const fatCalories = calorieTarget * (fat / 100);
  const carbGrams = carbCalories / caloriePerGramOfCarb;
  const proteinGrams = proteinCalories / caloriePerGramOfProtein;
  const fatGrams = fatCalories / caloriePerGramOfFat;

  // Update result elements
  resultPara.textContent = `With a goal of ${goal}-weight, you should have a macro ratio of ${carbs}% carbs / ${protein}% protein / ${fat}% fats.`;
  resultPro.textContent = `${proteinGrams.toFixed(1)} g (${protein}% of calories)`;
  resultCarb.textContent = `${carbGrams.toFixed(1)} g (${carbs}% of calories)`; 
  resultFat.textContent = `${fatGrams.toFixed(1)} g (${fat}% of calories)`; 
  resultTotal.textContent = `${Math.floor(calorieTarget)}`;

  // Show result statement
  resultStatement_cm.classList.add("show")
  }
  
  // Add event listener for form submit
  const form_cm = document.querySelector(".c-4 form");
  form_cm.addEventListener('submit', handleSubmit);

  //<============== A Water Intake Calculator ==============>

const form_wi = document.querySelector('.c-5 form');
const resultStatement_wi = document.querySelector('#result-statement5');
const resultPara_wi = document.getElementById('result-para5');

form_wi.addEventListener('submit', function(event) {
  event.preventDefault();

  // Get input values
  const age = document.getElementById('age_dropdown5').value;
  const gender = document.getElementById('gender_dropdown5').value;
  const height = document.getElementById('height_cm5').value;
  const weight = document.getElementById('weight5').value;
  const season = document.getElementById('season_dropdown5').value;
  const activityLevel = document.getElementById('al_dropdown5').value;

  // Calculate daily water intake
  let dailyWaterIntake = 0;
  if (gender === 'male') {
    dailyWaterIntake = (weight * 35) / 1000;
  } else if (gender === 'female') {
    dailyWaterIntake = (weight * 31) / 1000;
  }

  if (activityLevel === 'lightly') {
    dailyWaterIntake += 0.4 * weight;
  } else if (activityLevel === 'moderately') {
    dailyWaterIntake += 0.6 * weight;
  } else if (activityLevel === 'very') {
    dailyWaterIntake += 0.8 * weight;
  }

  if (season === 'winter') {
    dailyWaterIntake += 200;
  } else if (season === 'summer') {
    dailyWaterIntake += 500;
  }

  if (age === 'teenage') {
    dailyWaterIntake += 500;
  } else if (age === 'young') {
    dailyWaterIntake += 1000;
  } else if (age === 'adult') {
    dailyWaterIntake += 1500;
  } else if (age === 'elder') {
    dailyWaterIntake += 1200;
  }

  const litersWI = dailyWaterIntake / 1000;
  // Display result
  resultPara_wi.innerText = `You have to drink ${litersWI.toFixed(2)} Ltr. per day`;
  resultStatement_wi.classList.add("show");
});

