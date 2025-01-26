var ga_jelas= ga_jelas();
const shiftValue = 3;
var biar_jelas = dekripsi(ga_jelas, shiftValue);

function showDecrypted() {
    var mau_bolos = $('#inputcodeabsen').val();
    var decrypted = CryptoJS.AES.decrypt(mau_bolos, biar_jelas);
    var decrypted_2 = decrypted.toString(CryptoJS.enc.Utf8);

    $('#inputcodeabsen2').text(mau_bolos);
    $('#decrypted').text(decrypted_2);
}