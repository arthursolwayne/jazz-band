
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
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass (Marcus) - walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), F#2 (fifth), E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=43, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.25),
    # Bar 3: A2 (root), C#3 (fifth), B2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=50, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=49, start=2.75, end=3.0),
    # Bar 4: D2 (root), F#2 (fifth), E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=43, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.75)
]
bass.notes.extend(bass_notes)

# Piano (Diane) - Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),  # C5 (bass note)
    # Bar 3: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # C#5
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # E5
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # G5
    # Bar 4: Dmaj7 (D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # A4
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.25),  # C#5
]
piano.notes.extend(piano_notes)

# Drums (Little Ray) - Bar 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5)
]
drums.notes.extend(drum_notes)

# Sax (Dante) - Bar 2: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D4 (62), F#4 (65), A4 (69), D5 (72)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.5),
    # Repeat the motif starting at bar 3 (halfway through)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.0)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
