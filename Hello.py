# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Streamlit! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )
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

if __name__ == "__main__":
    run()
