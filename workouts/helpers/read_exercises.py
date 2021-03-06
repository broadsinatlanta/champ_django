"""
User in manage.py shell to import exercises_fin.csv into the database.

Not needed bar the initial entry.
"""

import csv
import os

from django.contrib.auth.models import User

from workouts.models import Exercise


me = User.objects.get(id=1)


def makeEntry(row):
    return Exercise(
                exercise=row['Exercise'],
                gym_level=row['GymLevel'],
                equipment=row['Equipment'],
                exercise_type=row['ExerciseType'],
                movement_type=row['MovementType'],
                compound_isolation=row['Compound/Isolation'],
                muscle_group=row['MuscleGroup'],
                major_muscles=row['MajorMuscle'],
                minor_muscles=row['MinorMuscle'],
                beginner='Yes' if int(row['Beginner']) == 1 else 'No',
                intermediate='Yes' if int(row['Intermediate']) == 1 else 'No',
                advanced='Yes' if int(row['Advanced']) == 1 else 'No',
                sl='Yes' if row['SL'] == "1" else 'No',
                gvt='Yes' if row['GVT'] == '1' else 'No',
                main_lift=row['MainLift'],
                owner=me,
            )

with open('workouts/helpers/exercises_fin.csv', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        e = makeEntry(row)
        print(True if e else False)
        e.save()
