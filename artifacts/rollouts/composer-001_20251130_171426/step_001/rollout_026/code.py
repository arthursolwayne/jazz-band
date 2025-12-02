
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: All instruments join in (1.5 - 3.0s)
# Sax melody - short motif, make it sing
# Dm7 - F, A, C, D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Marcus: Walking bass line in Dm (1.5 - 3.0s)
# Dm - D, F, A, C (chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=70, pitch=63, start=1.75, end=2.0),  # Eb (approach to F)
    pretty_midi.Note(velocity=70, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=70, pitch=67, start=2.25, end=2.5),  # G (approach to A)
    pretty_midi.Note(velocity=70, pitch=69, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=70, pitch=70, start=2.75, end=3.0),  # Bb (approach to C)
    pretty_midi.Note(velocity=70, pitch=71, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=70, pitch=72, start=3.25, end=3.5),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4 (1.5 - 3.0s)
# Dm7 on beat 2
piano_notes_2 = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # A
]
# Dm7 on beat 4
piano_notes_4 = [
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # A
]

for note in piano_notes_2 + piano_notes_4:
    piano.notes.append(note)

# Bar 3 and 4: Repeat or slightly vary
# Repeat sax motif at 3.0 - 4.5s
for note in sax_notes:
    note.start += 1.5
    note.end += 1.5
    sax.notes.append(note)

# Repeat bass line at 3.0 - 4.5s
for note in bass_notes:
    note.start += 1.5
    note.end += 1.5
    bass.notes.append(note)

# Repeat piano chords at 3.0 - 4.5s
for note in piano_notes_2 + piano_notes_4:
    note.start += 1.5
    note.end += 1.5
    piano.notes.append(note)

# Repeat drums at 3.0 - 4.5s
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
