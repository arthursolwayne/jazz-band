
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: chromatic walking line, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=51, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=54, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=80, pitch=56, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=58, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=61, start=5.625, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2: Dm7 (D F A C)
chord1 = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25), # C
]
# Bar 3: G7 (G B D F)
chord2 = [
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0), # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0), # B
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=3.0), # G
]
# Bar 4: Cm7 (C Eb G Bb)
chord3 = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.75), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.75), # Bb
]
piano.notes.extend(chord1 + chord2 + chord3)

# Drums: same pattern in bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
