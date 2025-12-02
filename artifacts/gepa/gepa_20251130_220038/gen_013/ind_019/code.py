
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

# Bass line (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),   # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.25),   # E
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),   # F#
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),   # A
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25),   # A#
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5),   # B
    pretty_midi.Note(velocity=90, pitch=76, start=3.5, end=3.75),   # C#
    pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=90, pitch=79, start=4.0, end=4.25),   # E
    pretty_midi.Note(velocity=90, pitch=81, start=4.25, end=4.5),   # F#
    pretty_midi.Note(velocity=90, pitch=83, start=4.5, end=4.75),   # G
    pretty_midi.Note(velocity=90, pitch=84, start=4.75, end=5.0),   # G#
    pretty_midi.Note(velocity=90, pitch=86, start=5.0, end=5.25),   # A
    pretty_midi.Note(velocity=90, pitch=88, start=5.25, end=5.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=89, start=5.5, end=5.75),   # B
    pretty_midi.Note(velocity=90, pitch=91, start=5.75, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, on 2 and 4
piano_notes = [
    # Bar 2: D7 on 2
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=2.0, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=79, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=82, start=2.0, end=2.25),  # C
    # Bar 3: G7 on 2
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.25),  # F
    # Bar 4: A7 on 2
    pretty_midi.Note(velocity=100, pitch=82, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=85, start=4.0, end=4.25),  # C#
    pretty_midi.Note(velocity=100, pitch=87, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=100, pitch=90, start=4.0, end=4.25),  # G
    # Bar 4: D7 on 4
    pretty_midi.Note(velocity=100, pitch=74, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=5.0, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=79, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=82, start=5.0, end=5.25),  # C
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875)
drums.notes.extend(drum_notes)

# Saxophone (Dante) - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=74, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=110, pitch=77, start=1.75, end=2.0),   # F#
    pretty_midi.Note(velocity=110, pitch=74, start=2.0, end=2.25),   # D
    pretty_midi.Note(velocity=110, pitch=77, start=2.25, end=2.5),   # F#
    pretty_midi.Note(velocity=110, pitch=74, start=2.5, end=2.75),   # D
    pretty_midi.Note(velocity=110, pitch=77, start=2.75, end=3.0),   # F#
    pretty_midi.Note(velocity=110, pitch=79, start=3.0, end=3.25),   # A
    pretty_midi.Note(velocity=110, pitch=82, start=3.25, end=3.5),   # C
    pretty_midi.Note(velocity=110, pitch=79, start=3.5, end=3.75),   # A
    pretty_midi.Note(velocity=110, pitch=82, start=3.75, end=4.0),   # C
    pretty_midi.Note(velocity=110, pitch=79, start=4.0, end=4.25),   # A
    pretty_midi.Note(velocity=110, pitch=82, start=4.25, end=4.5),   # C
    pretty_midi.Note(velocity=110, pitch=77, start=4.5, end=4.75),   # F#
    pretty_midi.Note(velocity=110, pitch=74, start=4.75, end=5.0),   # D
    pretty_midi.Note(velocity=110, pitch=77, start=5.0, end=5.25),   # F#
    pretty_midi.Note(velocity=110, pitch=74, start=5.25, end=5.5),   # D
    pretty_midi.Note(velocity=110, pitch=77, start=5.5, end=5.75),   # F#
    pretty_midi.Note(velocity=110, pitch=74, start=5.75, end=6.0),   # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
