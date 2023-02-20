#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_youtube_analytics_custom import SourceYoutubeAnalyticsCustom

if __name__ == "__main__":
    source = SourceYoutubeAnalyticsCustom()
    launch(source, sys.argv[1:])
