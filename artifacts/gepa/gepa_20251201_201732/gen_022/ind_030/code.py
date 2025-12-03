
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),  # A
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=46, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=90, pitch=47, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=49, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=82, start=1.5, end=2.0),
    # Bar 3: Em7 (E, G, B, D)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=75, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.5),
    # Bar 4: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=82, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=83, start=4.5, end=5.0),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif (F, A, Bb, C)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=68, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),
    # Bar 3: Leave it hanging (no notes)
    # Bar 4: Return and finish it (F, A, Bb, C)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=68, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),
]
sax.notes.extend(sax_notes)

# Drums continue with same pattern for bars 2-4
for i in range(1, 4):
    for note in drum_notes:
        new_note = pretty_midi.Note(
            velocity=note.velocity,
            pitch=note.pitch,
            start=note.start + i * 1.5,
            end=note.end + i * 1.5
        )
        drums.notes.append(new_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
