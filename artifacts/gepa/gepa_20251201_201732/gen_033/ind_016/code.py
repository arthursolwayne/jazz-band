
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
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

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (2), F# (3), D (4), E (5)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # F#2
    pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0), # E2
    # Bar 3: A (2), C# (3), B (4), C# (5)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375), # A2
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75), # C#2
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125), # B2
    pretty_midi.Note(velocity=90, pitch=46, start=4.125, end=4.5), # C#2
    # Bar 4: D (2), F# (3), D (4), F# (5)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875), # D2
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25), # F#2
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0), # F#2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25),
]
# Bar 3: Gm7 (G Bb D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.75),
])
# Bar 4: Cmaj7 (C E G B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25),
])
for note in piano_notes:
    piano.notes.append(note)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F# (67), B (71), D (62) — but only first three notes in bar 2, and last note in bar 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
