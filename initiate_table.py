import datetime
import sqlite3
import functions
import tabulate

functions.user_table()
functions.competencies_table()
functions.assessment_table()
functions.competency_assessment_results_table()

functions.csv_import_users()
functions.csv_import_competencies()
functions.csv_import_assessments()
functions.csv_import_assessment_results()