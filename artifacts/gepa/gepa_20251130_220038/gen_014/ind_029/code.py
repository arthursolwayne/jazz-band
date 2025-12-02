
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
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

# Bass line - walking line in D, chromatic approaches
bass_notes = [
    # Bar 2: D - C# - Eb - E
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25), # C#
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on 2 and 4
    pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=95, pitch=71, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=95, pitch=72, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=95, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=2.625, end=3.0),   # F#
    pretty_midi.Note(velocity=95, pitch=71, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=95, pitch=72, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=95, pitch=62, start=2.625, end=3.0),   # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - motif: D - F# - Eb - E (1.5 - 1.875), then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),   # E
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line - walking line in D, chromatic approaches
bass_notes = [
    # Bar 3: F# - G - A - Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),   # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: D7 on 2 and 4
    pretty_midi.Note(velocity=95, pitch=67, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=95, pitch=71, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=95, pitch=72, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=95, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=4.125, end=4.5),   # F#
    pretty_midi.Note(velocity=95, pitch=71, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=95, pitch=72, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=95, pitch=62, start=4.125, end=4.5),   # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - motif: D - F# - Eb - E (3.0 - 3.375), then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5),   # E
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line - walking line in D, chromatic approaches
bass_notes = [
    # Bar 4: Bb - B - C# - D
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=73, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=90, pitch=61, start=5.25, end=5.625),  # C#
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),   # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: D7 on 2 and 4
    pretty_midi.Note(velocity=95, pitch=67, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=95, pitch=71, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=95, pitch=72, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=95, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=5.625, end=6.0),   # F#
    pretty_midi.Note(velocity=95, pitch=71, start=5.625, end=6.0),   # A
    pretty_midi.Note(velocity=95, pitch=72, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=95, pitch=62, start=5.625, end=6.0),   # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - motif: D - F# - Eb - E (4.5 - 4.875), then finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),   # E
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: kick=36, snare=38, hihat=42
# Bar 3: 3.0 - 4.5s
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.875),
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

# Bar 4: 4.5 - 6.0s
# Drums: kick on 1 and 3, snare on 2 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
