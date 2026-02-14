import streamlit as st
import random
import time

st.set_page_config(
    page_title="EcoSphere AI",
    page_icon="🌍",
    layout="wide"
)

# ---------- HEADER ----------
st.markdown(
    "<h1 style='text-align: center;'>🌱 EcoSphere AI</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'>Environmental Intelligence Dashboard</p>",
    unsafe_allow_html=True
)

st.divider()

# ---------- FAKE DATA ----------
air_aqi = random.randint(50, 200)
soil_moisture = random.randint(20, 80)
solar_power = round(random.uniform(1, 6), 2)
energy_used = round(random.uniform(3, 7), 2)

# ---------- METRICS ----------
col1, col2, col3, col4 = st.columns(4)

col1.metric("🌫 Air Quality (AQI)", air_aqi)
col2.metric("🌱 Soil Moisture (%)", soil_moisture)
col3.metric("☀ Solar Power (kW)", solar_power)
col4.metric("⚡ Energy Used (kW)", energy_used)

st.divider()

# ---------- INSIGHTS ----------
st.subheader("🔍 System Insights")

if air_aqi > 150:
    st.error("⚠ High pollution detected. Recommend traffic control or alerts.")
else:
    st.success("✅ Air quality is within acceptable limits.")

if soil_moisture < 35:
    st.warning("💧 Soil moisture low. Irrigation recommended.")
else:
    st.success("🌾 Soil moisture is optimal.")

if solar_power < energy_used:
    st.info("🔌 Solar generation insufficient. Grid usage increased.")
else:
    st.success("🔋 Solar generation sufficient.")

st.divider()

# ---------- IMPACT ----------
st.subheader("📊 Sustainability Impact (Estimated)")

water_saved = random.randint(500, 1500)
energy_saved = round(random.uniform(1, 5), 2)
carbon_saved = round(energy_saved * 0.82, 2)

st.write(f"💧 **Water Saved:** {water_saved} liters")
st.write(f"⚡ **Energy Optimized:** {energy_saved} kWh")
st.write(f"♻ **Carbon Reduced:** {carbon_saved} kg CO₂")

st.divider()

# ---------- FOOTER ----------
st.markdown(
    "<p style='text-align: center; color: gray;'>Prototype built for 24-hour EcoTech Hackathon</p>",
    unsafe_allow_html=True
)
