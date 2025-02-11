function copyCode() {
    const copyButton = document.getElementById("copyButton");
    const code = document.getElementById("kode_baru_enc").value;

    navigator.clipboard.writeText(code).then(() => {
        copyButton.innerText = "Disalin!";
        copyButton.classList.remove('is-link');
        copyButton.classList.add('is-success');

        setTimeout(() => {
            copyButton.innerText = "Salin";
            copyButton.classList.remove('is-success');
            copyButton.classList.add('is-link');
        }, 3000);
    }).catch(err => {
        console.error('Tidak bisa mengcopy teks: ', err);
    });
}

document.getElementById("copyButton").addEventListener("click", copyCode);