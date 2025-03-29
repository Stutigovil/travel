import streamlit as st
import requests
import google.generativeai as genai
import os

api_key = "AIzaSyDwPHN1Gb0Qph2eBEynNkVwFX29mh6wzFA"
genai.configure(api_key=api_key)


def get_itinerary(destination, days, interests, budget,walking,health,season,wildlife,travel_guide,dine_in,public_travel,recommendation,age):
    prompt = f"""
    Create a {days}-day travel itinerary for {destination} based on these preferences 
    walking distance should be according to preference {walking}
    it should also be based on season :{season} of travel
    Interests: {interests}
    Budget: {budget}
    Health: {health}
    Wildlife: {wildlife}
    Travel guide: {travel_guide}
    restuarants:{dine_in}
    public travel:{public_travel}
    suggest places and acitivities according to the age {age}

    hotel Recommendation: {recommendation} according to the {budget} and {dine_in} type
    The itinerary should include:
    - Morning, afternoon, and evening activities.
    - Dining recommendations.
    - Local attractions and famous places of the town irrespective of interests.
    Sum of all of this travel will be strictly under the {budget} range
    """
    
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)

    return response.text 

st.title("🌍 Travel Guide Application")
st.write("Plan your trip effortlessly!")
#destination, days, interests, budget,walking,health,season,wildlife,travel_guide,dine_in,public_travel,recommendation,age

destination = st.text_input("Enter Destination (City, Country)")
days = st.slider("Number of Days", 1, 20, 3)

budgets = st.text_input("Budget")
if(budgets=="moderate"):
    budget = 10000
elif(budgets=="luxury"):
    budget=17000
else: 
    budget=int(budgets)

walking=st.selectbox("Do you have problem in walking?",["Yes","No"])
health=st.text_input("Do you have any health issues?")
season=st.selectbox("Season of travel",["Summer","Winter","Rainy","Autumn"])
wildlife=st.selectbox("Wildlife preference",["Yes","No"])
public_travel=st.selectbox("Are you comfortable in public travel",["Yes","No"])
travel_guide=st.selectbox("Travel guide preference",["Yes","No"])
dine_in=st.text_input("Dine in preference")
recommendation=st.selectbox("Do you need Hotel Recommendation",["Yes","No"])
age=st.number_input("Enter your age",min_value=1,step=1)
option=["Adventure and Outdoor Activities","Spiritual","Recreational Activities","Fun & Entertainment","Historical and cultural Exploration","Shopping","Nature & Relaxation","Sightseeing","Photography","Space & Science"]
interests = st.multiselect("Your Interests",option)


if st.button("Generate Itinerary"):
    if destination:
        with st.spinner("Fetching itinerary..."):
            itinerary = get_itinerary(destination, days, interests, budget,walking,health,season,wildlife,travel_guide,dine_in,public_travel,recommendation,age)
            st.subheader(f"📍 {days}-Day Itinerary for {destination}")
            st.write(itinerary)
            
    else:
        st.error("Please enter a destination!")
