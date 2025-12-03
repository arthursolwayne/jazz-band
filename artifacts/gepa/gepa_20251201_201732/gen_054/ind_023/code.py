
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

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line in Fm, roots and fifths with chromatic approaches
# Fm = F, Ab, D, C, Bb, G, Eb, etc. Walking line in D2-G2 (MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # Ab (Eb2)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # D (G2)
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # C (F2)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=3.0),  # F (C4)
    pretty_midi.Note(velocity=90, pitch=51, start=1.5, end=3.0),  # Ab (A3)
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=3.0),  # C (D4)
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=3.0),  # D (E4)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, haunting and incomplete
# Start with a descending idea, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # Eb (E4)
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # D (D4)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # Eb (E4)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line continuing
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),  # Bb (Eb2)
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75),  # Ab (A3)
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),  # D (G2)
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),  # C (F2)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Next chord: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=4.5),  # Bb (Bb3)
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=4.5),  # D (C4)
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=4.5),  # F (C4)
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=4.5),  # Ab (A3)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif, leave it unresolved
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # Bb (Bb4)
    pretty_midi.Note(velocity=100, pitch=56, start=3.375, end=3.75),  # Ab (Ab4)
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.125),  # G (G4)
    pretty_midi.Note(velocity=100, pitch=56, start=4.125, end=4.5),  # Ab (Ab4)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Same pattern
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line continuing
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.875),  # Eb (G#2)
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25),  # Ab (A3)
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),  # D (G2)
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),  # C (F2)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Next chord: Eb7 (Eb, G, Bb, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=49, start=4.5, end=6.0),  # Eb (Eb3)
    pretty_midi.Note(velocity=90, pitch=51, start=4.5, end=6.0),  # G (G3)
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=6.0),  # Bb (Bb3)
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=6.0),  # D (C4)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Complete the motif, end on a question
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875),  # B (B4)
    pretty_midi.Note(velocity=100, pitch=56, start=4.875, end=5.25),  # Ab (Ab4)
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=56, start=5.625, end=6.0),  # Ab (Ab4)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Same pattern
for note in drum_notes:
    drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
