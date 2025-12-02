
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=70, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=70, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=70, pitch=61, start=2.0, end=2.25),
    pretty_midi.Note(velocity=70, pitch=62, start=2.25, end=2.5),
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=70, pitch=63, start=3.0, end=3.25),
    pretty_midi.Note(velocity=70, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=70, pitch=60, start=3.5, end=3.75),
    pretty_midi.Note(velocity=70, pitch=61, start=3.75, end=4.0),
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=70, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=70, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=70, pitch=61, start=5.0, end=5.25),
    pretty_midi.Note(velocity=70, pitch=63, start=5.25, end=5.5),
    pretty_midi.Note(velocity=70, pitch=62, start=5.5, end=5.75),
    pretty_midi.Note(velocity=70, pitch=60, start=5.75, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=70, start=1.75, end=2.0),  # D7
    pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=74, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=77, start=1.75, end=2.0),
    
    pretty_midi.Note(velocity=90, pitch=70, start=2.75, end=3.0),  # D7
    pretty_midi.Note(velocity=90, pitch=72, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=74, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=77, start=2.75, end=3.0),
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.0),  # D7
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=4.0),
    
    pretty_midi.Note(velocity=90, pitch=70, start=4.75, end=5.0),  # D7
    pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=74, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=77, start=4.75, end=5.0),
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=70, start=5.75, end=6.0),  # D7
    pretty_midi.Note(velocity=90, pitch=72, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=74, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=77, start=5.75, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Tenor motif — short, singable, leaves it hanging
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=1.6875, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0),    # G
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=3.1875, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5),    # G
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=4.6875, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0),    # G
    # Leave it hanging on G
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75),
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
