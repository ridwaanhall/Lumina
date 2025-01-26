var ga_jelas= ga_jelas();
const shiftValue = 3;
var biar_jelas = dekripsi(ga_jelas, shiftValue);

function showDecrypted() {
    var mau_bolos = document.getElementById('inputcodeabsen').value;
    try {
        var decrypted = CryptoJS.AES.decrypt(mau_bolos, biar_jelas);
        var decrypted_2 = decrypted.toString(CryptoJS.enc.Utf8);

        document.getElementById('inputcodeabsen2').value = decrypted_2; // Hanya memperbarui nilai input text
    } catch (e) {
        document.getElementById('inputcodeabsen2').value = "Gagal mendekripsi. Pastikan kode benar."; // Mengisi input text dengan pesan error
    }
}