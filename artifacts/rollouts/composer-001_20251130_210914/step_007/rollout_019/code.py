
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=100, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=100, pitch=42, start=1.375, end=1.5)
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS: Walking line in F (F, G, A, Bb), chromatic approaches
bass_notes = [
    # Bar 2: F, Gb, G, A
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # A
    
    # Bar 3: Bb, B, C, D
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=63, start=2.75, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # D
    
    # Bar 4: Eb, E, F, G
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.25, end=4.5),  # G
]

bass.notes.extend(bass_notes)

# PIANO: 7th chords, comp on 2 and 4 (F7, Bb7, F7, Bb7)
piano_notes = []

# Bar 2: F7 on beat 2 (2.0 - 2.25)
for note in [65, 67, 69, 64]:  # F, A, C, Gb
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=2.0, end=2.25))

# Bar 3: Bb7 on beat 4 (3.5 - 3.75)
for note in [62, 64, 67, 60]:  # Bb, D, F, Eb
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=3.5, end=3.75))

# Bar 4: F7 on beat 2 (4.0 - 4.25)
for note in [65, 67, 69, 64]:  # F, A, C, Gb
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=4.0, end=4.25))

# Bar 4: Bb7 on beat 4 (4.5 - 4.75)
for note in [62, 64, 67, 60]:  # Bb, D, F, Eb
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=4.5, end=4.75))

piano.notes.extend(piano_notes)

# SAX: Tenor sax motif in F. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif - F, A, C
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),  # A
    
    # Bar 3: Leave it hanging - just A
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # A
    
    # Bar 4: Return to motif - C, F, A
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.625),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=3.625, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.875),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=3.875, end=4.0),  # F
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_piece.mid")
