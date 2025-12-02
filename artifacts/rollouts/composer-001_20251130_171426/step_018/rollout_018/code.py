
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
    # Kick on 1 and 3 (beat 0 and 2)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    # Snare on 2 and 4 (beat 1 and 3)
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    # Hihat on every eighth note
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Drums for bars 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3 (beat 0 and 2)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125),
    # Snare on 2 and 4 (beat 1 and 3)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5),
    # Hihat on every eighth note
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5),
drums.notes.extend(drum_notes)

# Saxophone motif: short, singable, hanging
# F7 -> G7 -> A7 -> Bb7 -> C7 -> D7 -> Eb7 -> F7
motif_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.65),
    pretty_midi.Note(velocity=100, pitch=89, start=1.65, end=1.8),
    pretty_midi.Note(velocity=100, pitch=91, start=1.8, end=1.95),
    pretty_midi.Note(velocity=100, pitch=90, start=1.95, end=2.1),
    pretty_midi.Note(velocity=100, pitch=92, start=2.1, end=2.25),
    pretty_midi.Note(velocity=100, pitch=94, start=2.25, end=2.4),
    pretty_midi.Note(velocity=100, pitch=93, start=2.4, end=2.55),
    pretty_midi.Note(velocity=100, pitch=87, start=2.55, end=2.7),
]
sax.notes.extend(motif_notes)

# Bass line: walking line, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=54, start=1.5, end=1.65),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=1.65, end=1.8),  # F#
    pretty_midi.Note(velocity=80, pitch=57, start=1.8, end=1.95),  # G
    pretty_midi.Note(velocity=80, pitch=59, start=1.95, end=2.1),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=2.1, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.4),  # B
    pretty_midi.Note(velocity=80, pitch=64, start=2.4, end=2.55),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=2.55, end=2.7),  # C#
    pretty_midi.Note(velocity=80, pitch=67, start=2.7, end=2.85),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=2.85, end=3.0),  # E
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.15),  # F
    pretty_midi.Note(velocity=80, pitch=72, start=3.15, end=3.3),  # G
    pretty_midi.Note(velocity=80, pitch=74, start=3.3, end=3.45),  # A
    pretty_midi.Note(velocity=80, pitch=76, start=3.45, end=3.6),  # Bb
    pretty_midi.Note(velocity=80, pitch=77, start=3.6, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=79, start=3.75, end=3.9),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2: F7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.375),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.375),  # D
    # Bar 3: G7 on beat 2
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=3.25, end=3.375),  # D
    # Bar 4: A7 on beat 2
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.375),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=4.25, end=4.375),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.25, end=4.375),  # D
    pretty_midi.Note(velocity=100, pitch=81, start=4.25, end=4.375),  # E
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
