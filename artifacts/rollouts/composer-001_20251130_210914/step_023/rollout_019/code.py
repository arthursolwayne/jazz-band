
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2: F -> Gb -> G -> Ab (chromatic approach to A)
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=72, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5),  # Ab
    # Bar 3: A -> Bb -> B -> C (chromatic approach to C#)
    pretty_midi.Note(velocity=80, pitch=76, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=80, pitch=75, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=77, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=80, pitch=76, start=3.25, end=3.5),  # C
    # Bar 4: C# -> D -> D# -> E (chromatic approach to F)
    pretty_midi.Note(velocity=80, pitch=78, start=3.5, end=3.75),  # C#
    pretty_midi.Note(velocity=80, pitch=79, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=80, pitch=80, start=4.0, end=4.25),  # D#
    pretty_midi.Note(velocity=80, pitch=79, start=4.25, end=4.5),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=79, start=2.0, end=2.25),  # D
    # Bar 3: A7 on beat 2
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.25),  # C#
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.25),  # D#
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=100, pitch=79, start=4.0, end=4.25),  # D
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)
drums.notes.extend(drum_notes[0:12] * 3)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=76, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=77, start=2.0, end=2.25),  # B
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=81, start=3.0, end=3.25),  # D#
    # Bar 4: Return and finish
    pretty_midi.Note(velocity=110, pitch=76, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=77, start=4.25, end=4.5),  # B
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
