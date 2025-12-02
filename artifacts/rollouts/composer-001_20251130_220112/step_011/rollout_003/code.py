
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),   # G
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # G#
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=90, pitch=48, start=4.125, end=4.5),   # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=46, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),   # E
]
bass.notes.extend(bass_notes)

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (F, A, C, D)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # D
    # Bar 3: Dm7 (F, A, C, D)
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # D
    # Bar 4: Dm7 (F, A, C, D)
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # D
]
piano.notes.extend(piano_notes)

# Sax - Dante: short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=1.625, end=1.75),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),  # Bb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.125),  # Bb
    # Bar 4: Return and finish the motif
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.625),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.0),   # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.125, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.375),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.375, end=5.5),   # F
]
sax.notes.extend(sax_notes)

# Drums: continue the pattern for bars 2-4
for i in range(2):
    offset = 1.5 + i * 3.0
    for note in drum_notes:
        new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + offset, note.end + offset)
        drums.notes.append(new_note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
