import streamlit as st
import pandas as pd
from datetime import time

# Assuming 'courses' is fetched from an API and is available as a list of dictionaries
courses = [
    {"courseID": "12345", "Short_Name": "Strategic Management", "Description": "This course is ABC..."},
    {"courseID": "98765", "Short_Name": "Strategic Leadership", "Description": "This course is CBA..."}
]

def main():
    st.title("Study Planner Interface")

    # Dropdown for courses
    course_options = {course['Short_Name']: course for course in courses}
    selected_course = st.selectbox("Select a Course", options=list(course_options.keys()))
    course_details = course_options[selected_course]

    # Inputs for exam date and ECTS
    exam_date = st.date_input("Exam Date")
    ects = st.number_input("ECTS", min_value=0, step=1)

    # Study time inputs
    start_hour = st.time_input('Start Hour', value=time(hour=8))
    lunch_break = st.number_input('Lunch Break (minutes)', min_value=0, max_value=240, value=60)
    lunch_break_start = st.time_input('Lunch Break Start Hour', value=time(hour=12))
    end_hour = st.time_input("End Hour", value=time(hour=17))

    # Save the data
    my_courses = [{
        "courseID": course_details["courseID"],
        "Short_Name": course_details["Short_Name"],
        "Description": course_details["Description"],
        "exam_date": exam_date.strftime("%d.%m.%Y"),
        "ECTS": ects
    }]

    st.write("Your Courses:", my_courses)

if __name__ == "__main__":
    main()
