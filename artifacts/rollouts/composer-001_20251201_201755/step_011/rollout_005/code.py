
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)
# Bass: Walking line (F2 - Bb2, MIDI 53 - 57), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (53) -> Bb (57) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=54, start=1.875, end=2.125),
    pretty_midi.Note(velocity=80, pitch=57, start=2.125, end=2.5),
    # Bar 3: Bb (57) -> Eb (60) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=57, start=2.5, end=2.875),
    pretty_midi.Note(velocity=80, pitch=58, start=2.875, end=3.125),
    pretty_midi.Note(velocity=80, pitch=60, start=3.125, end=3.5),
    # Bar 4: Eb (60) -> Ab (63) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=60, start=3.5, end=3.875),
    pretty_midi.Note(velocity=80, pitch=61, start=3.875, end=4.125),
    pretty_midi.Note(velocity=80, pitch=63, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=2.0),
]
# Bar 3: Bbmaj7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=57, start=2.0, end=2.5),
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.5),
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.5),
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.5),
])
# Bar 4: Ebmaj7 (Eb, G, Bb, D)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=3.0),
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (66), Ab (69), Bb (62), F (66) - play the first two notes, then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5-2.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
]
# Bar 3 (2.0-2.5s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=2.375, end=2.5),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5),
])
# Bar 4 (2.5-3.0s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.0),
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo.mid")
