==========================
Incident Command Utilities
==========================

This is a simple toolkit of utilities that make my on-call life easier.

Tools
=====

.. _list_pagerduty_incidents:

list-pagerduty-incidents
------------------------
::

   list-pagerduty-incidents [options] START END

This utility retrieves incidents from PagerDuty for the time range and
writes them to standard output.  The **--format** option controls the
output format which is JSON by default.

Options
~~~~~~~
**--format=** *json* or *confluence*
   This optional parameter sets the format of the produced output.  The
   default for this option is to production JSON output.

**--verbose**, **-v**
   Increases the diagnostic verbosity.  By default, errors and warnings are
   displayed.  This option can be specified multiple times for increased
   effect.

**--quiet**, **-q**
   This option disables all diagnostic output.

Parameters
~~~~~~~~~~
**START**
   The starting date for the range of incidents to retrieve.

**END**
   The ending date for the range of incidents to retrieve.


.. _scan_hipchat_room:

scan-hipchat-room
-----------------
::

   scan-hipchat-room [options] START END ROOM [ROOM...]

This utility retrieves messages from one or more HipChat rooms for
the given time range.  The **--format** option controls the output
format which defaults to JSON.

Options
~~~~~~~
**--format=** *json* or *confluence*
   This optional parameter sets the format of the produced output.  The
   default for this option is to production JSON output.

**--verbose**, **-v**
   Increases the diagnostic verbosity.  By default, errors and warnings are
   displayed.  This option can be specified multiple times for increased
   effect.

**--quiet**, **-q**
   This option disables all diagnostic output.

Parameters
~~~~~~~~~~
**START**
   The starting date for the range of messages to retrieve.

**END**
   The ending date for the range of messages to retrieve.

**ROOM**
   One or more room names to fetch messages from.



Environment Variables
=====================

HIPCHAT_TOKEN
-------------
API token to use when talking to the `HipChat API`_.

PAGERDUTY_TOKEN
---------------
API token to use when talking to the `pagerduty API`_.

.. _HipChat API: https://developer.atlassian.com/hipchat/guide/hipchat-rest-api
.. _pagerduty API: https://v2.developer.pagerduty.com/v2/page/api-reference
   #!/Incidents/get_incidents
