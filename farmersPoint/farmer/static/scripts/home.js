const timoutFunc = () => {
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
}

const isRegistered = () => {
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");

    setTimeout(timoutFunc, 3000);
}

function initiateDropdown() {
    document.getElementById("myDropdown").classList.toggle("show");
}