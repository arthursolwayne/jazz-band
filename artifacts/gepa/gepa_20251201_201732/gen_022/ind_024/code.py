
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (38) -> C (43) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=41, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.0),
    # Bar 3: Am7 (43) -> D (46) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=46, start=2.375, end=2.5),
    # Bar 4: G7 (46) -> C (43) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=46, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=44, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=43, start=2.875, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Diane (open voicings, different chords each bar, resolve on the last)
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),  # E
]
# Bar 3: Am7 (A, C, E, G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.25),  # G
])
# Bar 4: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=79, start=2.5, end=2.75),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # F
])
piano.notes.extend(piano_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(start_time):
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start_time + i * 0.1875, end=start_time + i * 0.1875 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.append(kick)
    drums.notes.append(snare)

add_drums(1.5)
add_drums(2.0)
add_drums(2.5)

# Sax: Dante (one short motif, make it sing. Start it, leave it hanging. Come back and finish it.)
# Motif: F (65), G# (67), A (69), F (65) — start at 1.5s, leave it hanging until 3.0s, return and finish
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # G#
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
