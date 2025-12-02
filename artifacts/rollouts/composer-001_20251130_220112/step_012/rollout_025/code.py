
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.5),  # G#
    pretty_midi.Note(velocity=90, pitch=44, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=90, pitch=45, start=2.75, end=3.0),  # A#
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=47, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=90, pitch=48, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=4.0),  # C#
    pretty_midi.Note(velocity=90, pitch=50, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=51, start=4.25, end=4.5),  # D#
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=53, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=90, pitch=54, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.5),  # F#
    pretty_midi.Note(velocity=90, pitch=56, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=90, pitch=57, start=5.75, end=6.0),  # G#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F (root)
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),  # A (7th)
    pretty_midi.Note(velocity=80, pitch=68, start=1.75, end=2.0),  # Bb (9th)
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # F (root)
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),  # A (7th)
    pretty_midi.Note(velocity=80, pitch=68, start=2.25, end=2.5),  # Bb (9th)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # F (root)
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),  # A (7th)
    pretty_midi.Note(velocity=80, pitch=68, start=3.25, end=3.5),  # Bb (9th)
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # F (root)
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),  # A (7th)
    pretty_midi.Note(velocity=80, pitch=68, start=3.75, end=4.0),  # Bb (9th)
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # F (root)
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0),  # A (7th)
    pretty_midi.Note(velocity=80, pitch=68, start=4.75, end=5.0),  # Bb (9th)
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),  # F (root)
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5),  # A (7th)
    pretty_midi.Note(velocity=80, pitch=68, start=5.25, end=5.5),  # Bb (9th)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # A (motif start)
    pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=2.0),  # C (up a third)
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # A (back down)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # A (motif repeat)
    pretty_midi.Note(velocity=100, pitch=70, start=3.25, end=3.5),  # C (up a third)
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # A (back down)
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # Bb (half step up)
    pretty_midi.Note(velocity=100, pitch=70, start=4.0, end=4.25),  # C (resolve)
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # A (motif final time)
    pretty_midi.Note(velocity=100, pitch=70, start=4.75, end=5.0),  # C (up a third)
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # A (back down)
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # Bb (half step up)
    pretty_midi.Note(velocity=100, pitch=70, start=5.5, end=5.75),  # C (resolve)
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # A (end on A)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
