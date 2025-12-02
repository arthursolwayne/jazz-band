
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
    end = start + 1.5
    # Kick on 1 (0.0s) and 3 (1.125s)
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.125 + 0.375)
    # Snare on 2 (0.75s) and 4 (1.5s)
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=end - 0.375, end=end)
    # Hi-hat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: Dm (D2, F2, A2), chromatic approach to D
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.5 + 0.375),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.5 + 0.375, end=1.5 + 0.75),  # F2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5 + 0.75, end=1.5 + 1.125),  # A2
    pretty_midi.Note(velocity=100, pitch=37, start=1.5 + 1.125, end=1.5 + 1.5),  # chromatic approach to D
]
# Bar 3: Gm7 (G2, Bb2, D2), chromatic approach to G
bass_notes.extend([
    pretty_midi.Note(velocity=100, pitch=43, start=1.5 + 1.5, end=1.5 + 1.875),  # G2
    pretty_midi.Note(velocity=100, pitch=45, start=1.5 + 1.875, end=1.5 + 2.25),  # Bb2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5 + 2.25, end=1.5 + 2.625),  # D2
    pretty_midi.Note(velocity=100, pitch=44, start=1.5 + 2.625, end=1.5 + 3.0),  # chromatic approach to G
])
# Bar 4: Cm7 (C2, Eb2, G2), chromatic approach to C
bass_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5 + 3.0, end=1.5 + 3.375),  # C2
    pretty_midi.Note(velocity=100, pitch=39, start=1.5 + 3.375, end=1.5 + 3.75),  # Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=1.5 + 3.75, end=1.5 + 4.125),  # G2
    pretty_midi.Note(velocity=100, pitch=35, start=1.5 + 4.125, end=1.5 + 4.5),  # chromatic approach to C
])
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.375),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + 0.375),  # A4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.5 + 0.375),  # C4
]
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 1.5, end=1.5 + 1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 1.5, end=1.5 + 1.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 1.5, end=1.5 + 1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 1.5, end=1.5 + 1.875),  # F4
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=1.5 + 3.0, end=1.5 + 3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=1.5 + 3.0, end=1.5 + 3.375),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 3.0, end=1.5 + 3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 3.0, end=1.5 + 3.375),  # Bb4
])
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    end = start + 1.5
    # Kick on 1 (0.0s) and 3 (1.125s)
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.125 + 0.375)
    # Snare on 2 (0.75s) and 4 (1.5s)
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=end - 0.375, end=end)
    # Hi-hat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Dm (D4, F4, A4, C4) - Play a motif starting on D4, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.5 + 0.375),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=1.5 + 0.75, end=1.5 + 1.125),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.5 + 1.5, end=1.5 + 1.875),  # A4
    pretty_midi.Note(velocity=110, pitch=60, start=1.5 + 2.25, end=1.5 + 2.625),  # C4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
