import streamlit as st
from utils import render_step_progress

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

    # Core instructional parameters
    course_title = st.sidebar.text_input("Course Title", placeholder="e.g., Principles of Hospitality Management")
    course_code = st.sidebar.selectbox("Course Code", ["None"] + COURSE_CODES)
    subject_domain = st.sidebar.text_input("Subject Domain", placeholder="e.g., Hospitality Management")

    num_modules = st.sidebar.number_input("Number of Modules", min_value=1, max_value=30, value=4)
    total_hours = st.sidebar.number_input("Total Course Hours", min_value=1, max_value=200, value=20)
    hours_per_module = st.sidebar.number_input("Hours per Module", min_value=1, max_value=20, value=5)

    learner_level = st.sidebar.selectbox("Learner Level", [
        "Beginner", "Intermediate", "Advanced", "Mixed / All Levels", 
        "Professional / Continuing Education", "Undergraduate", "Graduate", "Other (manual input)"
    ])

    mode_of_delivery = st.sidebar.selectbox("Mode of Delivery", [
        "Online (self-paced)", "Online (instructor-led)", "Hybrid (blended learning)",
        "In-person", "MOOC (Massive Open Online Course)", "Other (manual input)"
    ])

    learner_type = st.sidebar.selectbox("Learner Type", [
        "Adult learners", "Working professionals", "Undergraduate students", 
        "Graduate students", "Career switchers", "High school students", 
        "Technical specialists", "Custom (manual input)"
    ])

    prerequisites = st.sidebar.text_area("Prerequisites", placeholder="List any required prior knowledge or experience")
    course_description = st.sidebar.text_area("Course Description", placeholder="Summarize the course purpose, scope, and goals")
    learning_outcomes = st.sidebar.text_area("List of Learning Outcomes", placeholder="List specific skills/knowledge students will gain")
    course_outline = st.sidebar.text_area("Course Outline", placeholder="Provide a list of modules or topics in order")

    instructional_methods = st.sidebar.text_area("List of Instructional Methods", placeholder="e.g., lectures, case studies, simulations")

    tone = st.sidebar.selectbox("Tone", [
        "Professional", "Academic Formal", "Friendly", 
        "Conversational", "Encouraging", "Practical & Applied"
    ])

    assessment_strategy = st.sidebar.multiselect("Assessment Strategy", [
        "Quizzes (multiple choice)", "Open-ended reflection questions", "Graded assignments",
        "Final project or capstone", "Peer review", "Case analysis", 
        "Scenario-based tasks", "Formative assessments only", "Other (manual input)"
    ])

    num_key_concepts = st.sidebar.number_input("Number of Key Concepts per Module", min_value=1, max_value=10, value=3)

    return {
        "Course_Title": course_title or "Hospitality Course",
        "Course_Code": course_code or "HOSP 000",
        "Subject_Domain": subject_domain or "Hospitality and Tourism",
        "Number_of_modules": num_modules,
        "Total_Hours": total_hours,
        "Hours_per_Module": hours_per_module,
        "Learner_Level": learner_level,
        "Mode_of_Delivery": mode_of_delivery,
        "Learner_Type": learner_type,
        "Prerequisites": prerequisites or "None",
        "Cours_Description": course_description or "This course introduces core concepts in hospitality and tourism.",
        "List_of_Learning_Outcomes": learning_outcomes or "Understand hospitality operations, customer service, and industry trends.",
        "Course_Outline": course_outline or "Module 1: Introduction\nModule 2: Operations\nModule 3: Customer Experience\nModule 4: Innovation in Hospitality",
        "List_of_Instructional_Methods": instructional_methods or "Lectures, real-world case studies, group discussions",
        "Tone": tone or "Friendly",
        "Assessment_Strategy": assessment_strategy or ["Quizzes (multiple choice)", "Case analysis"],
        "Number_of_Key_Concept": num_key_concepts
    }

# Generate the course prompt
def generate_course_prompt(course):
    # example_file_display = course['Example Course File'].name if course['Example Course File'] else "None"
    return f"""
## SYSTEM ROLE
You are a veteran online course designer and instructor with over 20 years of experience teaching <span style='color:red'>**{course['Subject_Domain']}**</span>. Your task is to generate a comprehensive, fully written, <span style='color:red'>**{course['Number_of_modules']}**</span> -module course on <span style='color:red'>**{course['Course_Title']}**</span> (total duration:  <span style='color:red'>**{course['Total_Hours']}**</span>  hours, </span> (total duration: <span style='color:red'>**{course['Hours_per_Module']}**</span> hours per module). The course must be informative, engaging, and accessible to learners at the <span style='color:red'>**{course['Learner_Level']}**</span> level. Course delivery mode will be <span style='color:red'>**{course['Mode_of_Delivery']}**</span>. 

## USER INPUT
- Course Title: <span style='color:red'>**{course['Course_Title']}**</span>
- Subject Domain: <span style='color:red'>**{course['Subject_Domain']}**</span> 
- Audience & Context:<span style='color:red'>**{course['Learner_Type']}**</span> ; <span style='color:red'>**{course['Prerequisites']}**</span>
- Delivery Format: Detailed narrative course content, organized into modules, sessions, and learning activities.
- Total Duration: <span style='color:red'>**{course['Number_of_modules']}**</span> modules (each <span style='color:red'>**{course['Hours_per_Module']}**</span> hours; total <span style='color:red'>**{course['Total_Hours']}**</span> hours).
- Course Description: <span style='color:red'>**{course['Cours_Description']}**</span>
- Learning Outcomes:<span style='color:red'>**{course['List_of_Learning_Outcomes']}**</span>
- Course Outline (aligned to textbook or structure): <span style='color:red'>**{course['Course_Outline']}**</span>
- Instructional Methods:  <span style='color:red'>**{course['List_of_Instructional_Methods']}**</span>

## YOUR TASK
Using the above inputs, generate the complete, well written and well structured, module-by-module course content (not just outlines or bullet points). For each module and each major chapters/sessions within it, provide:

1. Module Overview & Objectives:
Provide a short introduction and 3 module-specific objectives aligned with the learning outcomes.

2. Lecture Narrative:
Provide a detailed, scripted lecture narrative using a <span style='color:red'>**{course['Tone']}**</span> tone.  Ensure the language is engaging, conceptually clear, and logically structured.  

3. Key Concept Definitions:
List and define up to  <span style='color:red'>**{course['Number_of_Key_Concept']}**</span> essential terms introduced in the module.

4. Discussion Prompt:
Provide 2 to 3 open-ended, thought-provoking questions that encourage learner reflection.

5. Micro-learning Objectives (per session/topic):
Break the module into approximately 3 to 5 sessions with short learning objectives for each session.

6. Real-World Examples or Case Studies:
Include at least 1 concrete, industry-relevant example per module.

7. Interactive Activities & Assessments:
Design at least 1 <span style='color:red'>**{course['Assessment_Strategy']}**</span> for each module. For quizzes, provide 3 - 5 sample questions with correct answers. For open-ended tasks, provide sample rubric or guidance. For assignments, provide well structured questions and tasks.

8. Recommended Readings & Resources:  
Suggest textbook chapters, whitepapers, guides, articles, or relevant external tools and resources. Include links or citation-style references when possible.

9. Transitions & Summary:
Conclude each module with a recap of major takeaways. Mention connections to prior and upcoming modules to maintain narrative continuity

At the end of the last module only, provide a course-wide summary, including 5 to 10 Key takeaways and final reflection prompt.



## STYLE & STRUCTURE GUIDELINES
Use a structured and logical flow aligned with the learning outcomes.
Be richly detailed and instructional, including figures, diagrams (if appropriate) and tactical insights. Where appropriate, “suggest” visuals such as conceptual diagrams, data tables, or process flows.
Avoid lists or outlines where full narrative explanations are needed.
Assume students will not be using a companion syllabus; your output should be self-contained and course-ready.
Use a <span style='color:red'>**{course['Tone']}**</span> tone that remains engaging and learner-centered.  
Be as detailed as possible, think about micro-learning objectives, specific case names, sample questions, and activities.
Use appropriate formatting with clear headings, bolded key terms, and paragraph breaks for readability. Lists should only be used for definitions or exercises where necessary.

Ensure the course is self-contained, detailed, and aligned with learning outcomes. Use a clear, engaging <span style='color:red'>**{course['Tone']}**</span> tone. Present content as full narrative (not outlines), with suggested visuals where helpful. Use clear structure with headings and paragraph spacing. Include real-world examples and micro-learning objectives per module.
 
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
            file_name=f"{course['Course_Code']}_{course['Course_Title'].replace(' ', '_')}_prompt.txt",
            mime="text/plain"
        )



    # ✅ Render Markdown directly (so bold works!)
    st.markdown(prompt, unsafe_allow_html=True)


# Main app function


# https://create-prompt-app-vmsknnghyebxx78rdmpq9s.streamlit.app/
# Instead of main(), just call directly:
st.set_page_config("Course Configuration", layout="wide")
st.title("1️⃣ Tourism and Hospitality Prompt Builder")

render_step_progress(current_step=1)
if 'generated_prompt' not in st.session_state:
    st.session_state.generated_prompt = ''

course_input = get_user_input()

if st.sidebar.button("✅ Generate Course Prompt"):
    display_prompt(course_input)
elif st.session_state.generated_prompt:
    display_prompt(course_input)
else:
    st.info("Use the sidebar to fill out course details and click '✅ Generate Course Prompt'.")
