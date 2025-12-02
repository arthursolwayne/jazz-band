
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

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.5),  # G#

    # Bar 3
    pretty_midi.Note(velocity=80, pitch=52, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=2.75, end=3.0),  # A#
    pretty_midi.Note(velocity=80, pitch=54, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=55, start=3.25, end=3.5),  # B

    # Bar 4
    pretty_midi.Note(velocity=80, pitch=56, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.0),  # C#
    pretty_midi.Note(velocity=80, pitch=58, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=80, pitch=59, start=4.25, end=4.5),  # D#

    # Bar 4, walking through F7
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=80, pitch=61, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.0, end=5.25),  # F#
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=5.5, end=5.75),  # G#
    pretty_midi.Note(velocity=80, pitch=65, start=5.75, end=6.0),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.75),  # E

    # Bar 3: F7 again
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=78, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=82, start=2.5, end=2.75),  # E

    # Bar 4: F7 again
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=78, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=82, start=3.5, end=3.75),  # E
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # A

    # Bar 3: Keep the motif going
    pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.75),  # B
    pretty_midi.Note(velocity=110, pitch=71, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=3.25),  # B

    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=110, pitch=72, start=3.5, end=3.75),  # C#
    pretty_midi.Note(velocity=110, pitch=74, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=110, pitch=73, start=4.0, end=4.25),  # C#
    pretty_midi.Note(velocity=110, pitch=75, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),  # A#
    pretty_midi.Note(velocity=110, pitch=66, start=5.0, end=5.25),  # A
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75)
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875)
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.875, end=bar_start + 2.25)
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 2.25, end=bar_start + 2.625)
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 2.625, end=bar_start + 3.0)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
