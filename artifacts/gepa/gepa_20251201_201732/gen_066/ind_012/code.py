
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: D (38) -> C# (37) -> G (43) -> A (45)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=70, pitch=37, start=1.875, end=2.25),
    pretty_midi.Note(velocity=70, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=70, pitch=45, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Bar 3: G (43) -> F# (42) -> D (38) -> E (44)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=70, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=70, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=70, pitch=44, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Bar 4: D (38) -> C# (37) -> G (43) -> A (45)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=70, pitch=37, start=4.875, end=5.25),
    pretty_midi.Note(velocity=70, pitch=43, start=5.25, end=5.625),
    pretty_midi.Note(velocity=70, pitch=45, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on last beat of each bar
# Bar 2: Dmaj7 (D-F#-A-C#), 2nd beat
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # C#
]
piano.notes.extend(piano_notes)

# Bar 3: G7 (G-B-D-F), 2nd beat
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # F
]
piano.notes.extend(piano_notes)

# Bar 4: Dm7 (D-F-A-C), 2nd beat
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) -> F# (67) -> D (62) -> B (66)
# Play first two notes in bar 2, leave the rest until bar 4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # B
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),   # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),   # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),   # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
