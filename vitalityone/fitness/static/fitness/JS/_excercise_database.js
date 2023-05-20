// ========= Fetch the ExerciseDB from API =========>

// Fetching categories Types from index

// To Capitalize the words
const dropDownItems = document.querySelector(".options-container");

const capitalize = (word) => {
  return word.charAt(0).toUpperCase() + word.slice(1);
};

// Clear the Dropdown
function clearDropdown() {
  dropDownItems.innerHTML = "";
}

//<=========  Creating Active Effect and Hide & Show the drop-down when clicked on categories =========>

const categoriesBtn = document.querySelectorAll(".category");
const dropDown = document.querySelector("#dropDown");

categoriesBtn.forEach((cat, index) => {
  cat.addEventListener("click", () => {
    // Remove active class from all clickables
    categoriesBtn.forEach((e) => {
      e.classList.remove("active");
    });

    // Add active class to the clicked element
    cat.classList.add("active");

    if (cat.classList.contains("show-dropdown") && index < 3) {
      dropDown.style.display = "block";
    } else {
      dropDown.style.display = "none";
    }

    // Clear the dropdown options
    clearDropdown();

  });
});

//========= The Excercise Categories & Drop-down option =========>

const SearchFunctionality = async () => {
  const selected = document.querySelector(".selected");
  const optionsContainer = document.querySelector(".options-container");
  const searchBox = document.querySelector(".search-box input");

  const optionsList = document.querySelectorAll(".option");

  selected.addEventListener("click", () => {
    optionsContainer.classList.toggle("active");

    searchBox.value = "";
    filterList("");

    if (optionsContainer.classList.contains("active")) {
      searchBox.focus();
    }
  });

  optionsList.forEach((o) => {
    o.addEventListener("click", async () => {
      selected.innerHTML = o.querySelector("label").innerHTML;
      optionsContainer.classList.remove("active");

      const category = o.dataset.category;
      const subCategory = o.dataset.subcategory;
      
      // Fetch exercises based on selected category and subcategory
      await fetchExercises(category, subCategory);
    });
  });

  searchBox.addEventListener("keyup", function (e) {
    filterList(e.target.value);
  });

  const filterList = (searchTerm) => {
    searchTerm = searchTerm.toLowerCase();
    optionsList.forEach((option) => {
      let label =
        option.firstElementChild.nextElementSibling.innerText.toLowerCase();
      if (label.indexOf(searchTerm) != -1) {
        option.style.display = "block";
      } else {
        option.style.display = "none";
      }
    });
  };
};

// Function to fetch exercises based on selected category and subcategory
async function fetchExercises(category, subCategory) {
  const url = "https://wger.de/api/v2/exercise/";
  const api_key = "{{ api_key }}";
  const headers = {
    "Authorization": `Token ${api_key}`,  // Replace with your API key
  };
  const params = {
    "language": 2,  // Language code for English
    "category": category,
    "subcategory": subCategory
  };

  try {
    const response = await fetch(url, { headers, params });
    if (response.ok) {
      const data = await response.json();
      const exercises = data.results;
      
      // Process the fetched exercises and update the UI
      displayExercises(exercises);
    } else {
      console.error("Failed to fetch exercises:", response.status);
    }
  } catch (error) {
    console.error("Error fetching exercises:", error);
  }
}

// Function to display the fetched exercises in the UI
function displayExercises(exercises) {
  // Update the exercise display on the page
  // Replace the code below with your implementation to render exercises in the desired format
  const exerciseContainer = document.querySelector(".exercise-container");
  exerciseContainer.innerHTML = ""; // Clear previous exercises
  
  exercises.forEach((exercise) => {
    const exerciseElement = document.createElement("div");
    exerciseElement.textContent = exercise.name;
    exerciseContainer.appendChild(exerciseElement);
  });
}

// Call the SearchFunctionality function when the page is loaded
window.addEventListener("load", SearchFunctionality);