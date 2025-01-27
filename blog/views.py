from django.shortcuts import render, get_object_or_404
from django.views import View
from django.utils.text import slugify

class BlogListView(View):
    def get(self, request):
        blogs = [
            {
                "title": "Sering Ketinggalan Presensi UTY? Santai, Ada Solusinya!",
                "thumbnail": "/static/img/lupa-presensi.webp",
                "date": "Senin, 27 Januari 2025",
                "category": "Tips & Trick",
                "username": "ridwaanhall",
                "name": "Ridwan Halim",
                "intro": "Lupa presensi kuliah? Tenang, website ini siap membantu kamu dengan fitur generator kode presensi otomatis yang mudah digunakan!",
                "content": """
                    <p>Siapa sih yang nggak pernah lupa presensi kuliah? Tenang aja, kamu nggak sendirian kok! Website ini hadir sebagai penyelamat buat kamu, mahasiswa Universitas Teknologi Yogyakarta (UTY), yang seringkali kejebak lupa presensi. Kami ngerti banget deh, betapa pentingnya presensi buat perkuliahan dan pastinya nggak mau ada masalah kan gara-gara ini? Nah, website ini solusinya, dirancang khusus biar kamu bisa atasi masalah ini dengan gampang, cepat, dan nggak ribet!</p>
                    <p>Website ini punya fitur andalan, yaitu generator kode presensi otomatis! Jadi, nggak perlu lagi panik kalau lupa presensi. Caranya gampang banget: *copy-paste* aja kode presensi lama kamu yang dienkripsi ke kolom yang udah disediain, terus masukin nomor pertemuan. Tinggal klik tombol "Buat Presensi Baru" dan website ini langsung memproses kodenya. Nggak pake lama, kamu langsung dapat kode presensi baru yang dienkripsi dan siap pakai! Simple banget, kan?</p>
                    <p>Kami sadar banget, yang namanya teknologi itu harusnya bikin hidup lebih mudah, bukan malah bikin pusing. Makanya, website ini didesain dengan tampilan yang simpel, bersih, dan gampang banget dimengerti. Jadi, kamu nggak perlu khawatir kalau nggak terlalu jago soal teknologi. Prosesnya juga mudah banget, nggak perlu ribet, cukup beberapa langkah, dan kode presensi kamu langsung beres. Waktu kamu pun jadi lebih efektif buat hal-hal yang lebih penting.</p>
                    <p>Keunggulan website ini jelas banget, yaitu bisa kasih solusi instan kalau kamu lupa presensi. Dengan generator kode presensi otomatis, kamu bisa hindari masalah atau sanksi yang nggak diinginkan karena telat atau lupa presensi. Selain itu, website ini juga bisa diakses kapanpun dan di manapun, mau lewat laptop atau HP, tetap bisa! Proses enkripsinya juga aman banget, jadi kamu bisa pakai kodenya tanpa khawatir.</p>
                    <p>Mungkin ada sedikit kendala teknis, terutama kalau kamu pakai *adblocker* atau ekstensi browser lainnya. Jadi, buat sementara, *adblocker*-nya dimatiin dulu ya biar website-nya bisa berfungsi dengan lancar. Kami juga terus berusaha buat ningkatin kualitas dan performa website ini biar selalu kasih yang terbaik buat kamu. Kalau ada pertanyaan atau butuh bantuan, jangan sungkan buat hubungi kami ya! Semoga dengan website ini, masalah lupa presensi bisa lebih mudah teratasi, ya!</p>
                """
            },
            {
                "title": "Tips Mengatasi Lupa Presensi di UTY",
                "thumbnail": "/static/img/tips-presensi.webp",
                "date": "Senin, 27 Januari 2025",
                "category": "Tips",
                "username": "ridwaanhall",
                "name": "Ridwan Halim",
                "intro": "Lupa presensi di UTY? Jangan panik! Ikuti tips sederhana ini untuk memastikan kamu tidak lagi ketinggalan presensi.",
                "content": """
                    <p>Lupa presensi memang sering terjadi, apalagi jika kamu memiliki jadwal kuliah yang padat. Tetapi, ada beberapa tips yang bisa kamu lakukan untuk mengatasi lupa presensi di UTY:</p>
                    <ol>
                        <li><strong>Pasang Alarm Pengingat:</strong> Set alarm di handphone kamu beberapa menit sebelum jam kuliah dimulai. Ini akan membantu kamu untuk tidak lupa melakukan presensi.</li>
                        <li><strong>Gunakan Aplikasi Pengingat:</strong> Ada berbagai aplikasi pengingat yang bisa kamu gunakan untuk mengingatkan kamu tentang jadwal kuliah dan presensi.</li>
                        <li><strong>Buat Catatan:</strong> Buat catatan atau kalender yang berisi jadwal kuliah dan presensi. Letakkan di tempat yang mudah kamu lihat setiap hari.</li>
                        <li><strong>Ajak Teman:</strong> Ajak teman untuk saling mengingatkan tentang presensi. Jika ada yang lupa, temanmu akan segera mengingatkanmu.</li>
                        <li><strong>Manfaatkan Generator Presensi Otomatis:</strong> Jika kamu sudah terlanjur lupa, kamu bisa menggunakan generator presensi otomatis di website ini untuk mengatasi masalahmu.</li>
                    </ol>
                    <p>Dengan menerapkan tips ini, diharapkan kamu tidak lagi mengalami masalah lupa presensi di UTY.</p>
                """
            },
            {
                "title": "Cara Menggunakan Generator Presensi Otomatis UTY",
                "thumbnail": "/static/img/cara-presensi.webp",
                "date": "Senin, 27 Januari 2025",
                "category": "Tutorial, Tips Kuliah, Teknologi Kampus",
                "username": "ridwaanhall",
                "name": "Ridwan Halim",
                "intro": "Lupa presensi UTY? Kami punya solusinya: Generator Presensi Otomatis. Ikuti panduannya di artikel ini.",
                "content": """
                    <p>Generator presensi otomatis ini adalah fitur andalan kami yang dirancang untuk membantu mahasiswa UTY mengatasi masalah lupa presensi. Dengan fitur ini, kamu bisa menghasilkan kode presensi baru secara otomatis, berdasarkan kode presensi lama yang kamu miliki. Yuk, simak panduan lengkapnya:</p>
                    
                    <h2>Langkah 1: Akses Generator Presensi</h2>
                    <p>Pertama-tama, buka halaman generator presensi otomatis di website kami. Kamu akan melihat tampilan yang sederhana dan mudah dipahami.</p>
                    <p><em>(Catatan: Saya akan menyarankan untuk memasukkan gambar screenshot tampilan generator presensi Anda di sini. Jika Anda tidak memiliki gambar, deskripsikan secara detail apa yang terlihat di halaman tersebut.)</em></p>
                    
                    <h2>Langkah 2: Masukkan Kode Presensi Lama</h2>
                    <p>Di bagian "Kode Presensi Lama", terdapat kolom input yang bertuliskan "Paste kode absenmu disini". Masukkan kode presensi lama yang kamu peroleh dari dosen atau sistem presensi. Pastikan kode yang kamu masukkan benar, ya!</p>
                    <p><em>(Catatan: Saya akan menyarankan untuk memasukkan gambar screenshot input kode presensi lama.)</em></p>
                    
                    <h2>Langkah 3: Masukkan Pertemuan Ke-</h2>
                    <p>Selanjutnya, pada kolom input di bawahnya, masukkan "Pertemuan ke-" yang ingin kamu presensikan. Misalnya, jika kamu ingin melakukan presensi untuk pertemuan ke-3, maka ketikkan angka 3 di kolom tersebut.</p>
                    <p><em>(Catatan: Saya akan menyarankan untuk memasukkan gambar screenshot input pertemuan ke-)</em></p>
                    
                    <h2>Langkah 4: Generate Kode Presensi Baru</h2>
                    <p>Setelah memasukkan kode presensi lama dan pertemuan ke-, klik tombol "Buat Presensi Baru". Sistem kami akan bekerja untuk mengolah data dan menghasilkan kode presensi baru yang unik untukmu.</p>
                    <p><em>(Catatan: Saya akan menyarankan untuk memasukkan gambar screenshot tombol "Buat Presensi Baru")</em></p>
                    
                    <h2>Langkah 5: Salin Kode Presensi Baru</h2>
                    <p>Kode presensi baru akan muncul di kolom input yang bertuliskan "Presensi Baru". Kamu bisa menyalin kode tersebut dengan mengklik tombol "Salin" yang ada di sebelahnya. Kode tersebut bisa kamu gunakan untuk melakukan presensi.</p>
                    <p><em>(Catatan: Saya akan menyarankan untuk memasukkan gambar screenshot kode presensi baru dan tombol "Salin")</em></p>
                    <p>Setelah tombol Salin di klik, maka tombol tersebut akan berubah tulisan menjadi "Disalin" selama beberapa detik. Setelah itu, tombol akan berubah kembali menjadi tulisan "Salin"</p>
                    
                    <h2>Langkah 6: Generate QR Code (Opsional)</h2>
                    <p>Jika kamu ingin melakukan presensi menggunakan QR code, kamu bisa mengklik tombol "QR Code" yang ada di sebelahnya. Sistem akan menghasilkan QR Code yang bisa kamu scan menggunakan aplikasi presensi di kampus.</p>
                    <p><em>(Catatan: Saya akan menyarankan untuk memasukkan gambar screenshot tombol "QR Code" serta contoh tampilan QR code)</em></p>
                    
                    <h2>Penting: Nonaktifkan AdBlock Jika Mengalami Masalah</h2>
                    <p>Beberapa pengguna mungkin mengalami masalah saat menggunakan generator presensi ini karena adanya AdBlock di browser mereka. Jika kamu mengalami masalah, coba nonaktifkan AdBlock terlebih dahulu, lalu refresh halaman generator presensi. </p>
                    <div class="notification is-danger">
                        <p><strong>Penting!</strong> Jika presensi tidak berfungsi, pastikan AdBlock kamu nonaktif terlebih dahulu.</p>
                    </div>
                    
                    <h2>Tips dan Trik Tambahan</h2>
                    <ul>
                        <li>Pastikan kamu memasukkan kode presensi lama dengan benar agar sistem bisa menghasilkan kode baru yang valid.</li>
                        <li>Periksa kembali pertemuan ke- yang kamu masukkan agar sesuai dengan jadwal kuliahmu.</li>
                        <li>Jika kamu mengalami masalah atau pertanyaan, jangan ragu untuk menghubungi tim support kami.</li>
                    </ul>
                    
                    <h2>Call to Action</h2>
                    <p>Tunggu apa lagi? Gunakan generator presensi otomatis UTY sekarang juga dan nikmati kemudahan anti ribet presensi! Kunjungi halaman <a href="https://absen-uty.vercel.app/">generator presensi</a> dan mulai sekarang!</p>
                """
            },
        ]
        context = {
            'blogs': blogs
        }
        return render(request, 'blog/blog.html', context)

class BlogDetailView(View):
    def get(self, request, title):
        blogs = [
            {
                "title": "Sering Ketinggalan Presensi UTY? Santai, Ada Solusinya!",
                "thumbnail": "/static/img/lupa-presensi.webp",
                "date": "Senin, 27 Januari 2025",
                "category": "Tips & Trick",
                "username": "ridwaanhall",
                "name": "Ridwan Halim",
                "intro": "Lupa presensi kuliah? Tenang, website ini siap membantu kamu dengan fitur generator kode presensi otomatis yang mudah digunakan!",
                "content": """
                    <p>Siapa sih yang nggak pernah lupa presensi kuliah? Tenang aja, kamu nggak sendirian kok! Website ini hadir sebagai penyelamat buat kamu, mahasiswa Universitas Teknologi Yogyakarta (UTY), yang seringkali kejebak lupa presensi. Kami ngerti banget deh, betapa pentingnya presensi buat perkuliahan dan pastinya nggak mau ada masalah kan gara-gara ini? Nah, website ini solusinya, dirancang khusus biar kamu bisa atasi masalah ini dengan gampang, cepat, dan nggak ribet!</p>
                    <p>Website ini punya fitur andalan, yaitu generator kode presensi otomatis! Jadi, nggak perlu lagi panik kalau lupa presensi. Caranya gampang banget: *copy-paste* aja kode presensi lama kamu yang dienkripsi ke kolom yang udah disediain, terus masukin nomor pertemuan. Tinggal klik tombol "Buat Presensi Baru" dan website ini langsung memproses kodenya. Nggak pake lama, kamu langsung dapat kode presensi baru yang dienkripsi dan siap pakai! Simple banget, kan?</p>
                    <p>Kami sadar banget, yang namanya teknologi itu harusnya bikin hidup lebih mudah, bukan malah bikin pusing. Makanya, website ini didesain dengan tampilan yang simpel, bersih, dan gampang banget dimengerti. Jadi, kamu nggak perlu khawatir kalau nggak terlalu jago soal teknologi. Prosesnya juga mudah banget, nggak perlu ribet, cukup beberapa langkah, dan kode presensi kamu langsung beres. Waktu kamu pun jadi lebih efektif buat hal-hal yang lebih penting.</p>
                    <p>Keunggulan website ini jelas banget, yaitu bisa kasih solusi instan kalau kamu lupa presensi. Dengan generator kode presensi otomatis, kamu bisa hindari masalah atau sanksi yang nggak diinginkan karena telat atau lupa presensi. Selain itu, website ini juga bisa diakses kapanpun dan di manapun, mau lewat laptop atau HP, tetap bisa! Proses enkripsinya juga aman banget, jadi kamu bisa pakai kodenya tanpa khawatir.</p>
                    <p>Mungkin ada sedikit kendala teknis, terutama kalau kamu pakai *adblocker* atau ekstensi browser lainnya. Jadi, buat sementara, *adblocker*-nya dimatiin dulu ya biar website-nya bisa berfungsi dengan lancar. Kami juga terus berusaha buat ningkatin kualitas dan performa website ini biar selalu kasih yang terbaik buat kamu. Kalau ada pertanyaan atau butuh bantuan, jangan sungkan buat hubungi kami ya! Semoga dengan website ini, masalah lupa presensi bisa lebih mudah teratasi, ya!</p>
                """
            },
            {
                "title": "Tips Mengatasi Lupa Presensi di UTY",
                "thumbnail": "/static/img/tips-presensi.webp",
                "date": "Senin, 27 Januari 2025",
                "category": "Tips",
                "username": "ridwaanhall",
                "name": "Ridwan Halim",
                "intro": "Lupa presensi di UTY? Jangan panik! Ikuti tips sederhana ini untuk memastikan kamu tidak lagi ketinggalan presensi.",
                "content": """
                    <p>Lupa presensi memang sering terjadi, apalagi jika kamu memiliki jadwal kuliah yang padat. Tetapi, ada beberapa tips yang bisa kamu lakukan untuk mengatasi lupa presensi di UTY:</p>
                    <ol>
                        <li><strong>Pasang Alarm Pengingat:</strong> Set alarm di handphone kamu beberapa menit sebelum jam kuliah dimulai. Ini akan membantu kamu untuk tidak lupa melakukan presensi.</li>
                        <li><strong>Gunakan Aplikasi Pengingat:</strong> Ada berbagai aplikasi pengingat yang bisa kamu gunakan untuk mengingatkan kamu tentang jadwal kuliah dan presensi.</li>
                        <li><strong>Buat Catatan:</strong> Buat catatan atau kalender yang berisi jadwal kuliah dan presensi. Letakkan di tempat yang mudah kamu lihat setiap hari.</li>
                        <li><strong>Ajak Teman:</strong> Ajak teman untuk saling mengingatkan tentang presensi. Jika ada yang lupa, temanmu akan segera mengingatkanmu.</li>
                        <li><strong>Manfaatkan Generator Presensi Otomatis:</strong> Jika kamu sudah terlanjur lupa, kamu bisa menggunakan generator presensi otomatis di website ini untuk mengatasi masalahmu.</li>
                    </ol>
                    <p>Dengan menerapkan tips ini, diharapkan kamu tidak lagi mengalami masalah lupa presensi di UTY.</p>
                """
            },
            {
                "title": "Cara Menggunakan Generator Presensi Otomatis UTY",
                "thumbnail": "/static/img/cara-presensi.webp",
                "date": "Senin, 27 Januari 2025",
                "category": "Tutorial, Tips Kuliah, Teknologi Kampus",
                "username": "ridwaanhall",
                "name": "Ridwan Halim",
                "intro": "Terburu-buru dan lupa presensi? Tenang! Generator Presensi Otomatis UTY siap membantu. Pelajari cara pakainya dalam panduan singkat ini!",
                "content": """
                    <p>Lupa presensi UTY? Kami punya solusinya: Generator Presensi Otomatis. Ikuti panduannya di artikel ini.</p>
                    <p>Generator presensi otomatis ini adalah fitur andalan kami yang dirancang untuk membantu mahasiswa UTY mengatasi masalah lupa presensi. Dengan fitur ini, kamu bisa menghasilkan kode presensi baru secara otomatis, berdasarkan kode presensi lama yang kamu miliki. Yuk, simak panduan lengkapnya:</p>
                    <h2>Langkah 1: Akses Generator Presensi</h2>
                    <p>Pertama-tama, buka halaman generator presensi otomatis di website kami. Kamu akan melihat tampilan yang sederhana dan mudah dipahami.</p>
                    
                    <h2>Langkah 2: Masukkan Kode Presensi Lama</h2>
                    <p>Di bagian "Kode Presensi Lama", terdapat kolom input yang bertuliskan "Paste kode absenmu disini". Masukkan kode presensi lama yang kamu peroleh dari dosen atau sistem presensi. Pastikan kode yang kamu masukkan benar, ya!</p>
                    
                    <h2>Langkah 3: Masukkan Pertemuan Ke-</h2>
                    <p>Selanjutnya, pada kolom input di bawahnya, masukkan "Pertemuan ke-" yang ingin kamu presensikan. Misalnya, jika kamu ingin melakukan presensi untuk pertemuan ke-3, maka ketikkan angka 3 di kolom tersebut.</p>
                    
                    <h2>Langkah 4: Generate Kode Presensi Baru</h2>
                    <p>Setelah memasukkan kode presensi lama dan pertemuan ke-, klik tombol "Buat Presensi Baru". Sistem kami akan bekerja untuk mengolah data dan menghasilkan kode presensi baru yang unik untukmu.</p>
                    
                    <h2>Langkah 5: Salin Kode Presensi Baru</h2>
                    <p>Kode presensi baru akan muncul di kolom input yang bertuliskan "Presensi Baru". Kamu bisa menyalin kode tersebut dengan mengklik tombol "Salin" yang ada di sebelahnya. Kode tersebut bisa kamu gunakan untuk melakukan presensi.</p>
                    <p>Setelah tombol Salin di klik, maka tombol tersebut akan berubah tulisan menjadi "Disalin" selama beberapa detik. Setelah itu, tombol akan berubah kembali menjadi tulisan "Salin"</p>
                    
                    <h2>Langkah 6: Generate QR Code (Opsional)</h2>
                    <p>Jika kamu ingin melakukan presensi menggunakan QR code, kamu bisa mengklik tombol "QR Code" yang ada di sebelahnya. Sistem akan menghasilkan QR Code yang bisa kamu scan menggunakan aplikasi presensi di kampus.</p>
                    
                    <h2>Penting: Nonaktifkan AdBlock Jika Mengalami Masalah</h2>
                    <p>Beberapa pengguna mungkin mengalami masalah saat menggunakan generator presensi ini karena adanya AdBlock di browser mereka. Jika kamu mengalami masalah, coba nonaktifkan AdBlock terlebih dahulu, lalu refresh halaman generator presensi. </p>
                    <div class="notification is-danger">
                        <p><strong>Penting!</strong> Jika presensi tidak berfungsi, pastikan AdBlock kamu nonaktif terlebih dahulu.</p>
                    </div>
                    
                    <h2>Tips dan Trik Tambahan</h2>
                    <ul>
                        <li>Pastikan kamu memasukkan kode presensi lama dengan benar agar sistem bisa menghasilkan kode baru yang valid.</li>
                        <li>Periksa kembali pertemuan ke- yang kamu masukkan agar sesuai dengan jadwal kuliahmu.</li>
                        <li>Jika kamu mengalami masalah atau pertanyaan, jangan ragu untuk menghubungi tim support kami.</li>
                    </ul>
                    
                    <h2>Call to Action</h2>
                    <p>Tunggu apa lagi? Gunakan generator presensi otomatis UTY sekarang juga dan nikmati kemudahan anti ribet presensi! Kunjungi halaman <a href="https://absen-uty.vercel.app/">generator presensi</a> dan mulai sekarang!</p>
                """
            },
        ]
        blog_post = next((item for item in blogs if slugify(item['title']) == title), None)
        if blog_post:
            context = {'blog' : blog_post}
            return render(request, 'blog/blog_detail.html', context)
        else:
          return render(request, 'blog/blog_not_found.html', status=404)