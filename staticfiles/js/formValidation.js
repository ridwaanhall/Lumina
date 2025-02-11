document.addEventListener("DOMContentLoaded", function () {
    const termsCheckbox = document.getElementById("termsCheckbox");
    const submitButton = document.getElementById("submitButton");
    const inputCodeAbsen = document.getElementById("inputcodeabsen");
    const inputPertemuan = document.getElementById("inputpertemuan");
    const errorMessage = document.getElementById("errorMessage");
    const successMessage = document.getElementById("successMessage");

    function checkFormValidity() {
        if (inputCodeAbsen.value.trim() !== "" &&
            inputPertemuan.value.trim() !== "" &&
            termsCheckbox.checked) {
            submitButton.disabled = false;
        } else {
            submitButton.disabled = true;
        }
    }

    function showMessage(message, isError = false) {
        if (isError) {
            errorMessage.innerText = message;
            errorMessage.classList.remove("is-hidden");
            successMessage.classList.add("is-hidden");
        } else {
            successMessage.innerText = message;
            successMessage.classList.remove("is-hidden");
            errorMessage.classList.add("is-hidden");
        }
    }

    function clearMessages() {
        errorMessage.classList.add("is-hidden");
        successMessage.classList.add("is-hidden");
    }

    inputCodeAbsen.addEventListener("input", checkFormValidity);
    inputPertemuan.addEventListener("input", checkFormValidity);
    termsCheckbox.addEventListener("change", checkFormValidity);

    checkFormValidity();
});