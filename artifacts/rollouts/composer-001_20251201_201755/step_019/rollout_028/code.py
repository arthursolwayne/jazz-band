
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2 - Bb2, MIDI 53 - 57), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.75),  # F2
    pretty_midi.Note(velocity=80, pitch=55, start=1.75, end=2.0),  # G2
    pretty_midi.Note(velocity=80, pitch=52, start=2.0, end=2.25),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=57, start=2.25, end=2.5),  # C3
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.25),  # C3
    pretty_midi.Note(velocity=80, pitch=55, start=3.25, end=3.5),  # G2
    pretty_midi.Note(velocity=80, pitch=56, start=3.5, end=3.75),  # A2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.0),  # F2
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.75),  # F2
    pretty_midi.Note(velocity=80, pitch=55, start=4.75, end=5.0),  # G2
    pretty_midi.Note(velocity=80, pitch=52, start=5.0, end=5.25),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=57, start=5.25, end=5.5),  # C3
    pretty_midi.Note(velocity=80, pitch=57, start=5.5, end=5.75),  # C3
    pretty_midi.Note(velocity=80, pitch=55, start=5.75, end=6.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0),  # E5
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # F5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # Ab5
])
# Bar 4: Gm7 (G, Bb, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.0),  # G5
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.0),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # F5
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif (F5, A5, F5)
    pretty_midi.Note(velocity=110, pitch=79, start=1.5, end=1.75),  # F5
    pretty_midi.Note(velocity=110, pitch=82, start=1.75, end=2.0),  # A5
    pretty_midi.Note(velocity=110, pitch=79, start=2.0, end=2.25),  # F5
    # Bar 3: Leave it hanging (rest)
    # Bar 4: Come back and finish it (F5, C6, F5)
    pretty_midi.Note(velocity=110, pitch=79, start=4.5, end=4.75),  # F5
    pretty_midi.Note(velocity=110, pitch=85, start=4.75, end=5.0),  # C6
    pretty_midi.Note(velocity=110, pitch=79, start=5.0, end=5.25),  # F5
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    kick_start = start
    kick_end = kick_start + 0.375
    kick2_start = start + 1.125
    kick2_end = kick2_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick2_start, end=kick2_end))
    # Snare on 2 and 4
    snare_start = start + 0.75
    snare_end = snare_start + 0.125
    snare2_start = start + 1.875
    snare2_end = snare2_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end))
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare2_start, end=snare2_end))
    # Hi-hat on every eighth
    for i in range(8):
        hihat_start = start + i * 0.1875
        hihat_end = hihat_start + 0.1875
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
