
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # F#2 (fifth)
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625), # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # D2 (root)

    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),  # G2 (root of next chord)
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75), # B2 (fifth)
    pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.125), # A2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.5),  # G2 (root)

    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # F#2 (root)
    pretty_midi.Note(velocity=100, pitch=46, start=4.875, end=5.25), # A#2 (fifth)
    pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=5.625), # A2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # F#2 (root)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # C#4

    # Bar 3: G7 (G, B, D, F#)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # F#5

    # Bar 4: F#7 (F#, A#, C#, E)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A#4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # C#5
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # E5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62) -> E4 (64) -> D4 (62) -> B3 (61)
# Start on 1.5s, last note at 2.0s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=61, start=2.625, end=3.0),   # B3

    # Finish the motif on beat 3 of bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),   # E4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),   # D4
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25),  # B3
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25))
    # Hihat on every eighth
    for eighth in [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]:
        start = bar_start + eighth
        end = bar_start + 1.5
        if start < end:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
