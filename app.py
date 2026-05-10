import streamlit as st

# Set page title and layout
st.set_page_config(
    page_title="Mechanical Unit Converter & Density Checker",
    page_icon="⚙️",
    layout="centered"
)

# ==============================================================================
# STUDENT CREDENTIALS HEADER (Required)
# ==============================================================================
st.markdown(
    """
    <div style="background-color:#f0f2f6; padding:20px; border-radius:10px; border-left: 5px solid #ff4b4b; margin-bottom: 25px;">
        <h2 style="margin:0; color:#31333F;">Mechanical Unit Converter & Density Checker</h2>
        <p style="margin:5px 0 0 0; font-size:1.1rem; color:#555;"><b>Developer:</b> Syed Muhammad Aunn</p>
        <p style="margin:2px 0 0 0; font-size:1.1rem; color:#555;"><b>Roll Number:</b> 25-ME-224</p>
    </div>
    """, 
    unsafe_style=True
)

# App description
st.write("Welcome! This engineering tool allows you to convert common mechanical units and check/calculate densities for various engineering materials.")

# Create tabs for clean navigation
tab1, tab2 = st.tabs(["🔄 Unit Converter", "⚖️ Material Density Checker"])

# ==============================================================================
# TAB 1: UNIT CONVERTER
# ==============================================================================
with tab1:
    st.header("Mechanical Unit Converter")
    
    # Select category of conversion
    category = st.selectbox(
        "Select Conversion Category",
        ["Length", "Pressure", "Force", "Temperature"]
    )
    
    st.markdown("---")
    
    if category == "Length":
        col1, col2 = st.columns(2)
        with col1:
            val = st.number_input("Enter Value", value=1.0, key="len_val")
            from_unit = st.selectbox("From", ["Meters (m)", "Millimeters (mm)", "Inches (in)", "Feet (ft)"], key="len_from")
        with col2:
            to_unit = st.selectbox("To", ["Meters (m)", "Millimeters (mm)", "Inches (in)", "Feet (ft)"], key="len_to")
        
        # Base conversion to Meters
        factors_to_m = {
            "Meters (m)": 1.0,
            "Millimeters (mm)": 0.001,
            "Inches (in)": 0.0254,
            "Feet (ft)": 0.3048
        }
        
        # Conversion from Meters to destination
        factors_from_m = {
            "Meters (m)": 1.0,
            "Millimeters (mm)": 1000.0,
            "Inches (in)": 39.3701,
            "Feet (ft)": 3.28084
        }
        
        # Calculate
        val_in_m = val * factors_to_m[from_unit]
        converted = val_in_m * factors_from_m[to_unit]
        st.success(f"**Result:** {val} {from_unit.split()[1]} = **{converted:.4f} {to_unit.split()[1]}**")

    elif category == "Pressure":
        col1, col2 = st.columns(2)
        with col1:
            val = st.number_input("Enter Value", value=1.0, key="pres_val")
            from_unit = st.selectbox("From", ["Pascal (Pa)", "Kilopascal (kPa)", "Bar", "PSI (psi)", "Atmosphere (atm)"], key="pres_from")
        with col2:
            to_unit = st.selectbox("To", ["Pascal (Pa)", "Kilopascal (kPa)", "Bar", "PSI (psi)", "Atmosphere (atm)"], key="pres_to")
            
        # Base conversion to Pa
        factors_to_pa = {
            "Pascal (Pa)": 1.0,
            "Kilopascal (kPa)": 1000.0,
            "Bar": 100000.0,
            "PSI (psi)": 6894.76,
            "Atmosphere (atm)": 101325.0
        }
        
        factors_from_pa = {
            "Pascal (Pa)": 1.0,
            "Kilopascal (kPa)": 0.001,
            "Bar": 0.00001,
            "PSI (psi)": 0.000145038,
            "Atmosphere (atm)": 0.00000986923
        }
        
        val_in_pa = val * factors_to_pa[from_unit]
        converted = val_in_pa * factors_from_pa[to_unit]
        st.success(f"**Result:** {val} {from_unit.split()[1]} = **{converted:.4f} {to_unit.split()[1]}**")

    elif category == "Force":
        col1, col2 = st.columns(2)
        with col1:
            val = st.number_input("Enter Value", value=1.0, key="force_val")
            from_unit = st.selectbox("From", ["Newton (N)", "Kilonewton (kN)", "Pound-force (lbf)", "Kilogram-force (kgf)"], key="force_from")
        with col2:
            to_unit = st.selectbox("To", ["Newton (N)", "Kilonewton (kN)", "Pound-force (lbf)", "Kilogram-force (kgf)"], key="force_to")
            
        # Base conversion to Newtons
        factors_to_n = {
            "Newton (N)": 1.0,
            "Kilonewton (kN)": 1000.0,
            "Pound-force (lbf)": 4.44822,
            "Kilogram-force (kgf)": 9.80665
        }
        
        factors_from_n = {
            "Newton (N)": 1.0,
            "Kilonewton (kN)": 0.001,
            "Pound-force (lbf)": 0.224809,
            "Kilogram-force (kgf)": 0.101972
        }
        
        val_in_n = val * factors_to_n[from_unit]
        converted = val_in_n * factors_from_n[to_unit]
        st.success(f"**Result:** {val} {from_unit.split()[1]} = **{converted:.4f} {to_unit.split()[1]}**")

    elif category == "Temperature":
        col1, col2 = st.columns(2)
        with col1:
            val = st.number_input("Enter Value", value=0.0, key="temp_val")
            from_unit = st.selectbox("From", ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"], key="temp_from")
        with col2:
            to_unit = st.selectbox("To", ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"], key="temp_to")
            
        # Convert input to Celsius first
        if from_unit == "Celsius (°C)":
            temp_c = val
        elif from_unit == "Fahrenheit (°F)":
            temp_c = (val - 32) * 5/9
        else: # Kelvin
            temp_c = val - 273.15
            
        # Convert Celsius to target
        if to_unit == "Celsius (°C)":
            converted = temp_c
        elif to_unit == "Fahrenheit (°F)":
            converted = (temp_c * 9/5) + 32
        else: # Kelvin
            converted = temp_c + 273.15
            
        st.success(f"**Result:** {val} {from_unit.split()[-1]} = **{converted:.2f} {to_unit.split()[-1]}**")

# ==============================================================================
# TAB 2: DENSITY CHECKER & CALCULATOR
# ==============================================================================
with tab2:
    st.header("Material Density Database & Checker")
    
    # 1. Database Lookup
    st.subheader("Standard Materials Lookup")
    
    # Density dictionary (kg/m^3)
    material_densities = {
        "Mild Steel": 7850,
        "Stainless Steel (304)": 8000,
        "Aluminum": 2700,
        "Copper": 8960,
        "Brass": 8500,
        "Titanium": 4500,
        "Cast Iron": 7200,
        "Concrete": 2400,
        "Water": 1000,
        "Structural Timber (Pine)": 500
    }
    
    selected_material = st.selectbox("Select a Material", list(material_densities.keys()))
    density_kg_m3 = material_densities[selected_material]
    density_g_cm3 = density_kg_m3 / 1000.0
    
    # Display material details
    st.info(f"**{selected_material}** has a nominal density of:")
    col1, col2 = st.columns(2)
    col1.metric("Density in SI Units", f"{density_kg_m3} kg/m³")
    col2.metric("Density in g/cm³", f"{density_g_cm3} g/cm³")
    
    st.markdown("---")
    
    # 2. Density / Mass Calculator
    st.subheader("Manual Density & Weight Calculator")
    st.write("Calculate total weight based on volume and material choice, or calculate custom density.")
    
    calc_mode = st.radio("Choose Action:", ["Calculate Mass from Volume", "Calculate Custom Density"])
    
    if calc_mode == "Calculate Mass from Volume":
        vol = st.number_input("Enter Volume (m³)", min_value=0.0001, value=1.0, format="%.6f")
        chosen_density = st.number_input("Material Density (kg/m³)", min_value=1.0, value=float(density_kg_m3))
        
        mass = vol * chosen_density
        st.success(f"Calculated Mass: **{mass:.3f} kg** (or **{mass * 2.20462:.3f} lbs**)")
        
    elif calc_mode == "Calculate Custom Density":
        mass_input = st.number_input("Enter Measured Mass (kg)", min_value=0.001, value=1.0)
        vol_input = st.number_input("Enter Measured Volume (m³)", min_value=0.0001, value=0.5, format="%.6f")
        
        calculated_density = mass_input / vol_input
        st.success(f"Calculated Density: **{calculated_density:.2f} kg/m³**")
