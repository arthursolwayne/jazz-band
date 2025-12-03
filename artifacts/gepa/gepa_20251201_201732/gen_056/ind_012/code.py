
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1: Kick on 1, snare on 2, kick on 3, snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    
    # Hi-hat on every eighth (4 notes per bar)
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5)
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line with chromatic approaches
# Fm7 -> Bb7 -> Eb7 -> Am7 (Fm key)
# Roots and fifths with chromatic approaches

# Bar 2 (1.5 - 3.0s) - Fm7 -> Bb7 (F -> Bb -> B -> Eb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),   # B
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, Eb) - open voicing, resolve on the 4th beat

# Fm7: F, Ab, C, Eb
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=3.0),  # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging.
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F (1.5s), Ab (1.875s), Bb (2.25s), rest (2.625s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Bb7 -> Eb7 (Bb -> Eb -> F -> Ab)
bass_notes_bar3 = [
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=46, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),   # F
]

for note in bass_notes_bar3:
    bass.notes.append(note)

# Piano: Bb7 (Bb, D, F, Ab) - open voicing, resolve on the 4th beat
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=4.5),  # Ab
]

for note in piano_notes_bar3:
    piano.notes.append(note)

# Sax: Continue motif, resolve on the 4th beat
# Continue from Bb (2.625s) - now bring in F again on the 4th beat
sax_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # F
]

for note in sax_notes_bar3:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Eb7 -> Am7 (Eb -> Ab -> B -> C)
bass_notes_bar4 = [
    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=80, pitch=48, start=5.625, end=6.0),   # C
]

for note in bass_notes_bar4:
    bass.notes.append(note)

# Piano: Eb7 -> Am7 (Eb, G, Bb, Db) -> A, C, E, G
# Resolve on A on the 4th beat
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=46, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=6.0),  # Db
    pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=48, start=5.25, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=6.0),  # E
    pretty_midi.Note(velocity=100, pitch=52, start=5.25, end=6.0),  # G
]

for note in piano_notes_bar4:
    piano.notes.append(note)

# Sax: Bring back the motif but with an unexpected resolution
# F (4.5s), Ab (4.875s), C (5.25s), rest (5.625s)
sax_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=48, start=5.25, end=5.625),  # C
]

for note in sax_notes_bar4:
    sax.notes.append(note)

# Drums: Bar 3 and 4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 3 (3.0 - 4.5s)
drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5)
]

for note in drum_notes_bar3:
    drums.notes.append(note)

# Bar 4 (4.5 - 6.0s)
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]

for note in drum_notes_bar4:
    drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
# midi.write disabled
