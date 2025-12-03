
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
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus): Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Fm root (F)
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25),  # Fm 5th (C)
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # chromatic approach to Bb
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # chromatic approach to Ab
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0),  # chromatic approach to Bb
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=46, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=2.25),  # D
    # Bar 3: Ab7
    pretty_midi.Note(velocity=100, pitch=48, start=2.25, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=3.0),  # Ab
    # Bar 4: Bb7
    pretty_midi.Note(velocity=100, pitch=46, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),  # Bb
    # Resolutions
    pretty_midi.Note(velocity=100, pitch=56, start=3.75, end=4.5),  # G7
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.5),  # F
    # Final bar: Fm7
    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=46, start=4.5, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),  # D
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # G
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # G
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),  # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),  # Hihat on every eighth
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),  # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),  # Hihat on every eighth
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),  # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),  # Hihat on every eighth
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
