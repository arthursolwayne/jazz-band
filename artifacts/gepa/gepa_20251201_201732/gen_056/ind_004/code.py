
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
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bar_start = 1.5
bass_notes = [
    # Bar 2: F (MIDI 65) -> C (MIDI 60)
    pretty_midi.Note(velocity=100, pitch=60, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=62, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=65, start=bar_start + 0.75, end=bar_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=63, start=bar_start + 1.125, end=bar_start + 1.5),
    # Bar 3: G (MIDI 67) -> D (MIDI 62)
    pretty_midi.Note(velocity=100, pitch=62, start=bar_start + 1.5, end=bar_start + 1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=bar_start + 1.875, end=bar_start + 2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=bar_start + 2.25, end=bar_start + 2.625),
    pretty_midi.Note(velocity=100, pitch=65, start=bar_start + 2.625, end=bar_start + 3.0),
    # Bar 4: A (MIDI 69) -> E (MIDI 64)
    pretty_midi.Note(velocity=100, pitch=64, start=bar_start + 3.0, end=bar_start + 3.375),
    pretty_midi.Note(velocity=100, pitch=66, start=bar_start + 3.375, end=bar_start + 3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=bar_start + 3.75, end=bar_start + 4.125),
    pretty_midi.Note(velocity=100, pitch=67, start=bar_start + 4.125, end=bar_start + 4.5),
]
bass.notes.extend(bass_notes)

# PIANO: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E) -> C (MIDI 60, 64, 65, 69)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=bar_start, end=bar_start + 1.5),
    pretty_midi.Note(velocity=100, pitch=69, start=bar_start, end=bar_start + 1.5),
    pretty_midi.Note(velocity=100, pitch=60, start=bar_start, end=bar_start + 1.5),
    pretty_midi.Note(velocity=100, pitch=64, start=bar_start, end=bar_start + 1.5),
]
# Bar 3: G7 (G, B, D, F) -> D (MIDI 62, 67, 69, 64)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=bar_start + 1.5, end=bar_start + 3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=bar_start + 1.5, end=bar_start + 3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=bar_start + 1.5, end=bar_start + 3.0),
    pretty_midi.Note(velocity=100, pitch=64, start=bar_start + 1.5, end=bar_start + 3.0),
])
# Bar 4: Am7 (A, C, E, G) -> E (MIDI 69, 64, 67, 69)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=bar_start + 3.0, end=bar_start + 4.5),
    pretty_midi.Note(velocity=100, pitch=64, start=bar_start + 3.0, end=bar_start + 4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=bar_start + 3.0, end=bar_start + 4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=bar_start + 3.0, end=bar_start + 4.5),
])
piano.notes.extend(piano_notes)

# DRUMS: Bars 2-4
for bar in range(2, 4):
    start = bar_start + (bar - 2) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# SAX: Your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (MIDI 65), G (MIDI 67), A (MIDI 69), F (MIDI 65)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=110, pitch=67, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=110, pitch=69, start=bar_start + 0.75, end=bar_start + 1.125),
    pretty_midi.Note(velocity=110, pitch=65, start=bar_start + 2.25, end=bar_start + 2.625),
    pretty_midi.Note(velocity=110, pitch=67, start=bar_start + 2.625, end=bar_start + 3.0),
    pretty_midi.Note(velocity=110, pitch=69, start=bar_start + 3.0, end=bar_start + 3.375),
    pretty_midi.Note(velocity=110, pitch=65, start=bar_start + 3.375, end=bar_start + 3.75),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
