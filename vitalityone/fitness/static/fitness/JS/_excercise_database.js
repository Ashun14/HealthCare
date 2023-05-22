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

const categoryFetch = async (index) => {
  const url = "https://wger.de/api/v2/exercise/";
  const headers = {
    "Authorization": `Token ${config('API_KEY')}`,  // Replace with your API key
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

      console.log(exercises)
      if (index == 0) {
        await fetch(
          "api/v2/exercise/?muscles=1&equipment=3"
        )
          .then((response) => response.json())
          .then((category) => {
            let data = "";
            for (items in category) {
              let catName = capitalize(category[items]);
              data += `
          <div class="option">
            <input type="radio" class="radio" id="${catName}" name="category" />
            <label for="${catName}">${catName}</label>
          </div>
          `;
            }
            dropDownItems.innerHTML += data;
          })
          .catch((err) => console.error(err));
      }

      if (index == 1) {
        await fetch(
          "https://exercisedb.p.rapidapi.com/exercises/targetList",
          options
        )
          .then((response) => response.json())
          .then((category) => {
            let data = "";
            for (items in category) {
              let catName = capitalize(category[items]);
              data += `
            <div class="option">
              <input type="radio" class="radio" id="${catName}" name="category" />
              <label for="${catName}">${catName}</label>
            </div>
            `;
            }
            dropDownItems.innerHTML += data;
          })
          .catch((err) => console.error(err));
      }

      if (index == 2) {
        await fetch(
          "https://exercisedb.p.rapidapi.com/exercises/equipmentList",
          options
        )
          .then((response) => response.json())
          .then((category) => {
            let data = "";
            for (items in category) {
              let catName = capitalize(category[items]);
              data += `
            <div class="option">
              <input type="radio" class="radio" id="${catName}" name="category" />
              <label for="${catName}">${catName}</label>
            </div>
            `;
            }
            dropDownItems.innerHTML += data;
          })
          .catch((err) => console.error(err));
      }

      SearchFunctionality();
    }
  } catch (err) {
    console.error(err);
  }
};

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

    //  Fetching Types based on Categories

    if (cat.classList.contains("bodypart")) {
      categoryFetch(0);
    }
    if (cat.classList.contains("muscles")) {
      categoryFetch(1);
    }
    if (cat.classList.contains("equipments")) {
      categoryFetch(2);
    }

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
    o.addEventListener("click", () => {
      selected.innerHTML = o.querySelector("label").innerHTML;
      optionsContainer.classList.remove("active");
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