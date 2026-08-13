from pathlib import Path

import streamlit as st


DATA_DIR = Path("data")


def init_data_dir():
    DATA_DIR.mkdir(exist_ok=True)


def subject_filename(subject):
    return subject.replace(" ", "").replace(".", "").lower()


def subject_path(subject):
    return DATA_DIR / f"{subject_filename(subject)}.txt"


def get_subjects():
    init_data_dir()
    return sorted(path.stem.capitalize() for path in DATA_DIR.glob("*.txt"))


def create_subject(subject):
    clean_subject = subject_filename(subject)
    if not clean_subject:
        raise ValueError("Please enter a subject name.")

    path = DATA_DIR / f"{clean_subject}.txt"
    if path.exists():
        raise FileExistsError("Subject already exists.")

    path.touch()


def save_result(first_name, last_name, matric_no, subject, score):
    with subject_path(subject).open("a", encoding="utf-8") as file:
        file.write(f"{first_name} {last_name} {matric_no} {score}\n")


def get_results(subject):
    path = subject_path(subject)
    if not path.exists():
        return []

    results = []
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            row = line.strip().split()
            if len(row) == 4:
                results.append(row)
    return results


def result_exists(subject, matric_no):
    return any(row[2] == matric_no for row in get_results(subject))


def validate_score_form(first_name, last_name, matric_no, subject, score):
    if not subject:
        return "Please choose a subject."

    if not first_name or not last_name or not matric_no or score is None:
        return "Please fill in all the details."

    if not matric_no.isdigit():
        return "Matric number must be a number."

    if len(matric_no) != 9:
        return "Matric number must be 9 digits."

    if result_exists(subject, matric_no):
        return "Result has already been recorded for this student."

    if score < 0:
        return "Score cannot be lower than 0."

    if score > 100:
        return "Score cannot be higher than 100."

    return None


def render_create_subject():
    st.subheader("Create Subject")

    with st.form("create-subject", clear_on_submit=True):
        subject = st.text_input("Subject name")
        submitted = st.form_submit_button("Create Subject")

    if submitted:
        try:
            create_subject(subject)
        except FileExistsError as error:
            st.error(str(error))
        except ValueError as error:
            st.warning(str(error))
        else:
            st.success("Subject created successfully.")


def render_add_score(subjects):
    st.subheader("Add Score")

    with st.form("add-score", clear_on_submit=True):
        first_name = st.text_input("First name")
        last_name = st.text_input("Last name")
        matric_no = st.text_input("Matric number", max_chars=9)
        score = st.number_input("Score", min_value=0, max_value=100, step=1)
        subject = st.selectbox("Subject", subjects, index=None, placeholder="Choose a subject")
        submitted = st.form_submit_button("Add Score")

    if submitted:
        error = validate_score_form(
            first_name.strip(),
            last_name.strip(),
            matric_no.strip(),
            subject,
            score,
        )

        if error:
            st.warning(error)
        else:
            save_result(
                first_name.strip(),
                last_name.strip(),
                matric_no.strip(),
                subject,
                int(score),
            )
            st.success("Score saved.")


def render_average_stats(subjects):
    st.subheader("Average Stats")

    subject = st.selectbox("Subject", subjects, index=None, placeholder="Choose a subject")
    if not subject:
        return

    results = get_results(subject)
    if not results:
        st.info("No scores have been added for this subject yet.")
        return

    scored_results = [(row, int(row[3])) for row in results]
    highest = max(scored_results, key=lambda item: item[1])[0]
    lowest = min(scored_results, key=lambda item: item[1])[0]
    mean = sum(score for _, score in scored_results) / len(scored_results)
    above_70 = [row for row, score in scored_results if score > 70]

    col1, col2, col3 = st.columns(3)
    col1.metric("Mean score", f"{mean:.2f}")
    col2.metric("Highest score", highest[3])
    col3.metric("Above 70", len(above_70))

    st.write("Highest scoring student")
    st.table([format_result_row(highest)])

    st.write("Lowest scoring student")
    st.table([format_result_row(lowest)])

    if above_70:
        st.write("Students who scored above 70")
        st.table([format_result_row(row) for row in above_70])


def format_result_row(row):
    return {
        "First name": row[0],
        "Last name": row[1],
        "Matric number": row[2],
        "Score": int(row[3]),
    }


def render_student_stats(subjects):
    st.subheader("Student Stats")

    subject = st.selectbox(
        "Subject",
        subjects,
        index=None,
        placeholder="Choose a subject",
        key="student-stats-subject",
    )
    if not subject:
        return

    results = get_results(subject)
    if not results:
        st.info("No scores have been added for this subject yet.")
        return

    rows = []
    for index, row in enumerate(results, start=1):
        formatted = format_result_row(row)
        formatted = {"SN": index, **formatted}
        rows.append(formatted)

    st.dataframe(rows, hide_index=True, use_container_width=True)


def main():
    st.set_page_config(page_title="Student Result Manager")
    init_data_dir()

    st.title("Student Result Manager")

    subjects = get_subjects()
    page = st.sidebar.radio(
        "Menu",
        ["Create Subject", "Add Score", "Stats", "Student Stats"],
    )

    if page != "Create Subject" and not subjects:
        st.info("Create a subject before adding or viewing scores.")
        render_create_subject()
        return

    if page == "Create Subject":
        render_create_subject()
    elif page == "Add Score":
        render_add_score(subjects)
    elif page == "Stats":
        render_average_stats(subjects)
    else:
        render_student_stats(subjects)


if __name__ == "__main__":
    main()
