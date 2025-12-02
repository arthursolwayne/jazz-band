
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Sax enters with motif (1.5 - 3.0s)
# Motif: Dm7 - Eb7 - Dm7 - C7 (in Dm key)
sax_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.625), # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.625), # C
    # Bar 3: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.125), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125), # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.125), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125), # D
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625), # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.625), # A
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.625), # C
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Dm (1.5 - 6.0s)
bass_notes = [
    # Bar 2: D - Eb - F - G
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=2.75),
    # Bar 3: A - Bb - C - D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.25),
    # Bar 4: D - Eb - F - G
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=5.75),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (1.5 - 6.0s)
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.625),
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.625),
    pretty_midi.Note(velocity=95, pitch=60, start=1.5, end=1.625),
    # Bar 3: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=95, pitch=60, start=3.0, end=3.125),
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.125),
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.125),
    pretty_midi.Note(velocity=95, pitch=65, start=3.0, end=3.125),
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.625),
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.625),
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.625),
    pretty_midi.Note(velocity=95, pitch=60, start=4.5, end=4.625),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Continue pattern for bars 2-4 (1.5 - 6.0s)
for i in range(3):
    start = 1.5 + i * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875)
    hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.875, end=start + 2.25)
    hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=start + 2.25, end=start + 2.625)
    hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=start + 2.625, end=start + 3.0)

    drums.notes.append(kick1)
    drums.notes.append(kick2)
    drums.notes.append(snare1)
    drums.notes.append(snare2)
    drums.notes.append(hihat1)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)
    drums.notes.append(hihat4)
    drums.notes.append(hihat5)
    drums.notes.append(hihat6)
    drums.notes.append(hihat7)
    drums.notes.append(hihat8)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
