import streamlit as st

st.title("AceCourt Sports Centre Booking System")

if "step" not in st.session_state:
    st.session_state.step = 1

# STEP 1: Booking details
if st.session_state.step == 1:
    st.header("Step 1: Booking Details")

    booking_date = st.date_input("Booking Date")
    court_type = st.selectbox("Type of Sport Court", ["Badminton", "Basketball", "Futsal"])
    starting_time = st.time_input("Starting Time")
    duration = st.number_input("Duration (Hours)", min_value=1, max_value=5)

    if st.button("Next"):
        st.session_state.booking_date = booking_date
        st.session_state.court_type = court_type
        st.session_state.starting_time = starting_time
        st.session_state.duration = duration
        st.session_state.step = 2
        st.rerun()

# STEP 2: User details
elif st.session_state.step == 2:
    st.header("Step 2: Personal & Payment Details")

    username = st.text_input("Username")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email Address")
    payment_method = st.selectbox("Payment Method", ["Online Banking", "DuitNow QR"])

    if st.button("Confirm Booking"):
        st.session_state.username = username
        st.session_state.phone = phone
        st.session_state.email = email
        st.session_state.payment_method = payment_method
        st.session_state.step = 3
        st.rerun()

    if st.button("Back"):
        st.session_state.step = 1
        st.rerun()

#STEP 3:Booking Comfirmed
elif st.session_state.step == 3:
        st.header("Confirm Booking")
        price = st.session_state.duration * 20

        st.success("Booking Confirmed!")

        st.write("### Booking Receipt")
        st.write(f"Booking Date: {st.session_state.booking_date}")
        st.write(f"Court Type: {st.session_state.court_type}")
        st.write(f"Starting Time: {st.session_state.starting_time}")
        st.write(f"Duration: {st.session_state.duration} hour(s)")
        st.write(f"Username: {st.session_state.username}")
        st.write(f"Phone Number: {st.session_state.phone}")
        st.write(f"Email Address: {st.session_state.email}")
        st.write(f"Payment Method: {st.session_state.payment_method}")
        st.write(f"Total Price: RM{st.session_state.price}")

    if st.button("Make Another Booking"):
        st.session_state.step = 1
        st.rerun()
