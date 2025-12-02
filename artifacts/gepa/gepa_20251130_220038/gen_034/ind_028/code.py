
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    # Bar 2 (1.5 - 3.0s): Fm7, walk down
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0),  # Db
    
    # Bar 3 (3.0 - 4.5s): Bb7, walk up
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375),  # Db
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # F
    
    # Bar 4 (4.5 - 6.0s): Fm7, walk down again
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=6.0),  # Db
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # Db
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # G
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # Db
]

for note in piano_notes:
    piano.notes.append(note)

# Tenor sax (Dante) - motif in Fm
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.5),  # Db
    
    # Bar 3 (3.0 - 4.5s) - leave it hanging
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.25),  # Db
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # Eb
    
    # Bar 4 (4.5 - 6.0s) - come back and finish it
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.5),  # Db
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
