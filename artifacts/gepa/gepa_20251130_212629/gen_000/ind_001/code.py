
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=90, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass line (walking, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=52, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=54, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=80, pitch=55, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=48, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=50, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=4.25, end=4.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=52, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=54, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=80, pitch=48, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=5.75, end=6.0),  # Gb
]
bass.notes.extend(bass_notes)

# Diane - Piano: 7th chords on 2 and 4, comp
piano_notes = [
    # Bar 2: Fm7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.5),  # D
    # Bar 3: Fm7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.0),  # D
    # Bar 4: Fm7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.5),  # D
]
piano.notes.extend(piano_notes)

# Little Ray - Drums (already added in bar 1)
# Repeat bar 1 pattern for bar 2-4, offset by 1.5s
for note in drum_notes:
    new_note = pretty_midi.Note(
        velocity=note.velocity,
        pitch=note.pitch,
        start=note.start + 1.5,
        end=note.end + 1.5
    )
    drums.notes.append(new_note)
for note in drum_notes:
    new_note = pretty_midi.Note(
        velocity=note.velocity,
        pitch=note.pitch,
        start=note.start + 3.0,
        end=note.end + 3.0
    )
    drums.notes.append(new_note)

# Dante - Sax: Motif (start on bar 2, 1.5s)
# Fm: F, Ab, Bb, C
# Motif: F (1.5s) -> Ab (1.75s) -> Bb (2.0s) -> C (2.25s)
# Leave it hanging, come back to finish it at 5.5s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=87, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=88, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=91, start=2.25, end=2.5),  # C
    # Repeat the same motif at the end to finish it
    pretty_midi.Note(velocity=100, pitch=84, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=87, start=5.75, end=6.0),  # Ab
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
