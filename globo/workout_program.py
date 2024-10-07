import datetime
import workout

MON, TUE, WED, THU, FRI, SAT, SUN = range(7)


WS4SB = {
    MON: workout.MaxEffortUpperBody,
    WED: workout.DynamicEffortLowerBody,
    FRI: workout.RepetitionUpperBody,
    SAT: workout.MaxEffortLowerBody,
}

# r/Fitness beginner routine
# https://thefitness.wiki/routines/r-fitness-basic-beginner-routine/
# Switch back and forth by week so order goes A, B, A, B, ...
WORKOUT_SWITCH = (datetime.datetime.today().isocalendar()[1] % 2) == 0


def _activeRecoverySelector():
    triSwitch = (datetime.datetime.today().isocalendar()[1] % 3) == 0
    if WORKOUT_SWITCH and triSwitch:
        return workout.YogaWorkoutA
    elif triSwitch:
        return workout.YogaWorkoutB
    else:
        return workout.StretchWorkout


def _longevityRecoveryWeekSwitch():
    """Allows a switch for 'every other even week'"""
    return (datetime.datetime.today().isocalendar()[1] % 4) == 0


def _longevityGetWednesday():
    """Gets the correct wednesday switch based on week."""
    return workout.FiveThreeOneWorkout if WORKOUT_SWITCH else workout.DownDogYogaVinyasa


def _longevityGetSunday():
    """Gets the correct sunday switch based on week."""
    return workout.DownDogYogaStretch if WORKOUT_SWITCH else workout.VO2Max


BasicStrengthTraining = {
    MON: workout.WorkoutA if WORKOUT_SWITCH else workout.WorkoutB,
    TUE: workout.ConditioningA if WORKOUT_SWITCH else workout.ConditioningB,
    WED: workout.WorkoutB if WORKOUT_SWITCH else workout.WorkoutA,
    THU: workout.WorkoutA if WORKOUT_SWITCH else workout.WorkoutB,
    FRI: _activeRecoverySelector(),
}

TrekTraining = {
    MON: workout.TrekAerobicA if WORKOUT_SWITCH else workout.TrekAerobicB,
    TUE: workout.Climb,
    THU: workout.TrekAerobicB if WORKOUT_SWITCH else workout.TrekAerobicA,
    FRI: workout.TrekStrength,
    SAT: _activeRecoverySelector(),
    SUN: workout.Climb,
}

# See https://thefitness.wiki/routines/5-3-1-for-beginners/
FiveThreeOne = {
    MON: workout.FiveThreeOneWorkout,
    TUE: workout.DownDogYogaVinyasa if WORKOUT_SWITCH else workout.DownDogYogaStretch,
    WED: workout.FiveThreeOneWorkout,
    THU: workout.DownDogHiit if WORKOUT_SWITCH else workout.ModerateCardio,
    FRI: workout.FiveThreeOneWorkout,
}

# See https://old.reddit.com/r/Fitness/comments/zc0uy/a_beginner_dumbbell_program_the_dumbbell_stopgap/
DumbbellStopGap = {
    MON: workout.DumbbellStopgapA if WORKOUT_SWITCH else workout.DumbbellStopgapB,
    WED: workout.DumbbellStopgapB if WORKOUT_SWITCH else workout.DumbbellStopgapA,
    FRI: workout.DumbbellStopgapA if WORKOUT_SWITCH else workout.DumbbellStopgapB,
    SUN: workout.DownDogYogaVinyasa,
}

AttiaLongevity = {
    MON: (
        workout.DownDogYogaStretch
        if _longevityRecoveryWeekSwitch()
        else workout.Zone2Cardio
    ),
    # TUE: (
    #     workout.Zone2Cardio if _longevityRecoveryWeekSwitch() else workout.Zone2Cardio
    # ),
    WED: (
        workout.Zone2Cardio
        if _longevityRecoveryWeekSwitch()
        else _longevityGetWednesday()
    ),
    # THU: (
    #     workout.Zone2Cardio if _longevityRecoveryWeekSwitch() else workout.Zone2Cardio
    # ),
    FRI: (
        workout.DownDogYogaStretch
        if _longevityRecoveryWeekSwitch()
        else workout.FiveThreeOneWorkout
    ),
    SAT: (
        workout.DownDogYogaStretch
        if _longevityRecoveryWeekSwitch()
        else workout.Zone2Cardio
    ),
    SUN: (
        workout.DownDogYogaVinyasa
        if _longevityRecoveryWeekSwitch()
        else workout.FiveThreeOneWorkout
    ),
}
