function updateStates(listOfPlaces) {
    const selectedCountry = document.getElementById("country").value;
    const states = listOfPlaces[selectedCountry];
    const selectStatesElement = document.getElementById("state");

    selectStatesElement.innerHTML = (states && states.length > 0)
        ? states.map(state => `<option value="${state}">${state}</option>`).join("")
        : `<option value="None">Not Available</option>`
}