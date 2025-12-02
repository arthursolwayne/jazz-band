
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875)   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - chromatic walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=56, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=100, pitch=48, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=46, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=44, start=5.625, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 2nd beat
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # C
    # Bar 3: Dm7 on 2nd beat
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # C
    # Bar 4: Dm7 on 2nd beat
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # C
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),   # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.999),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),   # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Sax melody - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, E, F, G, A, Bb, C
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=1.875), # F
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25),   # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
