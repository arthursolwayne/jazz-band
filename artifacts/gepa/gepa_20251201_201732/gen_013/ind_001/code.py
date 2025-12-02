
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, roots and fifths with chromatic approaches
# Fm: F - Ab - D - C
# Bass notes (MIDI)
# Bar 2: F (53), Ab (57), G (59), F (53)
# Bar 3: D (50), C (52), Bb (58), D (50)
# Bar 4: F (53), Ab (57), G (59), F (53)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=57, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=58, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=59, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
# Bar 3: D7 (D, F#, A, C)
# Bar 4: Fm7 (F, Ab, C, D)
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),
    # Bar 3: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),
    # Bar 4: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Ab - D - C (MIDI: 53, 57, 50, 52)
# Play the first two notes in bar 2, leave it hanging, then play the last two in bar 4
sax_notes = [
    # Bar 2: F and Ab
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=57, start=1.75, end=2.0),
    # Bar 4: D and C
    pretty_midi.Note(velocity=110, pitch=50, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=52, start=4.75, end=5.0),
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
# Snare on 2 and 4
# Hihat on every eighth
for bar in [2, 3, 4]:
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        start = bar_start + i * 0.1875
        end = start + 0.1875
        pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
