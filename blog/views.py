from django.shortcuts import render, get_object_or_404
from django.views import View
from django.utils.text import slugify

class BlogListView(View):
    def get(self, request):
        blogs = [
             {
                'title': 'Sering Ketinggalan Absen UTY? Santai, Ada Solusinya!',
                 'thumbnail': '/static/img/lupa-absen.webp', # Contoh path thumbnail
                'date': '2025-01-27',
                'category': 'Tips & Trick',
                'author' : 'ridwaanhall',
                'content': """
                    <p>Siapa sih yang nggak pernah lupa absen kuliah? Tenang aja, kamu nggak sendirian kok! Website ini hadir sebagai penyelamat buat kamu, mahasiswa Universitas Teknologi Yogyakarta (UTY), yang seringkali kejebak lupa absen. Kami ngerti banget deh, betapa pentingnya absen buat perkuliahan dan pastinya nggak mau ada masalah kan gara-gara ini? Nah, website ini solusinya, dirancang khusus biar kamu bisa atasi masalah ini dengan gampang, cepat, dan nggak ribet!</p>
                    <p>Website ini punya fitur andalan, yaitu generator kode absen otomatis! Jadi, nggak perlu lagi panik kalau lupa absen. Caranya gampang banget: *copy-paste* aja kode absen lama kamu yang dienkripsi ke kolom yang udah disediain, terus masukin nomor pertemuan. Tinggal klik tombol "Cek Decrypted," dan website ini langsung memproses kodenya. Nggak pake lama, kamu langsung dapat kode absen baru yang dienkripsi dan siap pakai! Simple banget, kan?</p>
                    <p>Kami sadar banget, yang namanya teknologi itu harusnya bikin hidup lebih mudah, bukan malah bikin pusing. Makanya, website ini didesain dengan tampilan yang simpel, bersih, dan gampang banget dimengerti. Jadi, kamu nggak perlu khawatir kalau nggak terlalu jago soal teknologi. Prosesnya juga mudah banget, nggak perlu ribet, cukup beberapa langkah, dan kode absen kamu langsung beres. Waktu kamu pun jadi lebih efektif buat hal-hal yang lebih penting.</p>
                    <p>Keunggulan website ini jelas banget, yaitu bisa kasih solusi instan kalau kamu lupa absen. Dengan generator kode absen otomatis, kamu bisa hindari masalah atau sanksi yang nggak diinginkan karena telat atau lupa absen. Selain itu, website ini juga bisa diakses kapanpun dan di manapun, mau lewat laptop atau HP, tetap bisa! Proses enkripsinya juga aman banget, jadi kamu bisa pakai kodenya tanpa khawatir.</p>
                    <p>Mungkin ada sedikit kendala teknis, terutama kalau kamu pakai *adblocker* atau ekstensi browser lainnya. Jadi, buat sementara, *adblocker*-nya dimatiin dulu ya biar website-nya bisa berfungsi dengan lancar. Kami juga terus berusaha buat ningkatin kualitas dan performa website ini biar selalu kasih yang terbaik buat kamu. Kalau ada pertanyaan atau butuh bantuan, jangan sungkan buat hubungi kami ya! Semoga dengan website ini, masalah lupa absen bisa lebih mudah teratasi, ya!</p>
                """
             },
               {
                'title': 'Tips Mengatasi Lupa Absen di UTY',
                'thumbnail': '/static/img/lupa-absen.webp', # Contoh path thumbnail
                'date': '2025-01-28',
                'category': 'Tips',
                'author' : 'ridwaanhall',
                'content': """
                    <p>Lupa absen memang sering terjadi, apalagi jika kamu memiliki jadwal kuliah yang padat. Tetapi, ada beberapa tips yang bisa kamu lakukan untuk mengatasi lupa absen di UTY:</p>
                    <ol>
                      <li><strong>Pasang Alarm Pengingat:</strong> Set alarm di handphone kamu beberapa menit sebelum jam kuliah dimulai. Ini akan membantu kamu untuk tidak lupa melakukan absensi.</li>
                      <li><strong>Gunakan Aplikasi Pengingat:</strong> Ada berbagai aplikasi pengingat yang bisa kamu gunakan untuk mengingatkan kamu tentang jadwal kuliah dan absensi.</li>
                      <li><strong>Buat Catatan:</strong> Buat catatan atau kalender yang berisi jadwal kuliah dan absensi. Letakkan di tempat yang mudah kamu lihat setiap hari.</li>
                      <li><strong>Ajak Teman:</strong> Ajak teman untuk saling mengingatkan tentang absensi. Jika ada yang lupa, temanmu akan segera mengingatkanmu.</li>
                      <li><strong>Manfaatkan Generator Absen Otomatis:</strong> Jika kamu sudah terlanjur lupa, kamu bisa menggunakan generator absen otomatis di website ini untuk mengatasi masalahmu.</li>
                    </ol>
                    <p>Dengan menerapkan tips ini, diharapkan kamu tidak lagi mengalami masalah lupa absen di UTY.</p>
                """
             }
        ]
        context = {
            'blogs': blogs
        }
        return render(request, 'blog/blog.html', context)

class BlogDetailView(View):
    def get(self, request, title):
        blogs = [
             {
                'title': 'Sering Ketinggalan Absen UTY? Santai, Ada Solusinya!',
                'thumbnail': '/static/img/lupa-absen.webp', # Contoh path thumbnail
                'date': '2025-01-27',
                'category': 'Tips & Trick',
                'author' : 'ridwaanhall',
                'content': """
                    <p>Siapa sih yang nggak pernah lupa absen kuliah? Tenang aja, kamu nggak sendirian kok! Website ini hadir sebagai penyelamat buat kamu, mahasiswa Universitas Teknologi Yogyakarta (UTY), yang seringkali kejebak lupa absen. Kami ngerti banget deh, betapa pentingnya absen buat perkuliahan dan pastinya nggak mau ada masalah kan gara-gara ini? Nah, website ini solusinya, dirancang khusus biar kamu bisa atasi masalah ini dengan gampang, cepat, dan nggak ribet!</p>
                    <p>Website ini punya fitur andalan, yaitu generator kode absen otomatis! Jadi, nggak perlu lagi panik kalau lupa absen. Caranya gampang banget: *copy-paste* aja kode absen lama kamu yang dienkripsi ke kolom yang udah disediain, terus masukin nomor pertemuan. Tinggal klik tombol "Cek Decrypted," dan website ini langsung memproses kodenya. Nggak pake lama, kamu langsung dapat kode absen baru yang dienkripsi dan siap pakai! Simple banget, kan?</p>
                    <p>Kami sadar banget, yang namanya teknologi itu harusnya bikin hidup lebih mudah, bukan malah bikin pusing. Makanya, website ini didesain dengan tampilan yang simpel, bersih, dan gampang banget dimengerti. Jadi, kamu nggak perlu khawatir kalau nggak terlalu jago soal teknologi. Prosesnya juga mudah banget, nggak perlu ribet, cukup beberapa langkah, dan kode absen kamu langsung beres. Waktu kamu pun jadi lebih efektif buat hal-hal yang lebih penting.</p>
                    <p>Keunggulan website ini jelas banget, yaitu bisa kasih solusi instan kalau kamu lupa absen. Dengan generator kode absen otomatis, kamu bisa hindari masalah atau sanksi yang nggak diinginkan karena telat atau lupa absen. Selain itu, website ini juga bisa diakses kapanpun dan di manapun, mau lewat laptop atau HP, tetap bisa! Proses enkripsinya juga aman banget, jadi kamu bisa pakai kodenya tanpa khawatir.</p>
                    <p>Mungkin ada sedikit kendala teknis, terutama kalau kamu pakai *adblocker* atau ekstensi browser lainnya. Jadi, buat sementara, *adblocker*-nya dimatiin dulu ya biar website-nya bisa berfungsi dengan lancar. Kami juga terus berusaha buat ningkatin kualitas dan performa website ini biar selalu kasih yang terbaik buat kamu. Kalau ada pertanyaan atau butuh bantuan, jangan sungkan buat hubungi kami ya! Semoga dengan website ini, masalah lupa absen bisa lebih mudah teratasi, ya!</p>
                """
             },
               {
                'title': 'Tips Mengatasi Lupa Absen di UTY',
                'thumbnail': '/static/img/lupa-absen.webp', # Contoh path thumbnail
                'date': '2025-01-28',
                'category': 'Tips',
                'author' : 'ridwaanhall',
                'content': """
                    <p>Lupa absen memang sering terjadi, apalagi jika kamu memiliki jadwal kuliah yang padat. Tetapi, ada beberapa tips yang bisa kamu lakukan untuk mengatasi lupa absen di UTY:</p>
                    <ol>
                      <li><strong>Pasang Alarm Pengingat:</strong> Set alarm di handphone kamu beberapa menit sebelum jam kuliah dimulai. Ini akan membantu kamu untuk tidak lupa melakukan absensi.</li>
                      <li><strong>Gunakan Aplikasi Pengingat:</strong> Ada berbagai aplikasi pengingat yang bisa kamu gunakan untuk mengingatkan kamu tentang jadwal kuliah dan absensi.</li>
                      <li><strong>Buat Catatan:</strong> Buat catatan atau kalender yang berisi jadwal kuliah dan absensi. Letakkan di tempat yang mudah kamu lihat setiap hari.</li>
                      <li><strong>Ajak Teman:</strong> Ajak teman untuk saling mengingatkan tentang absensi. Jika ada yang lupa, temanmu akan segera mengingatkanmu.</li>
                      <li><strong>Manfaatkan Generator Absen Otomatis:</strong> Jika kamu sudah terlanjur lupa, kamu bisa menggunakan generator absen otomatis di website ini untuk mengatasi masalahmu.</li>
                    </ol>
                    <p>Dengan menerapkan tips ini, diharapkan kamu tidak lagi mengalami masalah lupa absen di UTY.</p>
                """
             }
        ]
        blog_post = next((item for item in blogs if slugify(item['title']) == title), None)
        if blog_post:
            context = {'blog' : blog_post}
            return render(request, 'blog/blog_detail.html', context)
        else:
          return render(request, 'blog/blog_not_found.html', status=404)