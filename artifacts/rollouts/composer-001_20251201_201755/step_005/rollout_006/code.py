
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),   # F#2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, resolve on the last bar
piano_notes = [
    # Bar 2: Dmaj7 (D F# A C#)
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # C#
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.5),  # F
    # Bar 4: Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=55, start=2.5, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=2.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (E6), F# (E7), A (E8), D (E6) — short and haunting
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=81, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=83, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=110, pitch=86, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=81, start=2.25, end=2.375),  # D
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
