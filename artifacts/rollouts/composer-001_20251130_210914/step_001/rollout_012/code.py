
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
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick, kick2, snare, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # D
    # Bar 3: F7
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.375),  # F
    # Bar 4: Gm7
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # F
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick, kick2, snare, snare2])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - Eb - F - D (rest on F) - D - Eb - F - D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
