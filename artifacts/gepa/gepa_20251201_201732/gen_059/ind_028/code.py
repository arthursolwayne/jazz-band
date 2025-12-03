
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
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass (D2-G2, roots and fifths with chromatic approaches)
# Bar 2: Dm7 -> D -> C# -> D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2
]
# Bar 3: G7 -> G -> F# -> G
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75),  # B2
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125),  # A2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # G2
])
# Bar 4: Cmaj7 -> C -> B -> C
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),  # E3
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625),  # D#3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),  # C3
])
bass.notes.extend(bass_notes)

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 -> D -> F -> A -> D
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # G4
]
# Bar 3: G7 -> G -> B -> D -> F#
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # C#5
])
# Bar 4: Cmaj7 -> C -> E -> G -> B
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # B4
])
piano.notes.extend(piano_notes)

# Little Ray on drums (same pattern as bar 1 repeated for bars 2-4)
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# You on sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - Bb4 - D4 (first bar), then repeat but with a slight variation
# Bar 2: D4 - F4 - Bb4 - D4 (start at 1.5s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D4
]
# Bar 3: D4 - F4 - Bb4 - D4 (start at 3.0s)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),
])
# Bar 4: D4 - F4 - Bb4 - D4 (start at 4.5s)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),
])
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
