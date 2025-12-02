
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus (bass): Walking line in Fm, chromatic approaches
bass_notes = [
    # Fm chord tones: F, Ab, D, Bb
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=3.0),  # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Diane (piano): 7th chords on 2 and 4, Fm7 on 2, Ab7 on 4
piano_notes = [
    # Fm7 (F, Ab, C, Db) on 2 (1.875 - 2.25)
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),
    # Ab7 (Ab, C, Eb, Gb) on 4 (2.625 - 3.0)
    pretty_midi.Note(velocity=90, pitch=63, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=58, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=59, start=2.625, end=3.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Dante (sax): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (Ab), Bb (B), D (Eb), F (Ab)
# Start on 1.5s, leave it hanging at 2.25s, come back and finish at 3.0s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.0),   # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=2.125, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.75), # F
    pretty_midi.Note(velocity=100, pitch=63, start=2.75, end=2.875), # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=2.875, end=3.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus (bass): Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),  # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Diane (piano): 7th chords on 2 and 4, Fm7 on 2, Ab7 on 4
piano_notes = [
    # Fm7 (F, Ab, C, Db) on 2 (3.375 - 3.75)
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=61, start=3.375, end=3.75),
    # Ab7 (Ab, C, Eb, Gb) on 4 (4.125 - 4.5)
    pretty_midi.Note(velocity=90, pitch=63, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=58, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=59, start=4.125, end=4.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Dante (sax): Continue the motif, but with variation
# Motif: F (Ab), Bb (B), D (Eb), F (Ab)
# Start on 3.0s, leave it hanging again
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=3.125, end=3.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=61, start=3.375, end=3.5),   # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=3.625, end=3.75), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.25), # F
    pretty_midi.Note(velocity=100, pitch=63, start=4.25, end=4.375), # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=4.375, end=4.5),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus (bass): Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0),  # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Diane (piano): 7th chords on 2 and 4, Fm7 on 2, Ab7 on 4
piano_notes = [
    # Fm7 (F, Ab, C, Db) on 2 (4.875 - 5.25)
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.25),
    # Ab7 (Ab, C, Eb, Gb) on 4 (5.625 - 6.0)
    pretty_midi.Note(velocity=90, pitch=63, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=58, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Dante (sax): Finish the motif
# Motif: F (Ab), Bb (B), D (Eb), F (Ab)
# Start on 4.5s, resolve it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=4.625, end=4.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.0),   # B
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.125),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=5.125, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.375), # F
    pretty_midi.Note(velocity=100, pitch=63, start=5.375, end=5.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=5.75), # F
    pretty_midi.Note(velocity=100, pitch=63, start=5.75, end=5.875), # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=5.875, end=6.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3 and 4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
