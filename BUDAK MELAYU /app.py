import streamlit as st

st.title("📌 Sistem Perhitungan Panen Udang")

# --- INPUT DATA ---
st.header("Input Data Produksi")

jumlah_benur = st.number_input("Jumlah Benur (ekor)", min_value=1, step=1)
pakan_total = st.number_input("Total Pakan (kg)", min_value=0.0, step=0.1)
size_target = st.number_input("Size Target (contoh: 40 = 40 ekor/kg)", min_value=1, step=1)

harga_jual = st.number_input("Harga Jual per kg (Rp)", min_value=0, step=1000)
harga_modal = st.number_input("Harga Modal Produksi per kg (Rp)", min_value=0, step=1000)

st.write("---")

# --- PERHITUNGAN ---
if st.button("Hitung Hasil Panen"):
    # 1. Estimasi SR (Survival Rate) standar
    sr = 0.80  # bisa diubah sesuai kondisi
    
    # 2. Estimasi jumlah udang hidup
    udang_hidup = jumlah_benur * sr

    # 3. Perhitungan berat total panen berdasarkan size
    berat_total_kg = udang_hidup / size_target

    # 4. Pendapatan dan modal
    total_pendapatan = berat_total_kg * harga_jual
    total_modal = berat_total_kg * harga_modal
    laba_bersih = total_pendapatan - total_modal

    # --- OUTPUT ---
    st.header("📊 Hasil Perhitungan")
    st.write(f"**Estimasi Survival Rate (SR):** {sr*100:.0f}%")
    st.write(f"**Udang Hidup:** {udang_hidup:,.0f} ekor")
    st.write(f"**Total Berat Panen:** {berat_total_kg:,.2f} kg")
    st.write(f"**Total Pendapatan:** Rp {total_pendapatan:,.0f}")
    st.write(f"**Total Modal:** Rp {total_modal:,.0f}")
    st.write(f"### 💰 Laba Bersih: Rp {laba_bersih:,.0f}")

    if laba_bersih > 0:
        st.success("Usaha Menguntungkan ✔️")
    else:
        st.error("Usaha Merugi ❌")

st.write("---")
st.caption("Dibuat untuk perhitungan panen udang – Streamlit & Python")
