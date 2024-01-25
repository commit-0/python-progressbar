from datetime import date

from .__about__ import __author__, __version__
from .bar import DataTransferBar, NullBar, ProgressBar
from .base import UnknownLength
from .multi import MultiBar, SortKey
from .shortcuts import progressbar
from .terminal.stream import LineOffsetStreamWrapper
from .utils import len_color, streams
from .algorithms import ExponentialMovingAverage, SmoothingAlgorithm, DoubleExponentialMovingAverage
from .widgets import (
    ETA,
    AbsoluteETA,
    AdaptiveETA,
    SmoothingETA,
    AdaptiveTransferSpeed,
    AnimatedMarker,
    Bar,
    BouncingBar,
    Counter,
    CurrentTime,
    DataSize,
    DynamicMessage,
    FileTransferSpeed,
    FormatCustomText,
    FormatLabel,
    FormatLabelBar,
    GranularBar,
    JobStatusBar,
    MultiProgressBar,
    MultiRangeBar,
    Percentage,
    PercentageLabelBar,
    ReverseBar,
    RotatingMarker,
    SimpleProgress,
    Timer,
    Variable,
    VariableMixin,
)
from .algorithms import ExponentialMovingAverage, SmoothingAlgorithm

__date__ = str(date.today())
__all__ = [
    'progressbar',
    'len_color',
    'streams',
    'Timer',
    'ETA',
    'AdaptiveETA',
    'AbsoluteETA',
    'SmoothingETA',
    'SmoothingAlgorithm',
    'ExponentialMovingAverage',
    'DoubleExponentialMovingAverage',
    'DataSize',
    'FileTransferSpeed',
    'AdaptiveTransferSpeed',
    'AnimatedMarker',
    'Counter',
    'Percentage',
    'FormatLabel',
    'SimpleProgress',
    'Bar',
    'ReverseBar',
    'BouncingBar',
    'UnknownLength',
    'ProgressBar',
    'DataTransferBar',
    'RotatingMarker',
    'VariableMixin',
    'MultiRangeBar',
    'MultiProgressBar',
    'GranularBar',
    'FormatLabelBar',
    'PercentageLabelBar',
    'Variable',
    'DynamicMessage',
    'FormatCustomText',
    'CurrentTime',
    'NullBar',
    '__author__',
    '__version__',
    'LineOffsetStreamWrapper',
    'MultiBar',
    'SortKey',
    'JobStatusBar',
]
