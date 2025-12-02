
import pretty_midi
from pretty_midi import Note, Instrument

# Constants
BPM = 160
TEMPO = BPM * (60 / 6)  # 160 BPM = 160 beats per minute, 6 seconds for 4 bars
NOTE_DURATION = 0.375  # Each beat is 0.375s at 160 BPM
BAR_DURATION = 1.5     # 4/4 time, 6 seconds for 4 bars
TIME_SIGNATURE = (4, 4)

# Key: F minor
KEY = 'Fm'

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=TEMPO)
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Create instruments
drums = pretty_midi.Instrument(program=10, is_drum=True)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

pm.instruments = [drums, bass, piano, sax]

# ------------------------------
# BAR 1: Little Ray's Drums
# ------------------------------
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time: 0.0 to 1.5s

# Kick: 0.0, 0.75
drums.notes.append(Note(36, 100, 0.0, 0.375))
drums.notes.append(Note(36, 100, 0.75, 1.125))

# Snare: 0.375, 1.125
drums.notes.append(Note(38, 100, 0.375, 0.75))
drums.notes.append(Note(38, 100, 1.125, 1.5))

# Hi-Hat: every eighth note
hi_hat_notes = [Note(42, 90, i * 0.375, i * 0.375 + 0.125) for i in range(0, int(1.5 / 0.375))]
drums.notes.extend(hi_hat_notes)

# ------------------------------
# BAR 2: Start of the melody (Sax)
# ------------------------------
# Time: 1.5 to 3.0s

# Fm chord tones: F, Ab, D, G (Fm7)
# Unique motif: F - Ab - D - G (all in 16th notes)
# Then rest for a beat (suspense)

sax_notes = [
    Note(71, 100, 1.5, 1.625),   # F (tenor sax: F is C4 in MIDI, but we're shifting for tenor)
    Note(66, 100, 1.625, 1.75),  # Ab
    Note(69, 100, 1.75, 1.875),  # D
    Note(71, 100, 1.875, 2.0),   # G
    Note(71, 100, 2.0, 2.125),   # F again (repetition with tension)
    Note(71, 100, 2.125, 2.25),  # F again
    Note(71, 100, 2.25, 2.375),  # F
    Note(71, 100, 2.375, 2.5),   # F
    Note(71, 100, 2.5, 2.625),   # F
    Note(71, 100, 2.625, 2.75),  # F
    Note(71, 100, 2.75, 2.875),  # F
    Note(71, 100, 2.875, 3.0),   # F (end of bar)
]

sax.notes.extend(sax_notes)

# ------------------------------
# BAR 2: Bass Line (Marcus)
# ------------------------------
# Walking line: F - G - Ab - A - Bb - B - C - D
# Chromatic approach to G
# Time: 1.5 to 3.0s

bass_notes = [
    Note(53, 80, 1.5, 1.625),   # F
    Note(55, 80, 1.625, 1.75),  # G
    Note(54, 80, 1.75, 1.875),  # Ab
    Note(56, 80, 1.875, 2.0),   # A
    Note(57, 80, 2.0, 2.125),   # Bb
    Note(58, 80, 2.125, 2.25),  # B
    Note(59, 80, 2.25, 2.375),  # C
    Note(60, 80, 2.375, 2.5),   # D
    Note(60, 80, 2.5, 2.625),   # D
    Note(60, 80, 2.625, 2.75),  # D
    Note(60, 80, 2.75, 2.875),  # D
    Note(60, 80, 2.875, 3.0),   # D
]

bass.notes.extend(bass_notes)

# ------------------------------
# BAR 2: Piano (Diane) - 7th chords on 2 and 4
# ------------------------------
# Fm7 = F, Ab, C, D
# Time: 1.5 to 3.0s

piano_notes = [
    Note(66, 80, 1.875, 2.0),   # Ab
    Note(60, 80, 1.875, 2.0),   # C
    Note(69, 80, 1.875, 2.0),   # D
    Note(53, 80, 1.875, 2.0),   # F
    Note(66, 80, 2.625, 2.75),  # Ab
    Note(60, 80, 2.625, 2.75),  # C
    Note(69, 80, 2.625, 2.75),  # D
    Note(53, 80, 2.625, 2.75),  # F
]

piano.notes.extend(piano_notes)

# ------------------------------
# BAR 3-4: Sax continues with small variations
# ------------------------------
# Time: 3.0 to 6.0s
# We'll repeat the motif but slightly vary the rhythm to build tension

# Bar 3: Motif again, with slight rhythm change
sax_notes = [
    Note(71, 100, 3.0, 3.125),   # F
    Note(66, 100, 3.125, 3.25),  # Ab
    Note(69, 100, 3.25, 3.375),  # D
    Note(71, 100, 3.375, 3.5),   # G
    Note(71, 100, 3.5, 3.625),   # F
    Note(71, 100, 3.625, 3.75),  # F
    Note(71, 100, 3.75, 3.875),  # F
    Note(71, 100, 3.875, 4.0),   # F
    Note(71, 100, 4.0, 4.125),   # F
    Note(71, 100, 4.125, 4.25),  # F
    Note(71, 100, 4.25, 4.375),  # F
    Note(71, 100, 4.375, 4.5),   # F
]

sax.notes.extend(sax_notes)

# Bar 4: Bass continues the walking line
bass_notes = [
    Note(53, 80, 3.0, 3.125),   # F
    Note(55, 80, 3.125, 3.25),  # G
    Note(54, 80, 3.25, 3.375),  # Ab
    Note(56, 80, 3.375, 3.5),   # A
    Note(57, 80, 3.5, 3.625),   # Bb
    Note(58, 80, 3.625, 3.75),  # B
    Note(59, 80, 3.75, 3.875),  # C
    Note(60, 80, 3.875, 4.0),   # D
    Note(60, 80, 4.0, 4.125),   # D
    Note(60, 80, 4.125, 4.25),  # D
    Note(60, 80, 4.25, 4.375),  # D
    Note(60, 80, 4.375, 4.5),   # D
]

bass.notes.extend(bass_notes)

# Bar 4: Piano continues comping on 2 and 4
piano_notes = [
    Note(66, 80, 3.375, 3.5),   # Ab
    Note(60, 80, 3.375, 3.5),   # C
    Note(69, 80, 3.375, 3.5),   # D
    Note(53, 80, 3.375, 3.5),   # F
    Note(66, 80, 4.125, 4.25),  # Ab
    Note(60, 80, 4.125, 4.25),  # C
    Note(69, 80, 4.125, 4.25),  # D
    Note(53, 80, 4.125, 4.25),  # F
]

piano.notes.extend(piano_notes)

# Save to MIDI file
pm.write('jazz_intro.mid')
print("MIDI file 'jazz_intro.mid' has been created.")
