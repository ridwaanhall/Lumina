document.addEventListener("DOMContentLoaded", function () {
    const submitButton = document.getElementById("submitButton");
    const inputCodeAbsen = document.getElementById("inputcodeabsen");
    const inputPertemuan = document.getElementById("inputpertemuan");
    const kodeBaruEnc = document.getElementById("kode_baru_enc");
    const secondCard = document.getElementById("secondCard");
    const errorMessage = document.getElementById("errorMessage");
    const successMessage = document.getElementById("successMessage");

    let hideTimeout;
    let isVisible = false;

    function toggleSecondCard() {
        if (!isVisible) {
            secondCard.style.display = "block";
            isVisible = true;

            clearTimeout(hideTimeout);
            hideTimeout = setTimeout(() => {
                secondCard.style.display = "none";
                isVisible = false;
            }, 3000);
        } else {
            clearTimeout(hideTimeout);
            hideTimeout = setTimeout(() => {
                secondCard.style.display = "none";
                isVisible = false;
            }, 3000);
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

    submitButton.addEventListener("click", function () {
        const encryptedMessage = inputCodeAbsen.value.trim();
        const newMeetId = inputPertemuan.value.trim();

        clearMessages();

        if (!encryptedMessage || !newMeetId) {
            showMessage("⚠️ Masukkan kode presensi lama dan nomor pertemuan!", true);
            return;
        }

        fetch(encryptUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({
                "encrypted_message": encryptedMessage,
                "new_meet_id": newMeetId
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                kodeBaruEnc.value = data.data.updated_encrypted_message;
                showMessage("✅ Kode presensi berhasil dibuat!", false);
                toggleSecondCard();
            } else {
                showMessage(`⚠️ ${data.message}`, true);
            }
        })
        .catch(error => {
            showMessage("⚠️ Terjadi kesalahan, coba lagi.", true);
            console.error("Error:", error);
        });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});