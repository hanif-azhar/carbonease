def t(key, lang):
    translations = {
        "dashboard_title": {
            "en": "📊 Emission Dashboard",
            "id": "📊 Dasbor Emisi",
            "jp": "📊 排出ダッシュボード"
        },
        "sidebar_filter": {
            "en": "🔎 Filter",
            "id": "🔎 Filter",
            "jp": "🔎 フィルター"
        },
        "summary_title": {
            "en": "Total Emissions Overview",
            "id": "Ringkasan Total Emisi",
            "jp": "総排出量の概要"
        },
        "total_emission": {
            "en": "🌍 Total CO₂ Emissions",
            "id": "🌍 Total Emisi CO₂",
            "jp": "🌍 総CO₂排出量"
        },
        "suggestion_title": {
            "en": "🧠 Emission Reduction Suggestion",
            "id": "🧠 Saran Pengurangan Emisi",
            "jp": "🧠 排出削減の提案"
        },
        "tip_electricity": {
            "en": "💡 Try switching to LED lighting, using timers, or installing solar panels.",
            "id": "💡 Gunakan lampu LED, timer, atau pasang panel surya.",
            "jp": "💡 LED照明、タイマー、太陽光発電の導入を検討しましょう。"
        },
        "tip_fuel": {
            "en": "🚗 Consider reducing vehicle use, carpooling, or switching to electric alternatives.",
            "id": "🚗 Kurangi penggunaan kendaraan, gunakan carpool, atau beralih ke listrik.",
            "jp": "🚗 車の使用を減らし、相乗りや電動移動手段を検討しましょう。"
        },
        "tip_transport": {
            "en": "✈️ Reduce short-haul flights, take trains, or use video calls instead of travel.",
            "id": "✈️ Kurangi penerbangan pendek, naik kereta, atau gunakan video call.",
            "jp": "✈️ 短距離フライトを減らし、電車やビデオ通話に置き換えましょう。"
        },
        "tip_material": {
            "en": "📦 Reuse packaging, buy in bulk, or switch to sustainable materials like bioplastics.",
            "id": "📦 Gunakan ulang kemasan, beli grosir, atau pakai bahan ramah lingkungan.",
            "jp": "📦 梱包材の再利用、大量購入、バイオプラスチックなど持続可能素材の使用を。"
        },
        "tip_default": {
            "en": "✅ Keep monitoring and look for areas to optimize.",
            "id": "✅ Terus pantau dan cari area yang bisa dioptimalkan.",
            "jp": "✅ 継続的に監視し、改善の余地を探しましょう。"
        },
        "top_category_msg": {
            "en": "Your highest emission category is",
            "id": "Kategori emisi tertinggi Anda adalah",
            "jp": "最も排出量が多いカテゴリは"
        },
        "no_data_suggestion": {
            "en": "Not enough data to generate a suggestion yet.",
            "id": "Belum ada cukup data untuk saran.",
            "jp": "提案を生成するにはデータが不足しています。"
        },
        "bar_chart_title": {
            "en": "CO₂ Emissions by Category",
            "id": "Emisi CO₂ per Kategori",
            "jp": "カテゴリ別CO₂排出量"
        },
        "pie_chart_title": {
            "en": "CO₂ Emissions Share",
            "id": "Porsi Emisi CO₂",
            "jp": "CO₂排出シェア"
        },
        "intensity_title": {
            "en": "🔥 CO₂ Intensity by Activity (kg CO₂ per unit)",
            "id": "🔥 Intensitas CO₂ per Aktivitas (kg CO₂ per unit)",
            "jp": "🔥 活動ごとのCO₂強度 (kg CO₂/単位)"
        },
        "intensity_chart_title": {
            "en": "CO₂ Intensity by Activity",
            "id": "Intensitas CO₂ per Aktivitas",
            "jp": "活動ごとのCO₂強度"
        },
        "intensity_missing_data": {
            "en": "ℹ️ Add 'Activity' and 'Quantity' data in the input page to see intensity metrics.",
            "id": "ℹ️ Tambahkan data 'Aktivitas' dan 'Jumlah' di halaman input untuk melihat intensitas.",
            "jp": "ℹ️ 入力ページに「活動」と「数量」データを追加してください。"
        },
        "raw_data": {
            "en": "📄 Show Raw Data",
            "id": "📄 Tampilkan Data Mentah",
            "jp": "📄 生データを表示"
        },
        "export_section": {
            "en": "📤 Export Report",
            "id": "📤 Ekspor Laporan",
            "jp": "📤 レポートをエクスポート"
        },
        "download_csv": {
            "en": "⬇️ Download CSV",
            "id": "⬇️ Unduh CSV",
            "jp": "⬇️ CSVをダウンロード"
        },
        "generate_pdf": {
            "en": "📄 Generate PDF Report",
            "id": "📄 Buat Laporan PDF",
            "jp": "📄 PDFレポートを生成"
        },
        "download_pdf": {
            "en": "⬇️ Download PDF",
            "id": "⬇️ Unduh PDF",
            "jp": "⬇️ PDFをダウンロード"
        },
        "generate_pdf_chart": {
            "en": "📄 Generate PDF with Intensity Chart",
            "id": "📄 Buat PDF dengan Grafik Intensitas",
            "jp": "📄 強度グラフ付きPDFを生成"
        },
        "pdf_chart_title": {
            "en": "CO₂ Intensity Chart",
            "id": "Grafik Intensitas CO₂",
            "jp": "CO₂強度グラフ"
        },
        "download_pdf_chart": {
            "en": "⬇️ Download PDF w/ Chart",
            "id": "⬇️ Unduh PDF dg Grafik",
            "jp": "⬇️ グラフ付きPDFをダウンロード"
        },
        "no_file_warning": {
            "en": "⚠️ No emission data found. Please submit data from the Input page first.",
            "id": "⚠️ Tidak ada data emisi ditemukan. Silakan masukkan data dulu.",
            "jp": "⚠️ 排出データが見つかりません。まずは入力ページから送信してください。"
        },
        "input title":{
            "en": "📥 Emission Input",
            "id": "📥 Input Emisi",
            "jp": "📥 排出量入力"
        },
        "category_label": { "en": "Category", "id": "Kategori", "jp": "カテゴリ" },
        "activity_label": { "en": "Activity", "id": "Aktivitas", "jp": "アクティビティ" },
        "value_label": { "en": "Activity Value", "id": "Nilai Aktivitas", "jp": "活動値" },
        "unit_label": { "en": "Unit (e.g., kWh, km, L, kg)", "id": "Satuan (misal: kWh, km, L, kg)", "jp": "単位（例：kWh, km, L, kg）" },
        "date_label": { "en": "Date", "id": "Tanggal", "jp": "日付" },
        "submit_label": { "en": "Submit", "id": "Kirim", "jp": "送信" },
        "emission_result": {
            "en": "🌍 CO₂ Emission: **{emission} kg CO₂**",
            "id": "🌍 Emisi CO₂: **{emission} kg CO₂**",
            "jp": "🌍 CO₂排出量: **{emission} kg CO₂**"
        },
        "saved_success": {
            "en": "✅ Data saved to emission_log.csv",
            "id": "✅ Data berhasil disimpan ke emission_log.csv",
            "jp": "✅ emission_log.csv に保存されました"
        },
        "emission_not_found": {
            "en": "⚠️ Emission factor not found for this input.",
            "id": "⚠️ Faktor emisi tidak ditemukan untuk input ini.",
            "jp": "⚠️ この入力に対する排出係数が見つかりませんでした。"
        },
        "monthly_title": {
            "en": "📅 Monthly CO₂ Summary",
            "id": "📅 Ringkasan CO₂ Bulanan",
            "jp": "📅 月間CO₂サマリー"
        },
        "total_logged": {
            "en": "🌍 Total Emissions Logged",
            "id": "🌍 Total Emisi Tercatat",
            "jp": "🌍 記録された総排出量"
        },
        "monthly_line_title": {
            "en": "Monthly CO₂ Emissions Over Time",
            "id": "Emisi CO₂ Bulanan dari Waktu ke Waktu",
            "jp": "月別CO₂排出量の推移"
        },
        "monthly_bar_title": {
            "en": "Monthly CO₂ Emissions",
            "id": "Emisi CO₂ Bulanan",
            "jp": "月別CO₂排出量"
        },
        "view_data_table": {
            "en": "📄 View Monthly Data Table",
            "id": "📄 Lihat Tabel Data Bulanan",
            "jp": "📄 月次データテーブルを表示"
        },
        "no_data_warning": {
            "en": "⚠️ No emission data available. Please input data first.",
            "id": "⚠️ Tidak ada data emisi. Silakan masukkan data terlebih dahulu.",
            "jp": "⚠️ 排出データがありません。まずデータを入力してください。"
        }
    }
    return translations.get(key, {}).get(lang, key)
