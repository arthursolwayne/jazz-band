
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

# Bass line: Fm (F, Ab, D, C) with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0),  # C
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=44, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125),  # D#
    pretty_midi.Note(velocity=90, pitch=49, start=4.125, end=4.5),  # C#
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=48, start=5.625, end=6.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano chords: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0),
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=4.5),
]
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=46, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=6.0),
]
for note in piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4:
    piano.notes.append(note)

# Sax solo: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, C (Fm scale, but with a twist)
# Play the first two notes on bar 2, leave it hanging, then play the last two on bar 4
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=43, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=41, start=1.75, end=2.0),  # Ab
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=42, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=48, start=4.75, end=5.0),  # C
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4: same pattern as bar 1 (repeat every 1.5s)
for i in range(2):
    for note in drum_notes:
        note.start += 1.5 * (i + 1)
        note.end += 1.5 * (i + 1)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
