
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5
for beat in [0, 2]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=beat * 0.375 + 0.125))
for beat in [1, 3]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375, end=beat * 0.375 + 0.125))
for beat in range(8):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.125, end=beat * 0.125 + 0.0625))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.5 + 0.375)),   # F
    (pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=1.875 + 0.375)), # F#
    (pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.25 + 0.375)),  # G
    (pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.625 + 0.375)), # E
    (pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=2.625 + 0.375)),  # G#
    (pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.0 + 0.375)),     # A
    (pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.375 + 0.375)), # A#
    (pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=3.75 + 0.375)),  # G#
    (pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.125 + 0.375)), # A
    (pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.5 + 0.375)),     # A#
    (pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=4.875 + 0.375)), # B
    (pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.25 + 0.375)),  # A#
    (pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=5.625 + 0.375)), # A
    (pretty_midi.Note(velocity=100, pitch=40, start=6.0, end=6.0 + 0.375)),     # G#
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords on 2 and 4, comp on 2 and 4
def add_piano_chord(time, chord):
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# F7 (F, A, C, E)
add_piano_chord(1.875, [79, 82, 84, 87])
# G7 (G, B, D, F)
add_piano_chord(3.0, [80, 83, 85, 79])
# A7 (A, C#, E, G)
add_piano_chord(4.125, [81, 85, 88, 82])
# B7 (B, D#, F#, A)
add_piano_chord(5.25, [83, 87, 90, 85])

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Original motif: F, G#, A, Bb
# Repeat with a half-step shift in the second iteration

def add_sax_note(time, pitch, duration):
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + duration))

# First motif: F, G#, A, Bb
add_sax_note(1.5, 79, 0.375)
add_sax_note(1.875, 82, 0.375)
add_sax_note(2.25, 83, 0.375)
add_sax_note(2.625, 81, 0.375)

# Second motif: E, F#, G, A
add_sax_note(3.0, 78, 0.375)
add_sax_note(3.375, 81, 0.375)
add_sax_note(3.75, 82, 0.375)
add_sax_note(4.125, 83, 0.375)

# Third motif: F, G#, A, Bb (return to original)
add_sax_note(4.5, 79, 0.375)
add_sax_note(4.875, 82, 0.375)
add_sax_note(5.25, 83, 0.375)
add_sax_note(5.625, 81, 0.375)

# Drums continue on bars 2-4
for beat in [0, 2, 3, 5, 6, 8, 9, 11]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=(1.5 + beat * 0.375), end=(1.5 + beat * 0.375) + 0.125))
for beat in [1, 3, 4, 6, 7, 9, 10, 12]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=(1.5 + beat * 0.375), end=(1.5 + beat * 0.375) + 0.125))
for beat in range(12):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=(1.5 + beat * 0.125), end=(1.5 + beat * 0.125) + 0.0625))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("waynes_moment.mid")
