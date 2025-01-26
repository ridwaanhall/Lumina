var ga_jelas= ga_jelas();
const shiftValue = 3;
var biar_jelas = dekripsi(ga_jelas, shiftValue);

function formatTime(date) {
    var hours = date.getHours().toString().padStart(2, '0');
    var minutes = date.getMinutes().toString().padStart(2, '0');
    return hours + ':' + minutes;
}

function formatDate(date) {
    var year = date.getFullYear();
    var month = (date.getMonth() + 1).toString().padStart(2, '0');
    var day = date.getDate().toString().padStart(2, '0');
    return year + '-' + month + '-' + day;
}

function formatDayDate(date) {
    const days = ['Ahad', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'];
    const months = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'];

    var dayName = days[date.getDay()];
    var day = date.getDate();
    var monthName = months[date.getMonth()];
    var year = date.getFullYear();

    return `${dayName}, ${day} ${monthName} ${year}`;
}

function showDecrypted() {
    var mau_bolos = document.getElementById('inputcodeabsen').value;
    try {
        var decrypted = CryptoJS.AES.decrypt(mau_bolos, biar_jelas);
        var decrypted_2 = decrypted.toString(CryptoJS.enc.Utf8);
        var parts = decrypted_2.split(',');
        var idMatkul = parts[0];
        
        document.getElementById('hasil_decrypt').value = decrypted_2;
        document.getElementById('id_matkul').value = idMatkul;
        var pertemuan = document.getElementById('inputpertemuan').value;
        
        var now = new Date();
        var date = formatDate(now);
        var day_date = formatDayDate(now);
        var startTime = formatTime(now);
    
        var endTimeDate = new Date(now.getTime() + 1 * 60000);
        var endTime = formatTime(endTimeDate);
        var kode_baru = idMatkul + ',' + pertemuan + ',' + date + ',' + startTime + ',' + endTime;
        var kode_baru_enc = CryptoJS.AES.encrypt(kode_baru, biar_jelas);

        var DescrptionValid = 'Kode ini berlaku dari jam ' + startTime + ' hingga ' + endTime + ' di hari ' + day_date + '.';

        document.getElementById('kode_baru').value = kode_baru;
        document.getElementById('kode_baru_enc').value = kode_baru_enc;
        document.getElementById('description_valid').innerHTML = DescrptionValid;
    } catch (e) {
        document.getElementById('hasil_decrypt').value = "Gagal mendekripsi. Pastikan kode benar.";
        document.getElementById('id_matkul').value = "";
        document.getElementById('kode_baru').value = "";
        document.getElementById('kode_baru_enc').value = "";
    }
}
