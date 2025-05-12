import streamlit as st

# List of all the course topics from the table
COURSE_TOPICS = [
    "Management of Food and Beverage Operations",
    "Managing Front Office Operations",
    "Managing Housekeeping Operations",
    "Managing Beverage Service",
    "Managing Hospitality Human Resources",
    "Hospitality Facilities Management and Design",
    "Revenue Management",
    "Security and Loss Prevention Management",
    "Hospitality Sales and Marketing",
    "Convention Management and Service",
    "Basic Hotel and Restaurant Accounting",
    "Introduction to Travel and Tourism: An International Approach",
    "Supervision in the Hospitality Industry",
    "Managing Technology in the Hospitality Industry",
    "Service Excellence",
    "Hospitality Today"
]

# Course Codes
COURSE_CODES = [
    "HOSP 241", "HOSP 333", "HOSP 338", "HOSP 323", "HOSP 357", "HOSP 281",
    "HOSP 374", "HOSP 387", "HOSP 472", "HOSP 378", "HOSP 261", "HOSP 101",
    "HOSP 250", "HOSP 468", "HOSP 299", "HOSP 103"
]

# Career Occupation list
CAREER_OCCUPATIONS = [
    "Rooms Division: Front Desk Agent", "Reservation Agent", "Night Auditor", "Switch Board Operator", "Bell Person",
    "Concierge", "Room Attendant", "Laundry Attendant", "House Person", "Room Service Attendant", "Restaurant/Bar/Lounge Server",
    "Banquets’ Server", "Sales/Marketing Coordinator", "Catering/Banquets Coordinator"
]

# Target Audience options
TARGET_AUDIENCE_OPTIONS = [
    "Undergraduate students", "Professionals", "Career changers", "Aspiring hospitality managers", "Tourism enthusiasts", "Executives", "Interns", "None"
]

EXPERTISE_LEVEL_OPTIONS = [
    "Beginner", "Intermediate", "Advanced", "None"
]

# Tone options
TONE_OPTIONS = [
    "Formal", "Informal", "Friendly", "Conversational", "Beginner-friendly", "Technical", "None"
]

# Input form for course details
def get_user_input():
    st.sidebar.header("Course Configuration")

    course_title = st.sidebar.selectbox("Course Title & Topic", ["None"] + COURSE_TOPICS)
    instructor = st.sidebar.text_input("Instructor", placeholder="Enter the instructor's name")
    course_code = st.sidebar.selectbox("Course Code", ["None"] + COURSE_CODES)
    hours = st.sidebar.number_input("How many hours", min_value=1, max_value=200, value=20)
    duration = st.sidebar.selectbox("Duration", ["None", "2 weeks", "3 weeks", "4 weeks", "1 semester", "Full year"])
    delivery_mode = st.sidebar.selectbox("Delivery Mode", ["None", "Face-to-face", "Online", "Hybrid", "Flipped Classroom", "Intensive"], index=2)
    course_description = st.sidebar.text_area("Course Description")
    num_modules = st.sidebar.number_input("Number of Modules", min_value=1, max_value=30, value=4)
    industry_certifications = st.sidebar.text_area("Industry-Specific Certifications")
    career_occupation = st.sidebar.selectbox("Career Occupation", ["None"] + CAREER_OCCUPATIONS)

    learning_objectives = st.sidebar.text_area("Learning Objectives")
    key_topics = st.sidebar.text_area("Key Topics")
    activities_assessments = st.sidebar.text_area("Activities & Assessments")
    prerequisites = st.sidebar.text_area("Prerequisites")
    co_requisites = st.sidebar.text_area("Co-requisites (optional)")
    course_outline = st.sidebar.text_area("Course Outline")

    target_audience = st.sidebar.selectbox("Target Audience", ["General learners"] + TARGET_AUDIENCE_OPTIONS)
    expertise_level = st.sidebar.selectbox("Expertise Level", ["Beginner"] + EXPERTISE_LEVEL_OPTIONS)
    tone = st.sidebar.selectbox("Tone & Style", ["None"] + TONE_OPTIONS)

    preferred_content_format = st.sidebar.multiselect("Preferred Content Format", ["None", "Lesson plans", "Lectures & PowerPoint Presentations", "Guest Speakers", "Video scripts", "Activities", "Quizzes", "Case studies"])
    student_engagement_methods = st.sidebar.multiselect("Student Engagement Methods", ["None", "Group projects", "Peer reviews", "Online discussions", "Interactive workshops", "Case study analysis"])

    instructor_guest_speaker = st.sidebar.text_area("Guest Speaker")
    references = st.sidebar.text_area("References & Examples")
    example_course_file = st.sidebar.file_uploader("Example Course File", type=["pdf", "docx", "pptx", "txt"])
    notes = st.sidebar.text_area("Notes/Additional Information")

    return {
        "Course Title": course_title or "Hospitality Course",
        "Instructor": instructor or "TBD",
        "Course Code": course_code or "HOSP 000",
        "Hours": hours,
        "Duration": duration or "4 weeks",
        "Delivery Mode": delivery_mode or "Online",
        "Course Description": course_description or "This course explores key themes in hospitality and tourism.",
        "Number of Modules": num_modules,
        "Industry Certifications": industry_certifications or "None specified",
        "Career Occupation": career_occupation or "General Hospitality Roles",
        "Learning Objectives": learning_objectives or "Understand the fundamentals of hospitality and tourism management.",
        "Key Topics": key_topics or "Customer service, operations, marketing, HR, technology",
        "Activities & Assessments": activities_assessments or "Quizzes, group projects, case study analysis",
        "Prerequisites": prerequisites or "None",
        "Co-requisites": co_requisites or "None",
        "Course Outline": course_outline or "Module 1: Introduction\nModule 2: Operations\nModule 3: Customer Service\nModule 4: Technology in Hospitality",
        "Target Audience": f"{target_audience or 'General learners'} - {expertise_level or 'Beginner'}",
        "Tone": tone or "Friendly",
        "Preferred Content Format": preferred_content_format or ["Lesson plans", "Activities"],
        "Student Engagement Methods": student_engagement_methods or ["Group projects", "Interactive workshops"],
        "Guest Speaker": instructor_guest_speaker or "Guest speakers from the hospitality industry",
        "References": references or "Hospitality Today by Walker",
        "Example Course File": example_course_file,
        "Notes": notes or "N/A"
    }

# Generate the course prompt
def generate_course_prompt(course):
    example_file_display = course['Example Course File'].name if course['Example Course File'] else "None"
    return f"""
## SYSTEM ROLE
You are an expert online course instructor with 20 years’ experience teaching Hospitality & Tourism Management. Your mission is to generate a fully detailed,<span style='color:red'>**{course['Number of Modules']}**</span>-module course on <span style='color:red'>**{course['Course Title']}**</span> (<span style='color:red'>**{course['Hours']}**</span> hours total, in <span style='color:red'>**{course['Duration']}**</span> duration). The output must be informative, engaging, and structured for easy understanding by learners at the <span style='color:red'>**{course['Target Audience']}**</span> level.

## USER INPUT
- **Course Title & Topic:** <span style='color:red'>**{course['Course Title']}**</span>
- **Instructor**: <span style='color:red'>**{course['Instructor']}**</span>
- **Course Code**: <span style='color:red'>**{course['Course Code']}**</span>
- **Total Duration**: <span style='color:red'>**{course['Duration']}**</span> (<span style='color:red'>**{course['Hours']}**</span> total hours)
- **Course Description**: <span style='color:red'>**{course['Course Description']}**</span>
- **Learning Outcomes**: <span style='color:red'>**{course['Learning Objectives']}**</span>
- **Key Topics**: <span style='color:red'>**{course['Key Topics']}**</span>
- **Activities & Assessments**: <span style='color:red'>**{course['Activities & Assessments']}**</span>
- **Prerequisites**: <span style='color:red'>**{course['Prerequisites']}**</span>
- **Co-requisites**: <span style='color:red'>**{course['Co-requisites']}**</span>
- **Course Outline**: <span style='color:red'>**{course['Course Outline']}**</span>
- **Delivery Mode**: <span style='color:red'>**{course['Delivery Mode']}**</span>
- **Industry Certifications**: <span style='color:red'>**{course['Industry Certifications']}**</span>
- **Career Occupation**: <span style='color:red'>**{course['Career Occupation']}**</span>
- **Target Audience and level**: <span style='color:red'>**{course['Target Audience']}**</span>
- **Tone**: <span style='color:red'>**{course['Tone']}**</span>
- **Preferred Content Format**: <span style='color:red'>**{', '.join(course['Preferred Content Format'])}**</span>
- **Student Engagement Methods**: <span style='color:red'>**{', '.join(course['Student Engagement Methods'])}**</span>
- **Guest Speaker**: <span style='color:red'>**{course['Guest Speaker']}**</span>
- **References**: <span style='color:red'>**{course['References']}**</span>
- **Example Course File**: {example_file_display}
- **Notes**: <span style='color:red'>**{course['Notes']}**</span>

## YOUR TASK
Using the above specification, produce all of the course content: no syllabus, no lesson-plan tables, just the fully written, module-by-module teaching text. For each module and each major topic within it, include:
1. **Module Overview & Objectives** (with 2–3 module objectives aligned to learning outcomes)
2. **Lecture Narrative**: A scripted, engaging explanation of concepts in a <span style='color:red'>**{course['Tone']}**</span> yet approachable tone.
3. **Key Concept Definitions**: Clear, concise definitions of terms.
4. **Discussion Prompts**: 2–3 questions to spark class conversation.
5. **Micro-learning objectives per session**
6. **Real-World Examples or Case Studies**
7. **Interactive Activities & Assessments** considering <span style='color:red'>**{course['Activities & Assessments']}**</span>
8. **Recommended Readings & Resources**: <span style='color:red'>**{course['References']}**</span>
9. **Transitions & Summary**: A brief wrap-up of the module’s takeaways and a transition into the next module. Clear linkage between sessions and modules, with a closing summary and reflection prompt.
10. In addition consider: <span style='color:red'>**{course['Notes']}**</span>

Finally, conclude with a course-wide summary of key takeaways and a call to action inviting deeper exploration.

Use a <span style='color:red'>**{course['Tone']}**</span> tone that remains engaging and learner-centered. Be as detailed as possible, think micro-learning objectives, specific case names, sample questions, and activities.
"""

# Display prompt and download option
def display_prompt(course):
    st.subheader("📄 Generated Course Prompt")
    prompt = generate_course_prompt(course)
    st.session_state.generated_prompt = prompt

    # Remove HTML tags and bold markdown for plain text download
    plain_text_prompt = prompt.replace("<span style='color:red'>**", "").replace("</span>", "").replace("**", "")

    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            label="💾 Save Prompt as .txt",
            data=plain_text_prompt,
            file_name=f"{course['Course Code']}_{course['Course Title'].replace(' ', '_')}_prompt.txt",
            mime="text/plain"
        )



    # ✅ Render Markdown directly (so bold works!)
    st.markdown(prompt, unsafe_allow_html=True)


# Main app function
def main():
    st.set_page_config("Hospitality Course Builder", layout="wide")
    st.title("💥 Tourism and Hospitality Course Builder")

    if 'generated_prompt' not in st.session_state:
        st.session_state.generated_prompt = ''

    course_input = get_user_input()

    if st.sidebar.button("✅ Generate Course Prompt"):
        display_prompt(course_input)
    elif st.session_state.generated_prompt:
        display_prompt(course_input)
    else:
        st.info("Use the sidebar to fill out course details and click '✅ Generate Course Prompt'.")

if __name__ == "__main__":
    main()