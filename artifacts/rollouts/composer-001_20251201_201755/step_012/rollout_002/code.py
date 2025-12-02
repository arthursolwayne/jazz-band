
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
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (root) -> C# (chromatic approach to D)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),
    # Bar 3: F (fifth) -> E (chromatic approach to F)
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),
    # Bar 4: D (root) -> C# (chromatic approach to D)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=39, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875), # C
]
# Bar 3: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375), # B
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375), # F
])
# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.875), # Bb
])
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D E F G A Bb C
# Motif: D - F - G - A (octave up)
# Bar 2: D (D4), F (F4), G (G4), A (A4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25), # F4
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625), # G4
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0), # A4
    # Bar 3: leave it hanging
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375), # A4
    # Bar 4: come back and finish it
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875), # D4
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25), # F4
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.625), # G4
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0), # A4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
