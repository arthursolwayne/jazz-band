
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Constants
BPM = 160
TIME_SIGNATURE = (4, 4)
DURATION = 4
TIME_PER_BAR = (60.0 / BPM) * 4
D_BAR = 60  # D4
M7 = 70   # Bb4
F7 = 77   # F4
A7 = 82   # A4
G7 = 78   # G4
C7 = 72   # C4
B7 = 73   # B4

# Setup piano
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]
pm.tempo_changes = [pretty_midi.TempoChange(tempo=BPM, time=0)]

# Drums (Bar 1: Kick on 1 & 3, Snare on 2 & 4, Hihat on every 8th)
drum_program = Program(instrument=pretty_midi.instrument_name_to_program('Acoustic Grand Piano'))
drum_instrument = Instrument(program=drum_program, is_drum=True)
drum_instrument.notes = [
    Note(velocity=90, start=0.0, end=0.375, pitch=36),  # Kick on 1
    Note(velocity=80, start=0.75, end=1.125, pitch=38),  # Snare on 2
    Note(velocity=60, start=0.0, end=1.5, pitch=42),     # Hihat on every 8th
    Note(velocity=60, start=0.375, end=1.875, pitch=42),
    Note(velocity=60, start=0.75, end=2.25, pitch=42),
    Note(velocity=60, start=1.125, end=2.625, pitch=42),
    Note(velocity=60, start=1.5, end=3.0, pitch=42),
    Note(velocity=60, start=1.875, end=3.375, pitch=42),
    Note(velocity=60, start=2.25, end=3.75, pitch=42),
    Note(velocity=60, start=2.625, end=4.125, pitch=42),

    # Bar 2: Kick on 1 & 3 again
    Note(velocity=90, start=4.125, end=4.5, pitch=36),
    Note(velocity=90, start=5.5, end=5.875, pitch=36),
    # Snare on 2 & 4
    Note(velocity=80, start=4.5, end=4.875, pitch=38),
    Note(velocity=80, start=6.0, end=6.375, pitch=38),
    # Hihat 8ths
    Note(velocity=60, start=4.125, end=5.5, pitch=42),
    Note(velocity=60, start=4.5, end=5.875, pitch=42),
    Note(velocity=60, start=4.875, end=6.25, pitch=42),
    Note(velocity=60, start=5.25, end=6.625, pitch=42),
    Note(velocity=60, start=5.625, end=6.0, pitch=42),
]

pm.instruments.append(drum_instrument)

# Bass: Walking line, chromatic approaches, D minor key
bass_program = Program(instrument=pretty_midi.instrument_name_to_program('Double Bass'))
bass_instrument = Instrument(program=bass_program)
bass_instrument.notes = [
    Note(velocity=70, start=4.125, end=4.375, pitch=49),  # D3
    Note(velocity=70, start=4.375, end=4.625, pitch=50),  # Eb3
    Note(velocity=70, start=4.625, end=4.875, pitch=51),  # E3
    Note(velocity=70, start=4.875, end=5.125, pitch=48),  # C3
    Note(velocity=70, start=5.125, end=5.375, pitch=50),  # Eb3
    Note(velocity=70, start=5.375, end=5.625, pitch=51),  # E3
    Note(velocity=70, start=5.625, end=5.875, pitch=52),  # F3
    Note(velocity=70, start=5.875, end=6.125, pitch=48),  # C3
]

pm.instruments.append(bass_instrument)

# Piano: Dm7 comp on 2 and 4
piano_program = Program(instrument=pretty_midi.instrument_name_to_program('Acoustic Grand Piano'))
piano_instrument = Instrument(program=piano_program)
piano_instrument.notes = [
    # Bar 2: Dm7 on 2
    Note(velocity=90, start=4.5, end=4.75, pitch=D_BAR + 12),  # D4
    Note(velocity=90, start=4.5, end=4.75, pitch=M7),           # Bb4
    Note(velocity=90, start=4.5, end=4.75, pitch=F7),           # F4
    Note(velocity=90, start=4.5, end=4.75, pitch=A7),           # A4
    # Bar 3: Dm7 on 4
    Note(velocity=90, start=5.5, end=5.75, pitch=D_BAR + 12),
    Note(velocity=90, start=5.5, end=5.75, pitch=M7),
    Note(velocity=90, start=5.5, end=5.75, pitch=F7),
    Note(velocity=90, start=5.5, end=5.75, pitch=A7),
]

pm.instruments.append(piano_instrument)

# Tenor Sax: Short motif, D minor, emotional, with space
sax_program = Program(instrument=pretty_midi.instrument_name_to_program('Soprano Sax'))
sax_instrument = Instrument(program=sax_program)
sax_instrument.notes = [
    Note(velocity=100, start=4.125, end=4.375, pitch=D_BAR + 12),  # D4
    Note(velocity=100, start=4.625, end=4.875, pitch=G7),          # G4
    Note(velocity=100, start=5.125, end=5.375, pitch=A7),          # A4
    Note(velocity=100, start=5.625, end=5.875, pitch=C7),          # C4
    Note(velocity=100, start=6.125, end=6.375, pitch=D_BAR + 12),  # D4
    Note(velocity=100, start=6.625, end=6.875, pitch=G7),          # G4
    Note(velocity=100, start=7.125, end=7.375, pitch=A7),          # A4
    # Leave the final note open
]

pm.instruments.append(sax_instrument)

# Save the MIDI file
pm.write('jazz_intro_wayne.mid')
