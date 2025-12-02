
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): D2 - G2 - C2 - F2 (MIDI 38-43)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # F2 on 2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # G2 on 3
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=3.0),  # E2 on 4
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # D2 on 1
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75), # F2 on 2
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125), # G2 on 3
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),  # E2 on 4
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2 on 1
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25), # F2 on 2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # G2 on 3
    pretty_midi.Note(velocity=80, pitch=40, start=5.625, end=6.0),  # E2 on 4
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, resolve on the last beat of each bar
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D (top of Dm7)
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625), # D
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25), # F#
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=6.0),  # C (resolve)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=start_time, end=start_time + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 1.125)
    # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.75, end=start_time + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)
    # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=start_time + 1.125, end=start_time + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.5, end=start_time + 1.875)
    # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=42, start=start_time + 1.5, end=start_time + 1.875)

drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
