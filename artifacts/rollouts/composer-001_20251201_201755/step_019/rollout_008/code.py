
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5s - 3.0s)
    pretty_midi.Note(velocity=90, pitch=75, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=77, start=1.875, end=2.25), # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625), # F#2
    pretty_midi.Note(velocity=90, pitch=77, start=2.625, end=3.0),  # G2
    # Bar 3 (3.0s - 4.5s)
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=79, start=3.375, end=3.75), # A2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=78, start=3.75, end=4.125), # Ab2
    pretty_midi.Note(velocity=90, pitch=79, start=4.125, end=4.5),  # A2
    # Bar 4 (4.5s - 6.0s)
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875),  # A2
    pretty_midi.Note(velocity=90, pitch=81, start=4.875, end=5.25), # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=80, start=5.25, end=5.625), # A#2
    pretty_midi.Note(velocity=90, pitch=81, start=5.625, end=6.0),  # Bb2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=83, start=1.5, end=1.75),
]
# Bar 3: Dm7 (D, F, A, C)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.25),
]
# Bar 4: G7 (G, B, D, F)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),
]
piano.notes.extend(piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: F (76), Bb (81), F (76), rest
sax_notes_bar2 = [
    pretty_midi.Note(velocity=110, pitch=76, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=81, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=76, start=2.0, end=2.25),
]
# Bar 3: Rest, rest, rest, rest
# Bar 4: F (76), Bb (81), F (76), resolve with a grace note on G (77)
sax_notes_bar4 = [
    pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.5),
    pretty_midi.Note(velocity=110, pitch=81, start=5.5, end=5.75),
    pretty_midi.Note(velocity=110, pitch=76, start=5.75, end=6.0),
    pretty_midi.Note(velocity=60, pitch=77, start=5.75, end=5.75 + 0.05),
]
sax.notes.extend(sax_notes_bar2 + sax_notes_bar4)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
    # Hi-hat on every eighth
    for i in range(8):
        start = bar_start + i * 0.1875
        end = start + 0.1875
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
