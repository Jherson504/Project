const filtersLink = document.getElementById("filters-link")
const filtersDropdownMenu = document.querySelector(".home--body__header__nav>.menu>.dropdown-menu")


document.addEventListener("mouseover", e => {
   
    dropdownToggleActive(e.target)
    
})



let currentDropdown
function dropdownToggleActive(dropdown) {
    
    if (dropdown.matches("#filters-link") || dropdown.closest(".dropdown-menu") != null) {
        currentDropdown = dropdown.closest(".dropdown-menu")
        currentDropdown.classList.toggle("active", true)
        currentDropdown.querySelector(".dropdown-content").setAttribute("style", "pointer-events: all;")
        return
    }
    if (currentDropdown != null) {
        currentDropdown.querySelector(".dropdown-content").setAttribute("style", "pointer-events: none;")
    }

    filtersDropdownMenu.classList.toggle("active", false)

}
