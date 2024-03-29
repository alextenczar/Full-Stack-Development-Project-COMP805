from django.urls import path
from django.conf.urls import url
import scoring.views
from scoring.views import *
from scoring.views.remove_all_data import remove_all_data
from scoring.views.display.display_top_projects import display_top_projects

#from .views import HomeListView

urlpatterns = [
    # url(r'add/score/$', add_score, name='add_score'),
    # url(r'^edit/$', edit_score, name='edit_score'),
    path('', add_score, name='add_score'),
    path('display_judges/', display_judges, name='display_judges'),
    path('display_projects/', display_projects, name='display_projects'),
    path('display_judge_assignments/', display_judge_assignments, name='display_judge_assignments'),
    path('display_students/', display_students, name='display_students'),
    path('import_file/', import_file, name='import_file'),
    path('export_judge_assignment/', export_judge_assignment, name='export_judge_assignment'),
    path('remove_all_data/', remove_all_data, name='remove_all_data'),
    path('calculate_scores/', calculate_scores, name='calculate_scores'),
    path('display_top_projects/', display_top_projects, name='display_top_projects')
]
