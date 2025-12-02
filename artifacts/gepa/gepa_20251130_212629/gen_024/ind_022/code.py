
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Drums continue with same pattern
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))

drums.notes.extend(drum_notes)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=6.0),
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F7
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F7
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # F7
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),
]

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),  # C

    # Bar 3: Let it breathe
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5),  # C

    # Bar 4: End with a question
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),  # C
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('jazz_intro.mid')
