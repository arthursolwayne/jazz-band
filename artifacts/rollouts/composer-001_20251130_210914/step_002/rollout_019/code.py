
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
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
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in Dm, chromatic approaches
bass_notes = [
    # Bar 2: Dm - D, F, Ab, C
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.625),  # Eb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),  # G
    # Bar 3: Dm - Ab, C, D, F
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=61, start=4.125, end=4.5),  # Eb
    # Bar 4: Dm - G, C, D, F
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=61, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    # Bar 3: Dm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    # Bar 4: Dm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
]
piano.notes.extend(piano_notes)

# Sax - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D (62) -> Eb (61) -> F (64) -> G (65)
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=61, start=1.75, end=1.9),
    pretty_midi.Note(velocity=110, pitch=64, start=1.9, end=2.05),
    pretty_midi.Note(velocity=110, pitch=65, start=2.05, end=2.25),
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=61, start=3.25, end=3.4),
    pretty_midi.Note(velocity=110, pitch=64, start=3.4, end=3.55),
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=61, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.5),
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.75),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
