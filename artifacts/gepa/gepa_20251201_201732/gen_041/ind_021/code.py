
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus): Walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # E
    # Bar 3: C (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75), # C#
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=66, start=4.125, end=4.5),  # B
    # Bar 4: G (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25), # G#
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=77, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=95, pitch=81, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=95, pitch=84, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=95, pitch=86, start=1.5, end=1.875), # Eb
]
# Bar 3: C7 (C E G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=72, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=95, pitch=76, start=3.0, end=3.375), # E
    pretty_midi.Note(velocity=95, pitch=79, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=95, pitch=81, start=3.0, end=3.375), # Bb
])
# Bar 4: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=77, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=95, pitch=81, start=4.5, end=4.875), # B
    pretty_midi.Note(velocity=95, pitch=84, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=95, pitch=86, start=4.5, end=4.875), # F
])
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - B - F - E (with a slight delay on the E)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=1.875),    # F
    pretty_midi.Note(velocity=110, pitch=76, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=110, pitch=70, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=110, pitch=70, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),   # E
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=110, pitch=70, start=5.25, end=5.625),  # F
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75)
]
# Bar 3: Same pattern
drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25)
]
# Bar 4: Same pattern
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=42, start=6.375, end=6.75)
]
drums.notes.extend(drum_notes_bar2)
drums.notes.extend(drum_notes_bar3)
drums.notes.extend(drum_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
