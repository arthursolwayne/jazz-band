
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # Ab (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # D (root of Bb7)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # D
]
for note in piano_notes_bar2:
    piano.notes.append(note)

# Sax: Motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes_bar2 = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875),  # D (first note)
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # D (rest, leave it hanging)
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),  # C (resolve)
]
for note in sax_notes_bar2:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes_bar3 = [
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),  # Ab (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),  # F (root of Fm)
]
for note in bass_notes_bar3:
    bass.notes.append(note)

# Piano: Bb7 (Bb, D, F, Ab)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # Ab
]
for note in piano_notes_bar3:
    piano.notes.append(note)

# Sax: Motif variation, continue the story
sax_notes_bar3 = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),  # C
]
for note in sax_notes_bar3:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes_bar4 = [
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D (root of Bb7)
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=39, start=5.25, end=5.625),  # Eb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=36, start=5.625, end=6.0),  # Bb (root of Fm7)
]
for note in bass_notes_bar4:
    bass.notes.append(note)

# Piano: Fm7 (F, Ab, C, D)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # D
]
for note in piano_notes_bar4:
    piano.notes.append(note)

# Sax: Motif resolution, complete the story
sax_notes_bar4 = [
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),  # D (resolution)
]
for note in sax_notes_bar4:
    sax.notes.append(note)

# Drums: Bar 3 (4.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0)
]
for note in drum_notes_bar3:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
