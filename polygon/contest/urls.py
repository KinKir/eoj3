from django.conf.urls import url

import polygon.contest.views as v

urlpatterns = [
    url(r'^$', v.ContestList.as_view(), name='contest_list'),
    url(r'^create/$', v.ContestCreate.as_view(), name='contest_create'),
    url(r'^(?P<pk>\d+)/meta/$', v.ContestEdit.as_view(), name='contest_meta'),
    url(r'^(?P<pk>\d+)/statement/drop/$', v.ContestDropStatement.as_view(), name='contest_drop_statement'),
    url(r'^(?P<pk>\d+)/access/$', v.ContestAccessManage.as_view(), name='contest_access_manage'),
    url(r'^(?P<pk>\d+)/authors/$', v.ContestAuthorsManage.as_view(), name='contest_author_manage'),
    url(r'^(?P<pk>\d+)/volunteers/$', v.ContestVolunteersManage.as_view(), name='contest_volunteer_manage'),
    url(r'^(?P<pk>\d+)/problems/$', v.ContestProblemManage.as_view(), name='contest_problem_manage'),
    url(r'^(?P<pk>\d+)/problems/create/$', v.ContestProblemCreate.as_view(), name='contest_problem_create'),
    url(r'^(?P<pk>\d+)/problems/reorder/$', v.ContestProblemReorder.as_view(), name='contest_problem_reorder'),
    url(r'^(?P<pk>\d+)/problems/readjust/$', v.ContestProblemChangeWeight.as_view(),
        name='contest_problem_readjust_point'),
    url(r'^(?P<pk>\d+)/problems/identifier/change/$', v.ContestProblemChangeIdentifier.as_view(),
        name='contest_problem_readjust_identifier'),
    url(r'^(?P<pk>\d+)/problems/delete/$', v.ContestProblemDelete.as_view(), name='contest_problem_delete'),
    url(r'^(?P<pk>\d+)/invitation/$', v.ContestInvitationList.as_view(), name='contest_invitation'),
    url(r'^(?P<pk>\d+)/invitation/create/$', v.ContestInvitationCreate.as_view(),
        name='contest_invitation_create'),
    url(r'^(?P<pk>\d+)/invitation/(?P<invitation_pk>\d+)/delete/$', v.ContestInvitationDelete.as_view(),
        name='contest_invitation_delete'),
    url(r'^(?P<pk>\d+)/invitation/(?P<invitation_pk>\d+)/assign/$', v.ContestInvitationAssign.as_view(),
        name='contest_invitation_assign'),
    url(r'^(?P<pk>\d+)/invitation/download/$', v.ContestInvitationCodeDownload.as_view(),
        name='contest_invitation_download'),
    url(r'^(?P<pk>\d+)/participants/$', v.ContestParticipantList.as_view(), name='contest_participant'),
    url(r'^(?P<pk>\d+)/participants/star/auto/$', v.ContestParticipantAutoStarView.as_view(), name='contest_participant_auto_star'),
    url(r'^(?P<pk>\d+)/participants/(?P<participant_pk>\d+)/change/$',
        v.ContestParticipantCommentUpdate.as_view(), name='contest_participant_change'),
    url(r'^(?P<pk>\d+)/participants/(?P<participant_pk>\d+)/star/$', v.ContestParticipantStarToggle.as_view(),
        name='contest_participant_star_toggle'),
    url(r'^(?P<pk>\d+)/participants/(?P<participant_pk>\d+)/ip/clear/$', v.ContestParticipantClearIP.as_view(),
        name='contest_participant_clear_ip'),
    url(r'^(?P<pk>\d+)/participants/create/$', v.ContestParticipantCreate.as_view(),
        name='contest_participant_create'),
    url(r'^(?P<pk>\d+)/participants/download/$', v.ContestParticipantsNoteDownload.as_view(),
        name='contest_participant_download'),
    url(r'^(?P<pk>\d+)/participants/import/$', v.ContestParticipantFromActivity.as_view(),
        name='contest_participant_activity'),
    url(r'^(?P<pk>\d+)/ghost/import/$', v.ContestGhostRecordImport.as_view(), name='ghost_import'),
    url(r'^(?P<pk>\d+)/status/$', v.ContestStatusBackend.as_view(), name='contest_status'),
    url(r'^(?P<pk>\d+)/rejudge/$', v.RejudgeContestProblemSubmission.as_view(), name='contest_rejudge'),
    url(r'^(?P<pk>\d+)/system-test/', v.ContestSystemTestView.as_view(), name='contest_system_test'),
    url(r'^(?P<pk>\d+)/disable/(?P<participant_pk>\d+)/$', v.ContestAccountDisable.as_view(), name='contest_account_disable'),
    url(r'^(?P<pk>\d+)/anticheat/$', v.ContestAntiCheatStatus.as_view(), name='contest_anti_cheat_status'),
    url(r'^(?P<pk>\d+)/anticheat/start/$', v.ContestAntiCheatAnalysisStart.as_view(), name='contest_anti_cheat_start'),
    url(r'^(?P<pk>\d+)/anticheat/report/(?P<submission_pk>\d+)/$', v.ContestAntiCheatReport.as_view(), name='contest_anti_cheat_report'),
]
