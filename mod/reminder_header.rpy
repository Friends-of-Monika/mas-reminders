init -990 python in mas_submod_utils:
    Submod(
        author="Friends of Monika",
        name="Timers and Reminders",
        description="Allows Monika to set up custom reminders and timers for the player",
        version="1.0.1"
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Timers and Reminders",
            user_name="friends-of-monika",
            repository_name="mas-reminders",
            extraction_depth=3
        )