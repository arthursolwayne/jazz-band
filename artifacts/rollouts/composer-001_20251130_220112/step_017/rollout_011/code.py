
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

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=57, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875),  # F7: F, A, C, E
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Bar
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.0, end=bar_start + 0.375),
        pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75),
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.0, end=bar_start + 1.5),
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125),
        pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5),
    ]
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
