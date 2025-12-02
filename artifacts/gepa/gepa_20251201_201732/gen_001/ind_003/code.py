
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
    start_time = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.375, end=start_time + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.125, end=start_time + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start_time + i * 0.375, end=start_time + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass (walking line, D2-G2, roots and fifths with chromatic approaches)
# Bar 2: D2 - F#2 (chromatic approach)
# Bar 3: A2 - C#2 (chromatic approach)
# Bar 4: D2 - F#2 (resolve on last bar)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=37, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),  # F#2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),   # C#2
    pretty_midi.Note(velocity=90, pitch=37, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),  # F#2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),   # C#2
    pretty_midi.Note(velocity=90, pitch=37, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),  # F#2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # A2
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),   # C#2
]
bass.notes.extend(bass_notes)

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D-F#-A-C)
# Bar 3: Bm7 (B-D-F#-A)
# Bar 4: Gm7 (G-Bb-D-F)
piano_notes = [
    # Bar 2: D7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5
    # Bar 3: Bm7
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # F#5
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # A5
    # Bar 4: Gm7
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # F5
]
piano.notes.extend(piano_notes)

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start_time = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.375, end=start_time + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.125, end=start_time + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start_time + i * 0.375, end=start_time + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - B4 - D5, with a space in the middle
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),  # D5 (return after gap)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
