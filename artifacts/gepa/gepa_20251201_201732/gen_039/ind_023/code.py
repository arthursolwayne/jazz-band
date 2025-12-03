
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
for i in range(4):
    time = i * 0.375
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.375 + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Roots and fifths, chromatic approaches, walking line in Fm
bass_notes = [
    (0.0, 37, 100),  # F2
    (0.375, 40, 100), # Ab2
    (0.75, 38, 100),  # G2
    (1.125, 37, 100), # F2
    (1.5, 37, 100),   # F2
    (1.875, 40, 100), # Ab2
    (2.25, 38, 100),  # G2
    (2.625, 37, 100), # F2
    (3.0, 37, 100),   # F2
    (3.375, 40, 100), # Ab2
    (3.75, 38, 100),  # G2
    (4.125, 37, 100), # F2
    (4.5, 37, 100),   # F2
    (4.875, 40, 100), # Ab2
    (5.25, 38, 100),  # G2
    (5.625, 37, 100)  # F2
]

for start, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=1.5 + start, end=1.5 + start + 0.125)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F Ab C Eb)
note = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.5 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.5 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.5 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + 0.375)
piano.notes.append(note)

# Bar 3: Bb7 (Bb D F Ab)
note = pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=1.875 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=1.875 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=1.875 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=1.875 + 0.375)
piano.notes.append(note)

# Bar 4: Eb7 (Eb G Bb D)
note = pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.25 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.25 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.25 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.25 + 0.375)
piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, G, F (motif is 1 bar, then rest on bar 2, and end on bar 4)

# Bar 2: Start motif
note = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.5 + 0.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=68, start=1.5 + 0.375, end=1.5 + 0.375 + 0.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 0.75, end=1.5 + 0.75 + 0.125)
sax.notes.append(note)

# Bar 3: Rest - leave it hanging
# No notes

# Bar 4: Finish motif
note = pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.25 + 0.125)
sax.notes.append(note)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.375 + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
