
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Setup
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Time constants
BAR_DURATION = 1.5  # 4/4 @ 160 BPM = 1.5 seconds
BEAT_DURATION = BAR_DURATION / 4
NOTE_DURATION = BEAT_DURATION / 2  # Half note = 2 beats

# Define instruments
drums = Instrument(program=Program(0), is_drum=True)
piano = Instrument(program=Program(0))
bass = Instrument(program=Program(33))
sax = Instrument(program=Program(64))

pm.instruments = [drums, piano, bass, sax]

# ============= DRUMS: LITTLE RAY =============
# Bar 1: Suspenseful, open
drums.notes.append(Note(38, 0.0, 0.5))  # Kick on 1
drums.notes.append(Note(38, 1.0, 0.5))  # Kick on 3

# Bar 2: Full energy, hihat on every 8th
for t in [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75]:
    drums.notes.append(Note(42, t, 0.25))  # Hihat
drums.notes.append(Note(38, 0.0, 0.5))  # Kick
drums.notes.append(Note(38, 1.0, 0.5))  # Kick
drums.notes.append(Note(26, 0.5, 0.5))  # Snare on 2
drums.notes.append(Note(26, 1.5, 0.5))  # Snare on 4

# ============= PIANO: DIANE =============
# Bar 2: Fm7 (F, Ab, C, Eb) open voicing
piano.notes.append(Note(64, 0.0, 0.5))  # F4
piano.notes.append(Note(61, 0.0, 0.5))  # Ab4
piano.notes.append(Note(67, 0.0, 0.5))  # C5
piano.notes.append(Note(65, 0.0, 0.5))  # Eb5

# Bar 3: Bb7 (Bb, D, F, Ab) open voicing
piano.notes.append(Note(59, 1.5, 0.5))  # Bb4
piano.notes.append(Note(62, 1.5, 0.5))  # D5
piano.notes.append(Note(64, 1.5, 0.5))  # F5
piano.notes.append(Note(61, 1.5, 0.5))  # Ab5

# Bar 4: Ab7 (Ab, C, Eb, Gb) open voicing
piano.notes.append(Note(61, 3.0, 0.5))  # Ab4
piano.notes.append(Note(67, 3.0, 0.5))  # C5
piano.notes.append(Note(65, 3.0, 0.5))  # Eb5
piano.notes.append(Note(63, 3.0, 0.5))  # Gb5)

# ============= BASS: MARCUS =============
# Bar 2: F, Gb (chromatic), Ab, A
bass.notes.append(Note(46, 0.0, 0.5))  # F3
bass.notes.append(Note(45, 0.5, 0.5))  # Gb3
bass.notes.append(Note(47, 1.0, 0.5))  # Ab3
bass.notes.append(Note(48, 1.5, 0.5))  # A3

# Bar 3: Bb, B, C, C#
bass.notes.append(Note(50, 1.5, 0.5))  # Bb3
bass.notes.append(Note(51, 2.0, 0.5))  # B3
bass.notes.append(Note(52, 2.5, 0.5))  # C4
bass.notes.append(Note(53, 3.0, 0.5))  # C#4

# Bar 4: Ab, A, Bb, B
bass.notes.append(Note(47, 3.0, 0.5))  # Ab3
bass.notes.append(Note(48, 3.5, 0.5))  # A3
bass.notes.append(Note(50, 4.0, 0.5))  # Bb3
bass.notes.append(Note(51, 4.5, 0.5))  # B3

# ============= SAX: DANTES' LINE =============
# Bar 2: First note of the motif — F# (Fm7 tension)
sax.notes.append(Note(66, 0.0, 0.75))  # F#4

# Bar 3: Half note rest — silence, tension
# Bar 4: Resolution — F (the root), but not for long
sax.notes.append(Note(64, 3.0, 0.5))  # F4

# Save the MIDI
pm.write("dante_intro.mid")
