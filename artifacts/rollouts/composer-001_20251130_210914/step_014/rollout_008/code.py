
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: sax begins with a motif
# F7 -> G7 -> A7 -> D7 (F7, G7, A7, D7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F7
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # G7
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # A7
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D7
]
sax.notes.extend(sax_notes)

# Marcus (bass): walking line with chromatic approaches
bass_notes = [
    # Bar 2: F -> Eb -> D -> C (chromatic approach to F)
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.5),  # C
    # Bar 3: G -> F -> E -> D
    pretty_midi.Note(velocity=80, pitch=48, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=80, pitch=45, start=3.25, end=3.5),  # D
    # Bar 4: A -> G -> F -> E
    pretty_midi.Note(velocity=80, pitch=49, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=4.25, end=4.5),  # E
]
bass.notes.extend(bass_notes)

# Diane (piano): 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0),  # F7
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=1.75, end=2.0),  # E
    # Bar 3: G7 on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # G7
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=2.75, end=3.0),  # D
    # Bar 4: A7 on beat 2
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # A7
    pretty_midi.Note(velocity=90, pitch=73, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.0),  # G
]
piano.notes.extend(piano_notes)

# Bar 3: Sax continues motif, Diane continues comp, Marcus walks, Ray fills
# Bar 4: Sax resolves the motif, Diane continues comp, Marcus walks, Ray fills

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write('dante_intro.mid')
