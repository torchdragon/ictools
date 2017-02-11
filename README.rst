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

   list-pagerduty-incidents [--format=confluence|json] START END

**START**
   The earliest time to fetch messages from.  IOW, the starting date.

**END**
   The latest time to fetch messages from.  IOW, the ending date.

This utility writes the formatted messages to the standard output stream.


.. _scan_hipchat_room:

scan-hipchat-room
-----------------
::

   scan-hipchat-room [--format=confluence|json] START END ROOM [ROOM...]

**START**
   The earliest time to fetch messages from.  IOW, the starting date.

**END**
   The latest time to fetch messages from.  IOW, the ending date.

**ROOM**
   One or more room names to fetch messages from.

This utility writes the formatted messages to the standard output stream.


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
