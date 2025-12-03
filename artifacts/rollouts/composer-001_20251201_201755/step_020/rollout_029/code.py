
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.75, end=2.0),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.25),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.5),  # F#2 (chromatic approach)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.25),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=3.25, end=3.5),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=3.5, end=3.75),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.0),  # F#2
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.75),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.75, end=5.0),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=5.0, end=5.25),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.5),  # F#2
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D F# A C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # C#4
]
# Bar 3: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # F4
])
# Bar 4: D7 (D F# A C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.0),  # C4
])
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - Bb4 - D5 (start), then leave it hanging on Bb4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25),  # Bb4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # D5
    pretty_midi.Note(velocity=110, pitch=71, start=3.5, end=3.75),  # Bb4 (return)
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # D5
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25),  # F#5
    pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5),  # D5
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

drums.notes.extend([note for note in drums.notes if note not in drum_notes])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
