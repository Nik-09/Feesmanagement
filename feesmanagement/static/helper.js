const validationFunctionTriggered = false;

function validateSubjects() {
    var all = document.getElementById("all");
    var science = document.getElementById("science");
    var biology = document.getElementById("biology");
    var chemistry = document.getElementById("chemistry");
    var physics = document.getElementById("physics");
    var math = document.getElementById("math");
    var businesStudies = document.getElementById("busines-studies");
    var accounts = document.getElementById("accounts");
    var economics = document.getElementById("economics");

    secondaryChecked = (
        all.checked || science.checked);
    higherSecondaryScienceChecked = (
        biology.checked || chemistry.checked || physics.checked || math.checked);
    higherSecondaryCommerceChecked = (
            businesStudies.checked || accounts.checked || economics.checked);

    var condition =  (
        (secondaryChecked && higherSecondaryScienceChecked) ||
        (secondaryChecked && higherSecondaryCommerceChecked) ||
        (higherSecondaryScienceChecked && higherSecondaryCommerceChecked)
    )
    if (condition) {
        alert('Please select either from secondary or from higher secondary!');
        all.checked = false;
        science.checked = false;
        biology.checked = false;
        chemistry.checked = false;
        physics.checked = false;
        math.checked = false;
        businesStudies.checked = false;
        accounts.checked = false;
        economics.checked = false;
    }
}