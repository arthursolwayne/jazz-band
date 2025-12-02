
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass: D2 (38), G2 (43), chromatic approach to G2
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # Chromatic approach to G2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # G2 on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2 on 4
]

bass.notes.extend(bass_notes)

# Diane on piano: Open voicings, resolve on the last bar
piano_notes = [
    # Bar 2: D7 (D F# A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C5
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # F5
    # Bar 4: D7 (D F# A C)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # C5
]

piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=6.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 4
]

drums.notes.extend(drum_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # E4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # E4
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D4
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D4
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
