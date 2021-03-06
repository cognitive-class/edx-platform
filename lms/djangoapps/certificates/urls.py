"""
URLs for the certificates app.
"""

from django.conf.urls import patterns, url
from django.conf import settings

from certificates import views

urlpatterns = patterns(
    '',

    # Certificates HTML view end point to render web certs by user and course
    url(
        r'^user/(?P<user_id>[^/]*)/course/{course_id}'.format(course_id=settings.COURSE_ID_PATTERN),
        views.render_html_view,
        name='html_view'
    ),

    # Certificates HTML view end point to render web certs by certificate_uuid
    url(
        r'^(?P<certificate_uuid>[0-9a-f]{32})$',
        views.render_cert_by_uuid,
        name='render_cert_by_uuid'
    ),

    # Certificate HTML view end point to render Moodle web certs by certificate_uuid
    url(
        r'^moodle/(?P<moodle_cert_code>[0-9A-Za-z]+)-(?P<time_created>[0-9A-Za-z]+)-(?P<cert_date>[0-9A-Za-z]+)',
        views.render_moodle_html_view,
        name="render_moodle_html_view"
    ),

    # End-points used by student support
    # The views in the lms/djangoapps/support use these end-points
    # to retrieve certificate information and regenerate certificates.
    url(r'search', views.search_by_user, name="search"),
    url(r'regenerate', views.regenerate_certificate_for_user, name="regenerate_certificate_for_user"),
)


if settings.FEATURES.get("ENABLE_OPENBADGES", False):
    urlpatterns += (
        url(
            r'^badge_share_tracker/{}/(?P<network>[^/]+)/(?P<student_username>[^/]+)/$'.format(
                settings.COURSE_ID_PATTERN
            ),
            views.track_share_redirect,
            name='badge_share_tracker'
        ),
    )
