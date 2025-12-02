
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus on bass: walking line in D, chromatic approaches
bass_notes = [
    # D (2nd octave) on 1
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    # F# (chromatic approach) on 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),
    # A on 3
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),
    # C# (chromatic approach) on 4
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # D7 on 1
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),
    # F#7 on 2
    pretty_midi.Note(velocity=95, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=85, pitch=74, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=72, start=1.875, end=2.25),
    # A7 on 3
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),
    pretty_midi.Note(velocity=85, pitch=76, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.625),
    # C#7 on 4
    pretty_midi.Note(velocity=95, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),
    pretty_midi.Note(velocity=85, pitch=78, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=76, start=2.625, end=3.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: short motif, make it sing - D, F#, A, D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.125),
    pretty_midi.Note(velocity=110, pitch=67, start=2.125, end=2.5),
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.875),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus on bass: walking line in D, chromatic approaches
bass_notes = [
    # D (2nd octave) on 1
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),
    # F# (chromatic approach) on 2
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),
    # A on 3
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),
    # C# (chromatic approach) on 4
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # D7 on 1
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),
    # F#7 on 2
    pretty_midi.Note(velocity=95, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=85, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75),
    # A7 on 3
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),
    pretty_midi.Note(velocity=85, pitch=76, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=4.125),
    # C#7 on 4
    pretty_midi.Note(velocity=95, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),
    pretty_midi.Note(velocity=85, pitch=78, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=76, start=4.125, end=4.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Little Ray on drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus on bass: walking line in D, chromatic approaches
bass_notes = [
    # D (2nd octave) on 1
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),
    # F# (chromatic approach) on 2
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),
    # A on 3
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),
    # C# (chromatic approach) on 4
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # D7 on 1
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=85, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),
    # F#7 on 2
    pretty_midi.Note(velocity=95, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=85, pitch=74, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25),
    # A7 on 3
    pretty_midi.Note(velocity=95, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),
    pretty_midi.Note(velocity=85, pitch=76, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.625),
    # C#7 on 4
    pretty_midi.Note(velocity=95, pitch=69, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0),
    pretty_midi.Note(velocity=85, pitch=78, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=76, start=5.625, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: variation of the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.125),
    pretty_midi.Note(velocity=110, pitch=67, start=5.125, end=5.5),
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.875),
]

for note in sax_notes:
    sax.notes.append(note)

# Little Ray on drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
