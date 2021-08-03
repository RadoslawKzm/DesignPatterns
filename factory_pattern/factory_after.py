"""
Basic video exporting example
"""

import pathlib
from abc import ABC, abstractmethod


class VideoExporter(ABC):
    """Basic representation of video exporting codec."""

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares video data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the video data to a folder."""


class HighQualityVideoExporter(VideoExporter):
    """High video exporting codec."""

    def prepare_export(self, video_data):
        print("Preparing video data for HQ export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in gihg quality format to {folder}.")


class LowQualityVideoExporter(VideoExporter):
    """Low video exporting codec."""

    def prepare_export(self, video_data):
        print("Preparing video data for LQ export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in low quality format to {folder}.")


class MediumQualityVideoExporter(VideoExporter):
    """Medium video exporting codec."""

    def prepare_export(self, video_data):
        print("Preparing video data for MQ export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in medium quality format to {folder}.")


class AudioExporter(ABC):
    """Basic representation of audio exporting codec."""

    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepares audio data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder."""


class LowQualityAudioExporter(AudioExporter):
    """Low quality audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for LQ export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in loq quality format to {folder}.")


class MediumQualityAudioExporter(AudioExporter):
    """Medium quality audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for MQ export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in medium quality format to {folder}.")


class HighQualityAudioExporter(AudioExporter):
    """High quality audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for HQ export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in high quality format to {folder}.")


class ExporterFactory(ABC):
    """
    Factory that represents a combination of video and audio codecs.
    The factory doesn't maintain any of the instances it creates.
    """

    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter belonging to this factory."""

    @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        """Returns a new audio exporter belonging to this factory."""


class FastExporter(ExporterFactory):
    """Factory aimed at providing a high speed, lower quality export."""

    def get_video_exporter(self) -> VideoExporter:
        return LowQualityVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return LowQualityAudioExporter()


class MediumQualityExporter(ExporterFactory):
    """Factory aimed at providing a medium speed, medium quality export."""

    def get_video_exporter(self) -> VideoExporter:
        return MediumQualityVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return MediumQualityAudioExporter()


class HighQualityExporter(ExporterFactory):
    """Factory aimed at providing a low speed, high quality export."""

    def get_video_exporter(self) -> VideoExporter:
        return HighQualityVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return HighQualityAudioExporter()


def read_factory() -> ExporterFactory:
    """Constructs an exporter factory based on the user's preference."""

    factories = {
        "low": FastExporter(),
        "medium": MediumQualityExporter(),
        "high": HighQualityExporter(),
    }
    while True:
        export_quality = input("Enter desired output quality (low, medium, high): ")
        if export_quality not in factories:
            print(f"Unknown output quality option: {export_quality}.")
        return factories[export_quality]


def main(fac: ExporterFactory) -> None:
    """Main function."""

    # retrieve the exporters
    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    # create the factory
    factory = read_factory()

    # perform the exporting job
    main(factory)
