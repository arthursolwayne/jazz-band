
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
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=37, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.25),  # A (fifth)
    pretty_midi.Note(velocity=80, pitch=38, start=2.25, end=2.625),  # G (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=3.0),  # Bb (third)
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # Bb (root)
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),  # D (fifth)
    pretty_midi.Note(velocity=80, pitch=41, start=3.75, end=4.125),  # C# (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),  # E (third)
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # E (root)
    pretty_midi.Note(velocity=80, pitch=45, start=4.875, end=5.25),  # G (fifth)
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.625),  # F# (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=46, start=5.625, end=6.0),  # A (third)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=53, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=85, pitch=50, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=85, pitch=55, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=85, pitch=57, start=1.5, end=1.875),  # F
]
# Bar 3: Bbmaj7 (Bb D F A)
piano_notes.extend([
    pretty_midi.Note(velocity=85, pitch=52, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=85, pitch=49, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=85, pitch=51, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=85, pitch=53, start=3.0, end=3.375),  # Bb
])
# Bar 4: Am7 (A C E G)
piano_notes.extend([
    pretty_midi.Note(velocity=85, pitch=51, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=85, pitch=48, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=85, pitch=50, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=85, pitch=52, start=4.5, end=4.875),  # A
])
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (G4), Bb (A4), C (B4), F (D5)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F (G4)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # Bb (A4)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # C (B4)
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # F (D5)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F (G4)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
