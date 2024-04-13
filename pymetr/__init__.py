# pymetr/__init__.py

# Update the __all__ list to include specific classes you want to expose.
__all__ = [
    'Instrument', 'Subsystem', 'Sources', 'Trace',
    'SelectProperty', 'SwitchProperty', 'ValueProperty', 'DataProperty', 'DataBlockProperty'
]

try:
    from .instrument import Instrument, Subsystem, Sources, Trace
    from .properties import SelectProperty, SwitchProperty, ValueProperty, DataProperty, DataBlockProperty
except ImportError as e:
    print(f"Failed to import within pymetr: {e}")