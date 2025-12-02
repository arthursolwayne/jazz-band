
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
    
    # Hihat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),   # D
    
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=44, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.5),   # Gb
    
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),   # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=59, start=1.5, end=1.875),  # F7: F
    pretty_midi.Note(velocity=80, pitch=61, start=1.5, end=1.875),  # F7: A
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # F7: Bb
    
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=59, start=3.0, end=3.375),  # F7: F
    pretty_midi.Note(velocity=80, pitch=61, start=3.0, end=3.375),  # F7: A
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # F7: Bb
    
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=4.875),  # F7: F
    pretty_midi.Note(velocity=80, pitch=61, start=4.5, end=4.875),  # F7: A
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # F7: Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=61, start=2.25, end=2.625),  # A
    
    # Bar 3: Leave it hanging, space between
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),  # G
    
    # Bar 4: Return and finish the motif
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=61, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=59, start=5.625, end=6.0),   # F
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
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

midi.write('intro.mid')
