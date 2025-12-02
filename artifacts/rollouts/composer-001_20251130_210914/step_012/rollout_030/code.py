
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * 0.375
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62),    # D
    (1.875, 63),  # Eb
    (2.25, 64),   # E
    (2.625, 65),  # F
    (3.0, 67),    # G
    (3.375, 66),  # F#
    (3.75, 65),   # F
    (4.125, 64),  # E
    (4.5, 62),    # D
    (4.875, 61),  # C
    (5.25, 60),   # Bb
    (5.625, 59),  # B
    (6.0, 62)     # D
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Bar 2 (1.5s - 2.25s): Dm7 (D F A C)
note = pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25)
piano.notes.append(note)

# Bar 3 (2.25s - 3.0s): skip
# Bar 4 (3.0s - 3.75s): Dm7 again
note = pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75)
piano.notes.append(note)

# Sax: motif, make it sing
# Start it, leave it hanging, come back and finish it

# Bar 2 (1.5s - 2.25s): motif
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25)
sax.notes.append(note)

# Bar 3 (2.25s - 3.0s): silence
# Bar 4 (3.0s - 3.75s): return and finish the motif
note = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75)
sax.notes.append(note)

# Drums: continue same pattern
for beat in range(4, 8):
    time = (beat * 0.375) + 1.5
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
