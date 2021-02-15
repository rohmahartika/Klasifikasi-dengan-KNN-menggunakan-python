# Klasifikasi dengan KNN(K-Nearest Neighbors) Menggunakan Python

Studi kasus menggunakan data penyakit jantung yang didapat dari https://archive.ics.uci.edu/ml/datasets/Heart+Disease.

Terdapat beberapa variabel dari data penyakit jantung pada UCI dataset, seperti umur, lokasi nyeri, jenis kelamin, dll. Pada penelitian ini, akan dianalisis tentang klasifikasi penyakit jantung berdasarkan umur pasien.

![Capture1](https://user-images.githubusercontent.com/73114027/107907758-1b0c6f80-6f87-11eb-87d7-3241c90c2032.PNG)

Berdasakan grafik diatas, terlihat bahwa ada lebih banyak pasien yang terserang penyakit jantung. Sebanyak 165 pasien terserang penyakit jantung dan 138 pasien lainnya tidak terserang penyakit jantung. 

![Capture_age](https://user-images.githubusercontent.com/73114027/107909711-658feb00-6f8b-11eb-9372-b6217ef0bfc1.PNG)

Dari grafik diatas, dapat diketahui bahwa pasien yang banyak terserang penyakit jantung terdapat pada rentang usia 40-an dan 50-an. Jika ditampilkan dalam scatter plot sebagai berikut.

![scatterplot](https://user-images.githubusercontent.com/73114027/107909889-d0d9bd00-6f8b-11eb-984e-17eb10d5eb56.PNG)

Selanjutnya menentukan nilai K yang digunakan untuk perhitungan model prediksi KNN dengan melihat grafik berikut.

![Capturek](https://user-images.githubusercontent.com/73114027/107910302-bb18c780-6f8c-11eb-86a4-47b4f6ed081f.PNG)

Pada grafik tersebut ditampilkan percobaan untuk nilai K=1 sampai K=40. Dapat dilihat bahwa kesalahan rata-rata mendekati nol pada K=7 dan K=8, maka diambil K=7 untuk perhitungan kali ini.

Setelah melewati proses perhitungan, didapat nilai akurasi sebagai berikut.

![Captureacc](https://user-images.githubusercontent.com/73114027/107910577-4c883980-6f8d-11eb-8cce-e7cdcd893905.PNG)

Dan kinerja dari model dapat dilihat pada confusion matriks berikut.

![Capturemat](https://user-images.githubusercontent.com/73114027/107910580-4e51fd00-6f8d-11eb-8461-7243a9a161be.PNG)
