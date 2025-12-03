
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.5),  # A
    pretty_midi.Note(velocity=80, pitch=40, start=2.5, end=3.0),  # G#
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=3.5, end=4.0),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=4.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=38, start=5.0, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=5.5, end=6.0),  # G#
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=2.0),  # D
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.5),  # Ab
])
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=3.0),  # D
])
# Resolve on last bar
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.5),  # D
])
# Repeat chords on last two bars
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=4.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=4.0),  # C
    pretty_midi.Note(velocity=100, pitch=73, start=3.5, end=4.0),  # D
])
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=4.0, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=73, start=4.0, end=4.5),  # D
])
piano.notes.extend(piano_notes)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, G#, F (MIDI 71, 66, 68, 71)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),   # Ab
    pretty_midi.Note(velocity=110, pitch=68, start=2.0, end=2.25),  # G#
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=110, pitch=68, start=3.5, end=3.75),  # G#
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0),   # Ab
    pretty_midi.Note(velocity=110, pitch=68, start=5.0, end=5.25),  # G#
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.5),  # F
]
sax.notes.extend(sax_notes)

# Drums continue for bars 2-4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.875), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75), # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.375),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.375),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.375, end=4.625), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),   # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
