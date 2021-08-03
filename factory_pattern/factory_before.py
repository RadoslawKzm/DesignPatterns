"""
Basic video exporting example
"""

import pathlib
from abc import ABC, abstractmethod


class HighQualityVideoExporter:
    """High video exporting codec."""

    def prepare_export(self, video_data):
        print("Preparing video data for HQ export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in gihg quality format to {folder}.")


class LowQualityVideoExporter:
    """Low video exporting codec."""

    def prepare_export(self, video_data):
        print("Preparing video data for LQ export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in low quality format to {folder}.")


class MediumQualityVideoExporter:
    """Medium video exporting codec."""

    def prepare_export(self, video_data):
        print("Preparing video data for MQ export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in medium quality format to {folder}.")


class LowQualityAudioExporter:
    """Low quality audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for LQ export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in loq quality format to {folder}.")


class MediumQualityAudioExporter:
    """Medium quality audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for MQ export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in medium quality format to {folder}.")


class HighQualityAudioExporter:
    """High quality audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for HQ export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in high quality format to {folder}.")


def main() -> None:
    """Main function."""

    # read the desired export quality
    export_quality: str
    while True:
        export_quality = input("Enter desired output quality (low, medium, high): ")
        if export_quality in {"low", "medium", "high"}:
            break
        print(f"Unknown output quality option: {export_quality}.")

    # create the video and audio exporters
    if export_quality == "low":
        video_exporter = LowQualityVideoExporter()
        audio_exporter = LowQualityAudioExporter()
    elif export_quality == "medium":
        video_exporter = MediumQualityVideoExporter()
        audio_exporter = MediumQualityAudioExporter()
    else:
        # default: master quality
        video_exporter = HighQualityVideoExporter()
        audio_exporter = HighQualityAudioExporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    main()
