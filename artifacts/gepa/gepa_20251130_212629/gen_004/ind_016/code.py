
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus): Walking line, chromatic approaches
# F7 chord: F A C E (root, 3, 5, 7)
# F7 in bass: F A C E
# Walking line: F Ab Bb B C Eb D F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=68, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=3.0),   # B
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=70, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=70, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=68, start=5.625, end=6.0),   # Ab
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
# F7: F A C E
# Bb7: Bb D F Ab
# C7: C E G B
# E7: E G# B D
piano_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=81, start=1.5, end=1.875),  # A (3)
    pretty_midi.Note(velocity=90, pitch=78, start=1.5, end=1.875),  # C (5)
    pretty_midi.Note(velocity=90, pitch=84, start=1.5, end=1.875),  # E (7)
    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # Bb (root)
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # D (3)
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.375),  # F (5)
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.375),  # Ab (7)
    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # C (root)
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875),  # E (3)
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875),  # G (5)
    pretty_midi.Note(velocity=90, pitch=81, start=4.5, end=4.875),  # B (7)
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F Bb D (F7 arpeggio) with a twist
# F -> Bb -> D -> F (but shift on the last note)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=1.75),    # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),    # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),    # D
    pretty_midi.Note(velocity=110, pitch=70, start=2.25, end=2.5),    # F (sustained)
    pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=3.25),    # F (return)
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5),    # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),    # D
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.0),    # G (twist)
    pretty_midi.Note(velocity=110, pitch=70, start=4.5, end=4.75),    # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),    # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25),    # D
    pretty_midi.Note(velocity=110, pitch=70, start=5.25, end=5.5),    # F
    pretty_midi.Note(velocity=110, pitch=70, start=5.5, end=5.75),    # F (final)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
# Snare on 2 and 4
# Hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hihat
    for eighth in range(0, 8):
        start = bar_start + eighth * 0.375
        end = start + 0.1875
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)

drums.notes.extend([note for note in drums.notes])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
