from celery import shared_task
from time import sleep
from celery_progress.backend import ProgressRecorder

@shared_task(bind=True)
def calculation_task(self, patient_infos):
    print(patient_infos)
    progress_recorder = ProgressRecorder(self)
    for i in range(5):
        sleep(0.5)
        progress_recorder.set_progress(i + 1, 5, f'On iteration {i}')
    return 'Done'