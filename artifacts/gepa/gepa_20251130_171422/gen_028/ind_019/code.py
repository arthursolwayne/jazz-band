
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (walking line, chromatic approaches)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),   # F
    
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),   # D
    
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),   # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D7 - D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # D7 - G
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # D7 - Bb
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # D7 - C
    
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D7 - D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # D7 - G
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # D7 - Bb
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # D7 - C
    
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D7 - D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # D7 - G
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # D7 - Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # D7 - C
]

for note in piano_notes:
    piano.notes.append(note)

# Saxophone: Dante (melody, sparse and expressive)
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # D
    
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # D
    
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # D
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
