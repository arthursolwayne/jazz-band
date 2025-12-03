
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F (root)
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # C (fifth)
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0),  # E (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.5),  # F (root)
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=4.0),  # C (fifth)
    pretty_midi.Note(velocity=100, pitch=70, start=4.0, end=4.5),  # D (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # C (fifth)
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.5),  # F (root)
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=6.0),  # C (fifth)
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),
]
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.5),
])
# Bar 4: C7 (C, E, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),
])
# Bar 4 continuation (resolve)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=4.0),
])
# Bar 4 (final)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=76, start=4.0, end=4.5),
])
# Bar 5 (final resolution)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.0),
])
# Bar 6 (final)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.5),
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.5),
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.5),
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.5),
])
piano.notes.extend(piano_notes)

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - A - D (F, A, D, rest)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(start_time):
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375),
    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=start_time, end=start_time + 0.375),
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 1.125),
    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.75, end=start_time + 1.125),
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5),
    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.125, end=start_time + 1.5),
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.5, end=start_time + 1.875),
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.5, end=start_time + 1.875)

# Bar 2
add_drums(1.5)
# Bar 3
add_drums(3.0)
# Bar 4
add_drums(4.5)

drums.notes.extend([note for note in add_drums(1.5) + add_drums(3.0) + add_drums(4.5)])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
